#!/usr/bin/env python3
"""Build static reports from the working tree; no Git history or network required."""
from datetime import datetime, timezone
import html
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STYLE = '''
:root{color-scheme:light dark;--bg:#fcfcfa;--fg:#212b36;--muted:#607080;--line:#dce3e9;--accent:#2365a5}
@media(prefers-color-scheme:dark){:root{--bg:#161b20;--fg:#e0e6ec;--muted:#a3b1bf;--line:#38434e;--accent:#85baff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.7 system-ui,sans-serif}
main{max-width:900px;margin:auto;padding:38px 24px 80px}nav{display:flex;gap:20px;flex-wrap:wrap;font-size:14px;padding-bottom:22px;border-bottom:1px solid var(--line)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}h1{font-size:36px;line-height:1.2;margin-top:36px;letter-spacing:-1px}h2{font-size:25px;line-height:1.3;margin-top:38px}h3{font-size:19px;line-height:1.4;margin-top:28px}p{margin:14px 0}
.muted,footer{color:var(--muted);font-size:14px}footer{border-top:1px solid var(--line);padding-top:20px;margin-top:48px}
.metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:16px;margin:30px 0}.metric{border:1px solid var(--line);border-radius:8px;padding:18px}.metric strong{display:block;font-size:32px;line-height:1.2}.metric span{color:var(--muted);font-size:14px}
blockquote{border-left:3px solid var(--line);padding-left:18px;margin-left:0;color:var(--muted)}code{font-size:.88em}pre{padding:18px;background:var(--line);overflow:auto;border-radius:6px}li{margin:8px 0}
'''


def inline(text):
    value = html.escape(text)
    value = re.sub(r'`([^`]+)`', r'<code>\1</code>', value)
    value = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', value)
    value = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', value)
    def link(match):
        target = html.unescape(match.group(2))
        # Only ordinary document links; never execute embedded URI schemes.
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) and not target.startswith(('http://', 'https://')):
            return match.group(1)
        return '<a href="' + html.escape(target, quote=True) + '">' + match.group(1) + '</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link, value)


def markdown(text):
    """Render the headings, paragraphs, lists, and code used in these reports."""
    result, paragraph, items, code = [], [], [], None
    def flush():
        if paragraph:
            result.append('<p>' + inline(' '.join(paragraph)) + '</p>')
            paragraph.clear()
        if items:
            result.append('<ul>' + ''.join('<li>' + inline(item) + '</li>' for item in items) + '</ul>')
            items.clear()
    for line in text.splitlines():
        if line.startswith('```'):
            flush()
            if code is None:
                code = []
            else:
                result.append('<pre><code>' + html.escape('\n'.join(code)) + '</code></pre>')
                code = None
            continue
        if code is not None:
            code.append(line)
            continue
        heading = re.match(r'^(#{1,6})\s+(.+)$', line)
        item = re.match(r'^(?:[-*]|\d+\.)\s+(.+)$', line)
        if heading:
            flush()
            level = len(heading[1])
            result.append(f'<h{level}>' + inline(heading[2]) + f'</h{level}>')
        elif item:
            if paragraph:
                flush()
            items.append(item[1])
        elif not line.strip():
            flush()
        else:
            if items:
                flush()
            paragraph.append(line)
    flush()
    return '\n'.join(result)


def page(title, body):
    nav = [('progress.html', 'Overview'), ('synthesis.html', 'Synthesis'), ('themes.html', 'Themes'), ('horizons.html', 'Scenarios'), ('method.html', 'Method')]
    links = ''.join(f'<a href="{url}">{label}</a>' for url, label in nav)
    date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{html.escape(title)} | Agent Research</title><style>{STYLE}</style></head>
<body><main><nav aria-label="Reports">{links}</nav>{body}<footer>Research snapshot: 24 October 2026. Report built {date}. Hypotheses and scenarios are research arguments, not validated predictions.</footer></main></body></html>'''


def write(name, title, body):
    path = ROOT / name
    path.write_text(page(title, body), encoding='utf-8')
    print(f'Built {path.name}')


def build_progress():
    thesis = (ROOT / 'thesis.md').read_text(encoding='utf-8')
    claims = []
    for match in re.finditer(r'^## (C\d+)\.\s*(.+?)\n(.*?)(?=^## C\d+\.|\Z)', thesis, re.M | re.S):
        if not re.search(r'^Confidence:\s*retired', match[3], re.M):
            claims.append((match[1], match[2]))
    sources = len(list((ROOT / 'sources').glob('*.md')))
    live_scenarios = sum(not re.search(r'^Status:\s*retired', p.read_text(encoding='utf-8'), re.M) for p in (ROOT / 'scenarios').glob('*.md') if p.name != 'README.md')
    threads = len([p for p in (ROOT / 'threads').glob('*.md') if p.name != 'README.md'])
    metrics = ''.join(f'<div class="metric"><strong>{number}</strong><span>{label}</span></div>' for number, label in [(sources, 'Public source notes'), (len(claims), 'Live claims'), (live_scenarios, 'Live scenarios'), (threads, 'Research threads')])
    titles = ''.join(f'<li><strong>{cid}.</strong> {html.escape(title)}</li>' for cid, title in claims)
    body = '<p class="muted">A worked example of evidence-driven agent research</p><h1>How agents could change the close</h1><p>The corpus separates public evidence, defended arguments, and competing futures. Start with the synthesis, then inspect the premises and counter-evidence in the thesis.</p>' + '<div class="metrics">' + metrics + '</div>'
    body += '<h2>Current state</h2><p>This edition contains no bundled run history or fresh model scores. Counts above come from the current files. Use the offline checks to validate structure, or configure a live judge to evaluate the arguments again.</p><h2>Live claims</h2><ul>' + titles + '</ul><p><a href="thesis.md">Read full claims and source citations</a></p>'
    write('progress.html', 'Research overview', body)
    for source, output, title in [('synthesis.md','synthesis.html','Research synthesis'), ('themes.md','themes.html','Current themes'), ('horizons.md','horizons.html','Future scenarios')]:
        write(output, title, markdown((ROOT / source).read_text(encoding='utf-8')))


def build_method():
    write('method.html', 'Research method', markdown((ROOT / 'docs/methodology.md').read_text(encoding='utf-8')))
