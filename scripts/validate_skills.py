import pathlib, re, sys
root = pathlib.Path(__file__).resolve().parents[1]
ok = True
pat = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
for p in sorted((root / '.opencode' / 'skills').glob('*/SKILL.md')):
    name_dir = p.parent.name
    text = p.read_text(encoding='utf-8')
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
    if not m:
        print(f'FAIL {name_dir}: no frontmatter'); ok=False; continue
    fm = m.group(1)
    mn = re.search(r'^name:\s*(\S+)', fm, re.M)
    md = re.search(r'^description:\s*"(.*)"\s*$', fm, re.M)
    if not mn or mn.group(1) != name_dir:
        print(f'FAIL {name_dir}: name mismatch'); ok=False
    elif not pat.match(mn.group(1)) or len(mn.group(1))>64:
        print(f'FAIL {name_dir}: bad name'); ok=False
    if not md or not (1 <= len(md.group(1)) <= 1024):
        print(f'FAIL {name_dir}: description length {len(md.group(1)) if md else 0}'); ok=False
    else:
        print(f'OK {name_dir}: desc {len(md.group(1))} chars')
for c in sorted((root / '.opencode' / 'commands').glob('*.md')):
    t = c.read_text(encoding='utf-8')
    if not t.startswith('---'):
        print(f'FAIL cmd {c.name}'); ok=False
    else:
        print(f'OK cmd {c.name}')
sys.exit(0 if ok else 1)
