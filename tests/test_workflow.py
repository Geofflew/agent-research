"""Offline regression checks for evidence gating, judge failure, and clean exports."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


score = load('thesis_score', 'eval/score.py')
scenarios = load('scenario_score', 'eval/score_scenarios.py')
public = load('public_check', 'tools/check_public.py')
render = load('report_renderer', 'tools/render_reports.py')


class EvidenceChecks(unittest.TestCase):
    def test_missing_quote_cannot_pass_gate(self):
        sources = {'test-source': {'url': 'https://example.org/study', 'quotes': ['the specific finding'], 'type': 'primary'}}
        with mock.patch.object(score, 'fetch', return_value={'ok': True, 'text': 'a different finding'}):
            gate, _, reasons = score.ground_code({'slugs': ['test-source']}, sources)
        self.assertEqual(gate, 0)
        self.assertTrue(any('quote not found' in reason for reason in reasons))

    def test_verified_text_is_required_for_unavailable_source(self):
        source = {'url': 'https://example.org/study', 'quotes': ['a documented premise'], 'type': 'primary'}
        with mock.patch.object(score, 'fetch', return_value={'ok': False, 'err': 'offline'}), mock.patch.object(score, '_VER', set()):
            gate, _, _ = score.ground_code({'slugs': ['test-source']}, {'test-source': source})
        self.assertEqual(gate, 0)

    def test_current_claim_citations_resolve_offline(self):
        with mock.patch.object(score, 'fetch', side_effect=AssertionError('network forbidden')), mock.patch.object(score, 'judge', side_effect=AssertionError('judge forbidden')):
            score.check_local()
        with mock.patch.object(scenarios, 'judge', side_effect=AssertionError('judge forbidden')):
            scenarios.check_local()


class JudgeChecks(unittest.TestCase):
    def test_cli_failure_is_not_a_score(self):
        failure = subprocess.CompletedProcess([], 1, stdout='', stderr='unavailable')
        with tempfile.TemporaryDirectory() as temp, mock.patch.object(score, 'CACHE', temp), mock.patch.object(score.subprocess, 'run', return_value=failure):
            with self.assertRaisesRegex(RuntimeError, 'valid samples'):
                score.judge({'id': 'C0', 'text': 'test claim'}, ['premise'], 'question', 'rubric')
            self.assertEqual(list(Path(temp).iterdir()), [])
        with tempfile.TemporaryDirectory() as temp, mock.patch.object(scenarios, 'CACHE', temp), mock.patch.object(scenarios.subprocess, 'run', return_value=failure):
            with self.assertRaisesRegex(RuntimeError, 'valid samples'):
                scenarios.judge('scenario', 'question', 'rubric', 'titles', 3)
            self.assertEqual(list(Path(temp).iterdir()), [])

    def test_out_of_range_judge_output_is_rejected(self):
        invalid = {dimension: 9 for dimension in score.DIMS}
        output = subprocess.CompletedProcess([], 0, stdout=json.dumps({'result': json.dumps(invalid)}))
        with tempfile.TemporaryDirectory() as temp, mock.patch.object(score, 'CACHE', temp), mock.patch.object(score.subprocess, 'run', return_value=output):
            with self.assertRaises(RuntimeError):
                score.judge({'id': 'C0', 'text': 'test claim'}, [], 'question', 'rubric')

    def test_cache_distinguishes_question_and_model(self):
        valid = {dimension: 1 for dimension in score.DIMS}
        output = subprocess.CompletedProcess([], 0, stdout=json.dumps({'result': json.dumps(valid)}))
        with tempfile.TemporaryDirectory() as temp, mock.patch.object(score, 'CACHE', temp), mock.patch.object(score.subprocess, 'run', return_value=output) as run:
            # Cache each call in the temporary directory; direct the diagnostic log there too.
            with mock.patch.object(score, 'ROOT', temp):
                args = ({'id': 'C0', 'text': 'claim'}, ['premise'], 'question A', 'rubric')
                score.judge(*args)
                score.judge(*args)
                self.assertEqual(run.call_count, 3)
                score.judge(args[0], args[1], 'question B', args[3])
                self.assertEqual(run.call_count, 6)
                with mock.patch.object(score, 'JUDGE_MODEL', 'another-model'):
                    score.judge(*args)
                self.assertEqual(run.call_count, 9)


class ExportChecks(unittest.TestCase):
    def test_deny_terms_include_encoded_content_and_filenames(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'note.md').write_text('Ac&#109;e private example', encoding='utf-8')
            (root / 'ACME-record.md').write_text('example', encoding='utf-8')
            _, issues = public.audit(root, ['acme'])
            self.assertEqual(len(issues), 2)

    def test_local_credentials_and_private_source_endpoints_fail(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / '.env').write_text('placeholder', encoding='utf-8')
            (root / 'source.md').write_text('URL: http://127.0.0.1/private', encoding='utf-8')
            _, issues = public.audit(root)
            self.assertTrue(any('environment' in issue for issue in issues))
            self.assertTrue(any('non-public source' in issue for issue in issues))

    def test_reports_build_without_git_history(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for folder in ('sources', 'scenarios', 'threads', 'docs'):
                (root / folder).mkdir()
            (root / 'thesis.md').write_text('## C1. A sample argument\n\nConfidence: weak\n', encoding='utf-8')
            for path in ('synthesis.md', 'themes.md', 'horizons.md', 'docs/methodology.md'):
                (root / path).write_text('# Example\n\n<script>alert(1)</script>\n', encoding='utf-8')
            with mock.patch.object(render, 'ROOT', root):
                render.build_progress()
                render.build_method()
            self.assertIn('Live claims', (root / 'progress.html').read_text())
            rendered = (root / 'synthesis.html').read_text()
            self.assertNotIn('<script>', rendered)
            self.assertIn('&lt;script&gt;', rendered)
            self.assertTrue((root / 'method.html').exists())


if __name__ == '__main__':
    unittest.main()
