"""Parse the question pages of a UPTET solved-paper PDF.

Usage: parse_uptet.py <pdf> <lines.json> <last question page> <out.json>

Reads the font-tagged lines from extract_lines.py, converts the legacy Hindi,
and splits each question into English/Hindi stem and options. Figures and
stacked maths are flagged for manual repair rather than guessed.
"""
import json
import re
import sys

import pymupdf

sys.path.insert(0, __file__.rsplit('\\', 1)[0].rsplit('/', 1)[0])
from aps2uni import convert  # noqa: E402

SYMBOL_PIECES = re.compile('[-]')
SYMBOL_MAP = {'': '', '': '', '': '', '': '', '': '', '': ''}
DEVANAGARI_LETTER = re.compile('[ऄ-हक़-ॡ]')
HEADER = re.compile(
    r'^(PART|Part)\s*[–-]|^(Child Development|Language|Mathematics|Environmental|Science|Social|Hindi|English|Sanskrit)\b'
    r'|^(भाग|बाल विकास|भाषा|गणित|पर्यावरण|विज्ञान|सामाजिक|हिन्दी|अंग्रेजी|संस्कृत)'
    r'|परीक्षा तिथि|पात्रता परीक्षा|Class \(?[IV6]|प्रथम प्रश्न|व्याख्या सहित|Page \d+$')


PASSAGE_INTRO = re.compile(r'(निम्नलिखित (गद्यांश|पद्यांश|अवतरण|काव्यांश)|निर्देश|Directions?\b|Read the (following|passage|poem))')


def seg_text(kind, text):
    if kind == 'hi':
        # A lone x in the Hindi font is a maths variable, not a vowel sign.
        parts = re.split(r'(?<![^\s(])x(?![^\s),.?])', text)
        return 'x'.join(convert(p) for p in parts)
    if kind == 'RupeeForadian':
        return text.replace('`', '₹')
    if kind in ('Wingdings2', 'Webdings'):
        return '□'
    return text


def line_text(segs):
    return ''.join(t for _, t in segs)


def split_off(segs, n):
    """Drops the first n characters of a run of segments."""
    out = []
    for k, t in segs:
        if n >= len(t):
            n -= len(t)
            continue
        out.append((k, t[n:]))
        n = 0
    return out


def split_options(segs):
    """[(option id or None, segments)] for a line holding zero or more "(a)" labels."""
    pieces = [[None, []]]
    for k, t in segs:
        parts = re.split(r'(?:^|(?<=\s))\(([a-d])\)\s*', t) if k == 'en' else [t]
        pieces[-1][1].append((k, parts[0]))
        for j in range(1, len(parts), 2):
            pieces.append([parts[j], [(k, parts[j + 1])]])
    if not clean(line_text(pieces[0][1])) and len(pieces) > 1:
        pieces.pop(0)
    return [tuple(p) for p in pieces]


def split_lang(segs):
    """English part and Hindi part of a run of (kind, converted text) segments."""
    first_hi = next((i for i, (k, t) in enumerate(segs) if k == 'hi' and DEVANAGARI_LETTER.search(t)), None)
    if first_hi is None:
        return clean(line_text(segs)), None
    en = line_text(segs[:first_hi])
    hi = line_text(segs[first_hi:])
    head, sep, tail = en.rpartition('/')
    if sep and not re.search('[A-Za-z]', tail):
        en, hi = head, tail + hi
    if not DEVANAGARI_LETTER.search(hi):
        hi = None
    return clean(en) or None, clean(hi) if hi else None


def clean(s):
    s = re.sub(r'\s+', ' ', s or '').strip()
    s = re.sub(r'\s+([?,.।:;)])', r'\1', s)
    s = re.sub(r'([(‘“])\s+', r'\1', s)
    return s.strip(' /')


def main():
    pdf, lines_path, last_page, out_path = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    doc = pymupdf.open(pdf)
    image_pages = {i for i, p in enumerate(doc) if p.get_images()}
    lines = [l for l in json.load(open(lines_path, encoding='utf-8')) if l[0] <= last_page]

    questions = []
    cur = None
    part = None
    expected = 1
    passage = None
    for pno, y, x, segs in lines:
        # Page footers, and the title block above part I on the first page.
        if any(k == 'footer' for k, _ in segs) or (pno == 0 and y < 112):
            continue
        segs = [(k, seg_text(k, t)) for k, t in segs]
        text = clean(line_text(segs))
        if not text:
            continue
        if passage is not None and not re.match(r'(\d{1,3})\.(\s|$)', text):
            passage.append(text)
            continue
        if cur is not None and len(cur['options']) == 4 and PASSAGE_INTRO.match(text):
            passage = cur['passage_after'] = [text]
            continue
        passage = None
        m = re.match(r'(\d{1,3})\.(\s|$)', text)
        if m and (int(m[1]) == expected or (int(m[1]) == 61 and expected == 91)):
            num = int(m[1])
            expected = num + 1
            segs = split_off(segs, len(m[0]))
            cur = {'num': num, 'page': pno, 'stem': [], 'options': [], 'extra': [], 'part': part,
                   'passage_after': None}
            questions.append(cur)
            if not clean(line_text(segs)):
                continue
            text = clean(line_text(segs))
        if HEADER.search(text) and (cur is None or cur['options']):
            part = text if re.match('PART|Part', text) else part
            if cur is not None:
                cur['extra'].append(('header', text))
            continue
        if cur is None:
            continue
        for oid, osegs in split_options(segs):
            expected_option = 'abcd'[len(cur['options'])] if len(cur['options']) < 4 else None
            if oid is not None and oid == expected_option:
                cur['options'].append({'id': oid, 'segs': osegs})
                continue
            if oid is not None:
                osegs = [('en', f'({oid}) ')] + osegs
            if cur['options']:
                cur['options'][-1]['segs'] += [('en', ' ')] + osegs
            else:
                cur['stem'] += [('en', ' ')] + osegs

    out = []
    for q in questions:
        en, hi = split_lang(q['stem'])
        opts = []
        for o in q['options']:
            oen, ohi = split_lang(o['segs'])
            opts.append({'id': o['id'], 'en': oen, 'hi': ohi})
        raw = ''.join(t for _, t in q['stem']) + ''.join(t for o in q['options'] for _, t in o['segs'])
        flags = []
        if SYMBOL_PIECES.search(raw):
            flags.append('stacked-maths')
        if q['page'] in image_pages:
            flags.append('page-has-image')
        if [o['id'] for o in opts] != ['a', 'b', 'c', 'd']:
            flags.append('options:' + ''.join(o['id'] for o in opts))
        out.append({'num': q['num'], 'page': q['page'], 'part': q['part'], 'en': en, 'hi': hi,
                    'options': opts, 'flags': flags, 'extra': q['extra'],
                    'passage_after': q['passage_after']})
    json.dump(out, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(out), 'questions;', 'numbers:', ' '.join(str(q['num']) for q in out))


main()
