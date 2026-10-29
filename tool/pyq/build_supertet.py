"""Adds the UP Super TET (Assistant Teacher Recruitment Exam) 2019 paper to the content pack.

Usage: build_supertet.py <st19.pdf> <content_pack.json> [review.txt]
       build_supertet.py <st19.pdf> --dump <out.txt>     (parsed questions, before fixes)

The PDF is the typeset booklet (Series A) with the answer keys at the end. Each section of the
paper is a module in `st19/` with TOPICS, SKIP, FIX and EXPLAIN. Re-running replaces the paper
and questions added by a previous run.
"""
import importlib
import json
import re
import sys

import pymupdf

sys.path.insert(0, __file__.replace('\\', '/').rsplit('/', 1)[0])
sys.stdout.reconfigure(encoding='utf-8')

PAPER_ID = 'supertet-2019'
QPREFIX = 'q-supertet19'
SECTIONS = ['hin', 'san', 'eng', 'gk', 'cdp', 'sci', 'math', 'ca', 'life', 'reason', 'ict']
EXAM = ('UP Super TET 2019 (Assistant Teacher Recruitment Exam, ATRE 2019), held on 6 January 2019 by the Pariksha '
        'Niyamak Pradhikari (Examination Regulatory Authority), Uttar Pradesh, Prayagraj')
PASSAGE_PROMPT = {
    ('hi', 'prose'): 'नीचे दिए गए गद्यांश को पढ़कर प्रश्न का उत्तर दीजिए।',
    ('en', 'prose'): 'Read the passage below and answer the question.',
}

# (id, language, name en, name hi, topics) for subjects this paper adds or extends.
SUBJECTS = [
    ('hin', 'hi', None, None, []),
    ('san', 'hi', 'Sanskrit', 'संस्कृत',
     [('san.vyakaran', 'Grammar (Vyakaran)', 'व्याकरण'),
      ('san.shloka', 'Verses and vocabulary', 'श्लोक एवं शब्दार्थ')]),
    ('eng', 'en', None, None, []),
    ('gk', None, 'General Knowledge & Current Affairs', 'सामान्य ज्ञान एवं समसामयिकी',
     [('gk.history', 'History and the freedom struggle', 'इतिहास एवं स्वतंत्रता संग्राम'),
      ('gk.polity', 'Polity and economy', 'राजव्यवस्था एवं अर्थव्यवस्था'),
      ('gk.geography', 'Geography and environment', 'भूगोल एवं पर्यावरण'),
      ('gk.culture', 'Art, culture and literature', 'कला, संस्कृति एवं साहित्य'),
      ('gk.current', 'Current affairs', 'समसामयिकी')]),
    ('cdp', None, None, None,
     [('cdp.policy', 'Teaching, policy and administration', 'शिक्षण, शैक्षिक नीति एवं प्रशासन')]),
    ('sci', None, None, None, []),
    ('math', None, None, None, []),
    ('life', None, 'Life Skills, Management & Aptitude', 'जीवन कौशल, प्रबंधन एवं अभिवृत्ति',
     [('life.skills', 'Life skills and values', 'जीवन कौशल एवं मूल्य'),
      ('life.motivation', 'Motivation and guidance', 'अभिप्रेरणा एवं निर्देशन')]),
    ('reason', None, 'Reasoning', 'तार्किक क्षमता',
     [('reason.logic', 'Relations, directions and coding', 'संबंध, दिशा एवं कूटभाषा')]),
    ('ict', None, 'Information & Communication Technology', 'सूचना एवं संचार प्रौद्योगिकी',
     [('ict.basics', 'Computer and ICT basics', 'कंप्यूटर एवं आईसीटी की मूल बातें')]),
]

HEADER = re.compile(r'^(ATR–2019 · UP Super TET|प्रश्न-पुस्तिका सीरीज़ / Booklet Series A|\d{1,2})$')
QSTART = re.compile(r'^(\d{1,3})\.\s*(.*)$')
OPTION = re.compile(r'^\((\d)\)\s*(.*)$')


def tidy(text):
    """Joins wrapped lines and undoes the PDF's quirks: doubled vowel signs (ज्ञाान, राष्ट्रीीय), the
    raised-dot decimal point and opening quotes used as apostrophes."""
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'([ा-ौँ-ः])\1+', r'\1', text)
    text = re.sub(r'(ां)+', 'ां', text)
    text = re.sub(r'(?<=\d)·(?=\d)', '.', text)
    text = re.sub(r'(?<=[A-Za-z])‘s\b', '’s', text)
    # "the following sentence : One should ..." puts the sentence on its own line.
    return re.sub(r'(?<=[a-z]) ?: (?=[A-Z])', ':\n', text)


def is_heading(line, following):
    return '· ' in line and not line.startswith(('ATR', '(')) or following.startswith('· ')


def parse(pdf):
    """{n: {'hi': (text, [4 options]) | None, 'en': ..., 'passage': (lang, text) | None}} and the Series A key."""
    doc = pymupdf.open(pdf)
    lines = []
    for page in doc:
        page_lines = page.get_text().splitlines()
        while page_lines and HEADER.match(page_lines[0].strip()):
            page_lines.pop(0)
        lines += [l.strip() for l in page_lines if l.strip()]
    start = next(i for i, l in enumerate(lines) if l.startswith('भाषा — हिन्दी'))
    end = next(i for i, l in enumerate(lines) if l.startswith('अनुदेश / Instructions'))
    body, key_lines = lines[start:end], lines[end:]

    questions, current, expect, passage = {}, None, 1, None
    for i, line in enumerate(body):
        following = body[i + 1] if i + 1 < len(body) else ''
        if is_heading(line, following):
            continue
        m = QSTART.match(line)
        if m and int(m.group(1)) in (expect, expect - 1) and (current is None or len(current['opts']) == 4):
            n = int(m.group(1))
            lang = 'en' if not re.search('[ऀ-ॿ]', line + following) else 'hi'
            current = {'n': n, 'lang': lang, 'stem': [m.group(2)] if m.group(2) else [], 'opts': []}
            entry = questions.setdefault(n, {'hi': None, 'en': None, 'passage': None, 'parts': []})
            entry['parts'].append(current)
            if passage:
                for t in passage['targets']:
                    questions.setdefault(t, {'hi': None, 'en': None, 'passage': None, 'parts': []})
                    questions[t]['passage'] = (passage['lang'], tidy(' '.join(passage['lines'])))
                passage = None
            expect = n + 1
            continue
        if current is None:
            continue
        if line.startswith(('निर्देश', 'Direction')) and len(current['opts']) == 4:
            nums = [int(x) for x in re.findall(r'[0-9]+', line)[:2]] or [current['n'] + 1, current['n'] + 2]
            passage = {'lang': 'hi' if line.startswith('निर्देश') else 'en', 'targets': nums, 'lines': [], 'head': True}
            continue
        if passage is not None:
            if passage.pop('head', False) is False or not re.search(r'[।.:]$', line):
                passage['lines'].append(line)
            continue
        o = OPTION.match(line)
        if o and int(o.group(1)) == len(current['opts']) + 1:
            current['opts'].append([o.group(2)])
        elif current['opts']:
            current['opts'][-1].append(line)
        else:
            current['stem'].append(line)

    for n, entry in questions.items():
        for part in entry.pop('parts'):
            entry[part['lang']] = (tidy(' '.join(part['stem'])), [tidy(' '.join(o)) for o in part['opts']])

    digits = [int(l) for l in key_lines[key_lines.index('A'):] if l.isdigit()]
    key = {}
    for q, a in zip(digits[0::2], digits[1::2]):
        if q in key or not 1 <= q <= 150:
            break
        key[q] = str(a)
    assert sorted(key) == list(range(1, 151)), sorted(set(range(1, 151)) - set(key))
    return questions, key


def dump_parsed(questions, key, out):
    with open(out, 'w', encoding='utf-8') as f:
        for n in sorted(questions):
            q = questions[n]
            f.write(f'\n== {n} key {key.get(n)}\n')
            if q['passage']:
                f.write(f"  passage[{q['passage'][0]}]: {q['passage'][1]}\n")
            for lang in ('hi', 'en'):
                if q[lang]:
                    text, opts = q[lang]
                    f.write(f'  {lang}: {text}\n')
                    for i, o in enumerate(opts, 1):
                        f.write(f'     ({i}) {o}\n')


def build_question(n, mod, parsed, key, problems):
    fix = mod.FIX.get(n, {})
    language = mod.LANGUAGE
    text, options = {}, [{}, {}, {}, {}]
    for lang in ('hi', 'en'):
        if language and lang != language:
            continue
        stem, opts = parsed[lang] if parsed[lang] else (None, [None] * 4)
        stem = fix.get(lang, stem)
        if stem is None:
            continue
        if parsed['passage'] and lang == parsed['passage'][0] and 'passage' not in fix.get('keep', ''):
            stem = f"{PASSAGE_PROMPT[(lang, 'prose')]}\n\n{parsed['passage'][1]}\n\n{stem}"
        text[lang] = stem
        for i, o in enumerate(opts):
            override = fix.get('options', {}).get(i + 1)
            if override is not None:
                o = override[0 if lang == 'en' else 1]
            if o is None:
                problems.append(f'{n}: option {i + 1} missing {lang}')
            options[i][lang] = o
    explanation = dict(zip(('en', 'hi'), mod.EXPLAIN[n]))
    explanation = {l: t for l, t in explanation.items() if t and (not language or l == language)}
    topic = next(t for t, nums in mod.TOPICS.items() if n in nums)
    for lang in text:
        if len(options) != 4 or not all(o.get(lang) for o in options):
            problems.append(f'{n}: incomplete {lang} options')
        if lang not in explanation:
            problems.append(f'{n}: no {lang} explanation')
        if re.search(r'\d[a-z]\d|\b[a-z]\d\b', text[lang] + ' '.join(o.get(lang, '') for o in options)) \
                and n not in getattr(mod, 'PLAIN_OK', ()):
            problems.append(f'{n}: possible lost superscript in {lang}')
    return {
        'id': f'{QPREFIX}-{n:03d}',
        'subject_id': topic.split('.')[0],
        'topic_id': topic,
        'text': text,
        'options': [{'id': str(i + 1), 'text': o} for i, o in enumerate(options)],
        'correct_option_id': key[n],
        'explanation': explanation,
        'source': f'{EXAM}. Booklet Series A, question {n}. Answer from the answer key published with the booklet '
                  f'(dated 8 January 2019), checked against the final key. Explanation written by '
                  f'UPTET Saathi.',
        'verification_status': 'verified',
    }


def main():
    pdf = sys.argv[1]
    questions, key = parse(pdf)
    if sys.argv[2] == '--dump':
        dump_parsed(questions, key, sys.argv[3])
        print(f'{len(questions)} questions parsed')
        return
    pack_path = sys.argv[2]
    review_path = sys.argv[3] if len(sys.argv) > 3 else None

    problems, built, skipped = [], [], []
    covered = []
    for sec in SECTIONS:
        mod = importlib.import_module(f'st19.{sec}')
        first, last = mod.RANGE
        topic_nums = sorted(n for nums in mod.TOPICS.values() for n in nums)
        expected = sorted(set(range(first, last + 1)) - set(mod.SKIP))
        assert topic_nums == expected, (sec, set(topic_nums) ^ set(expected))
        for n in range(first, last + 1):
            covered.append(n)
            if n in mod.SKIP:
                skipped.append(n)
                continue
            built.append(build_question(n, mod, questions[n], key, problems))
    assert covered == list(range(1, 151))

    pack = json.load(open(pack_path, encoding='utf-8'))
    pack['papers'] = [p for p in pack['papers'] if not p['id'].startswith('supertet-')]
    pack['questions'] = [q for q in pack['questions'] if not q['id'].startswith('q-supertet')]

    by_id = {s['id']: s for s in pack['subjects']}
    for sid, language, en, hi, topics in SUBJECTS:
        if sid not in by_id:
            by_id[sid] = {'id': sid, 'name': {'en': en, 'hi': hi}, **({'language': language} if language else {}),
                          'topics': []}
            pack['subjects'].append(by_id[sid])
        known = {t['id'] for t in by_id[sid]['topics']}
        by_id[sid]['topics'] += [{'id': t, 'name': {'en': e, 'hi': h}} for t, e, h in topics if t not in known]

    ids = [q['id'] for q in built]
    paper = {
        'id': PAPER_ID,
        'title': {'en': 'Super TET 2019 · Primary level (Classes I–V) · Assistant Teacher Recruitment Exam',
                  'hi': 'सुपर टीईटी 2019 · प्राथमिक स्तर (कक्षा 1–5) · सहायक अध्यापक भर्ती परीक्षा'},
        'year': 2019,
        'paper_code': 'ATRE-2019-A',
        'exam': 'supertet',
        'level': 'primary',
        'is_official_pyq': True,
        'distribution_cleared': True,
        'duration_minutes': 150,
        'marking': {'correct': 1, 'incorrect': 0, 'unanswered': 0},
        'pdf_asset': f'assets/pdfs/{PAPER_ID}.pdf',
        'source': f'{EXAM}: question booklet Series A and the answer key dated 8 January 2019, from a retypeset '
                  f'copy of the booklet, checked against the official booklet and final key. '
                  + (f'Question{"s" if len(skipped) > 1 else ""} {", ".join(map(str, skipped))} '
                     f'{"are" if len(skipped) > 1 else "is"} left out (no single accepted answer, or the answer '
                     f'has changed since the exam). ' if skipped else '')
                  + 'Explanations are by UPTET Saathi.',
        'question_count': len(ids),
        'question_ids': ids,
    }
    pack['papers'].insert(next((i for i, p in enumerate(pack['papers']) if p['id'].startswith('ctet-')),
                               len(pack['papers'])), paper)
    pack['questions'] += built
    pack['content_version'] = '2026.10.30-release.1'

    open(pack_path, 'w', encoding='utf-8', newline='\n').write(dump(pack) + '\n')
    print(f'{PAPER_ID}: {len(ids)} questions; skipped {skipped}')
    print(len(problems), 'problems')
    for line in problems:
        print(' -', line)
    if review_path:
        with open(review_path, 'w', encoding='utf-8') as f:
            for q in built:
                f.write(f"\n{q['id']} [{q['topic_id']}] answer {q['correct_option_id']}\n")
                for l, t in q['text'].items():
                    f.write(f'  {l}: {t}\n')
                for o in q['options']:
                    f.write(f"  {o['id']}) {' || '.join(o['text'].values())}\n")
                for l, t in q['explanation'].items():
                    f.write(f'  why[{l}]: {t}\n')


def inline(o):
    if isinstance(o, dict):
        return '{ ' + ', '.join(f'{json.dumps(k)}: {inline(v)}' for k, v in o.items()) + ' }'
    if isinstance(o, list):
        return '[' + ', '.join(inline(v) for v in o) + ']'
    return json.dumps(o, ensure_ascii=False)


def dump(o, ind=0, key=None):
    pad, inner = '  ' * ind, '  ' * (ind + 1)
    if isinstance(o, dict):
        if key in ('name', 'marking') or len(inline(o)) <= 110:
            return inline(o)
        body = ',\n'.join(f'{inner}{json.dumps(k)}: {dump(v, ind + 1, k)}' for k, v in o.items())
        return '{\n' + body + '\n' + pad + '}'
    if isinstance(o, list):
        if key == 'question_ids':
            rows = [', '.join(json.dumps(v) for v in o[i:i + 5]) for i in range(0, len(o), 5)]
            return '[\n' + ',\n'.join(inner + r for r in rows) + '\n' + pad + ']'
        if key in ('options', 'topics'):
            return '[\n' + ',\n'.join(inner + inline(v) for v in o) + '\n' + pad + ']'
        return '[\n' + ',\n'.join(inner + dump(v, ind + 1) for v in o) + '\n' + pad + ']'
    return json.dumps(o, ensure_ascii=False)


main()
