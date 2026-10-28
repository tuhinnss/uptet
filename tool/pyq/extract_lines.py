"""visible text lines of a PDF as font-tagged segments.

Spans are grouped into visual lines per column (by baseline) and sorted left
to right, so justified lines that the PDF splits into pieces come back whole.
Small raised or lowered spans are attached to their line as superscripts or
subscripts.

Output JSON: [[page, y, x, [[kind, text], ...]], ...] where kind is
"hi" (APS-DV legacy Devanagari, still encoded), "en", "footer", or the font name.
"""
import json
import statistics
import sys

import pymupdf

COLUMN_SPLIT = 297.5
SUP = str.maketrans('0123456789+-−–()=abcnxyozmi', '⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁻⁽⁾⁼ᵃᵇᶜⁿˣʸ°ᶻᵐⁱ')
SUB = str.maketrans('0123456789+-−()=aeoxn', '₀₁₂₃₄₅₆₇₈₉₊₋₋₍₎₌ₐₑₒₓₙ')


def kind(font):
    if font.startswith('APS-DV'):
        return 'hi'
    if font.startswith('Helvetica'):
        return 'footer'
    if font.startswith('TimesNewRoman'):
        return 'en'
    return font


def script(text, table):
    """Text in super/subscript form, or plain when a character has no such form."""
    t = text.strip()
    converted = t.translate(table)
    if any(c == o and not c.isspace() for c, o in zip(converted, t)):
        return t if t.isalpha() else '^' + t if table is SUP else '_' + t
    return converted


doc = pymupdf.open(sys.argv[1])
out = []
for pno, page in enumerate(doc):
    spans = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                if not s['text']:
                    continue
                x0 = s['bbox'][0]
                col = 0 if x0 < COLUMN_SPLIT else 1
                spans.append([col, s['origin'][1], x0, s['bbox'][2], kind(s['font']), s['text'], s['size']])
    if not spans:
        continue
    normal = statistics.median(s[6] for s in spans if s[5].strip())
    small = [s for s in spans if s[6] < 0.8 * normal and s[5].strip() and s[4] in ('en', 'Symbol')]
    spans = [s for s in spans if s not in small]
    spans.sort(key=lambda s: (s[0], s[1], s[2]))
    rows = []
    for sp in spans:
        if rows and rows[-1][0] == sp[0] and abs(rows[-1][1] - sp[1]) < 3:
            rows[-1][2].append(sp)
        else:
            rows.append([sp[0], sp[1], [sp]])
    for sp in small:
        near = [r for r in rows if r[0] == sp[0] and abs(r[1] - sp[1]) < 9]
        if not near:
            continue
        row = min(near, key=lambda r: abs(r[1] - sp[1]))
        sp = list(sp)
        sp[5] = script(sp[5], SUP if sp[1] < row[1] - 1 else SUB)
        row[2].append(sp)
    for col, y, row in rows:
        row.sort(key=lambda s: s[2])
        segs = []
        prev_x1 = None
        for _, _, x0, x1, k, t, size in row:
            # Restore the space a justified line loses between separate pieces.
            if prev_x1 is not None and x0 - prev_x1 > 1.5 and not t.startswith(' ') and size >= 0.8 * normal:
                if segs and not segs[-1][1].endswith(' '):
                    t = ' ' + t
            prev_x1 = x1
            if segs and segs[-1][0] == k:
                segs[-1][1] += t
            else:
                segs.append([k, t])
        if any(t.strip() for _, t in segs):
            out.append([pno, round(y, 1), round(row[0][2], 1), segs])
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False)
print(len(out), 'lines')
