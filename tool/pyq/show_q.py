"""compact listing of parsed questions with the answer key.

Usage: show_q.py <name> <first> <last> [occurrence] [width]   (run inside the data directory)
Occurrence 1 selects the second run of 61–90 (Sanskrit).
"""
import json
import re
import sys

import pymupdf

sys.stdout.reconfigure(encoding='utf-8')
name = sys.argv[1]
lo, hi = int(sys.argv[2]), int(sys.argv[3])
occurrence = int(sys.argv[4]) if len(sys.argv) > 4 else 0
width = int(sys.argv[5]) if len(sys.argv) > 5 else 400

doc = pymupdf.open(f'{name}.pdf')
text = next(p.get_text() for p in doc if 'Answer Key' in p.get_text())
keys, section = {}, 'main'
for line in text.splitlines():
    if line.startswith('Q.') and 'Language II: English' in line:
        section = 'english'
    elif line.startswith('Q.') and 'Sanskrit' in line:
        section = 'sanskrit'
    elif line.startswith('Q. 91'):
        section = 'main'
    for n, a in re.findall(r'(\d+)\. \(([a-d*/]+)\)', line):
        keys[(section, int(n))] = a
notes = [l for l in text.splitlines() if l.startswith('Q. ') and ':' in l and 'Q. 1 ' not in l and ' - ' not in l[:12]]

qs = json.load(open(f'{name}.q.json', encoding='utf-8'))
seen = {}
for q in qs:
    n = q['num']
    seen[n] = seen.get(n, -1) + 1
    if not (lo <= n <= hi) or seen[n] != occurrence:
        continue
    sec = 'main' if not 61 <= n <= 90 else ('english' if occurrence == 0 else 'sanskrit')
    print(f"#{n} key={keys.get((sec, n))} p{q['page']} {' '.join(q['flags'])}"[:width])
    if q['en']:
        print('  E:', q['en'][:width])
    if q['hi']:
        print('  H:', q['hi'][:width])
    for o in q['options']:
        print(f"  {o['id']}) {o['en']}  ||  {o['hi']}"[:width])
    if q['passage_after']:
        print('  PASSAGE AFTER:', ' / '.join(q['passage_after'])[:width * 3])
for n in notes:
    print('NOTE', n)
