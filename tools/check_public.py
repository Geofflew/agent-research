#!/usr/bin/env python3
"""Scan a public working tree for local artifacts, obvious secrets, and optional deny terms."""
import argparse
import html
import ipaddress
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {'.git', '.cache', '__pycache__', '.venv'}
SECRET_PATTERNS = [
    re.compile(r'gh[pousr]_[A-Za-z0-9]{30,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{40,}'),
    re.compile(r'(?<![A-Za-z0-9_-])sk-(?:ant-)?[A-Za-z0-9_-]{30,}'),
    re.compile(r'AKIA[A-Z0-9]{16}'),
    re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
    re.compile(r'https?://[^\s/@:]+:[^\s/@]+@'),
]


def normalized(text):
    for _ in range(3):
        text = html.unescape(unquote(text))
    text = unicodedata.normalize('NFKC', text).casefold()
    return ''.join(c for c in text if unicodedata.category(c) != 'Cf')


def audit(root, deny_terms=()):
    problems = []
    count = 0
    terms = [normalized(t) for t in deny_terms if t]
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if any(part in SKIP_DIRS for part in relative.parts):
            continue
        if path.is_symlink():
            problems.append(f'{relative}: symbolic links are excluded from public exports')
            continue
        if not path.is_file():
            continue
        count += 1
        if path.name == '.env' or (path.name.startswith('.env.') and path.name != '.env.example') or path.suffix in {'.pem', '.key', '.zip'}:
            problems.append(f'{relative}: local environment, key, or archive file')
        if relative.parts[0] in {'log', 'locks'} or path.name in {'judge-log.tsv', 'results.tsv', 'verified-quotes.tsv', 'verdicts.tsv', 'verdict-titles.tsv'}:
            problems.append(f'{relative}: local research run state')
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeError:
            problems.append(f'{relative}: binary file needs separate review')
            continue
        if any(term in normalized(str(relative)) or term in normalized(text) for term in terms):
            problems.append(f'{relative}: denied term in filename or decoded content')
        for line_number, line in enumerate(text.splitlines(), 1):
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                problems.append(f'{relative}:{line_number}: possible credential; matched value withheld')
            if re.search(r'/(?:Users|workspace)/[^\s"\x27]+', line):
                problems.append(f'{relative}:{line_number}: machine-specific path')
            if line.startswith('URL:'):
                host = urlsplit(line[4:].strip()).hostname or ''
                private = host in {'localhost', 'metadata.google.internal'} or host.endswith(('.local', '.internal'))
                try:
                    private = private or not ipaddress.ip_address(host).is_global
                except ValueError:
                    pass
                if private:
                    problems.append(f'{relative}:{line_number}: non-public source endpoint')
    return count, problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--deny-term', action='append', default=[], help='Case-insensitive literal to exclude; may be repeated')
    args = parser.parse_args()
    count, problems = audit(ROOT, args.deny_term)
    if problems:
        print('\n'.join(problems), file=sys.stderr)
        return 1
    print(f'Public-tree check passed: {count} text files scanned; no configured findings.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
