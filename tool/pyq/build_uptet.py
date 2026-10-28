"""adds the UPTET previous papers (2018, 2019, 2021) to the content pack.

Usage: build_uptet.py <dir with *.pdf and *.q.json> <content_pack.json> [review.txt]

Re-running replaces the papers and questions added by a previous run.
"""
import importlib
import json
import re
import sys

import pymupdf

sys.path.insert(0, __file__.replace('\\', '/').rsplit('/', 1)[0])

data_dir, pack_path = sys.argv[1], sys.argv[2]
review_path = sys.argv[3] if len(sys.argv) > 3 else None
sys.stdout.reconfigure(encoding='utf-8')

LANG = {'hin': 'hi', 'eng': 'en'}
SOLVED_PAPER = ('Text and answers are taken from a published solved paper (Youth Competition Times) and are still to be '
                'checked against the official question booklet and final answer key.')
BY_PNP = 'by the Pariksha Niyamak Pradhikari (Examination Regulatory Authority), Uttar Pradesh, Prayagraj'
EXAM19 = f'UPTET 2019 (Uttar Pradesh Teacher Eligibility Test), held on 8 January 2020 {BY_PNP}'
EXAM18 = f'UPTET 2018 (Uttar Pradesh Teacher Eligibility Test), held on 18 November 2018 {BY_PNP}'
EXAM21P = (f'UPTET 2021 (Uttar Pradesh Teacher Eligibility Test), exam of 28 November 2021 {BY_PNP}; this sitting '
           f'was cancelled after the paper leaked, and the exam was held again on 23 January 2022 with a new paper')
EXAM21 = f'UPTET 2021 (Uttar Pradesh Teacher Eligibility Test), held on 23 January 2022 {BY_PNP}'
# Stray vowel signs the legacy font conversion leaves after a complete sign.
GLOBAL_REPLACE = [('ोंे', 'ों'), ('ोे', 'ो'), ('ेे', 'े'), ('ंे', 'ें'), ('ैे', 'ै')]

PAPERS = [
    {
        'id': 'uptet-2019-primary',
        'pkg': 'u19', 'qprefix': 'uptet19', 'year': 2019, 'exam': EXAM19,
        'title': {'en': 'UPTET 2019 · Primary level (Classes I–V) · Paper I',
                  'hi': 'UPTET 2019 · प्राथमिक स्तर (कक्षा 1–5) · प्रथम प्रश्न-पत्र'},
        'paper_code': 'UPTET-2019-P1',
        'level': 'primary',
        'sections': ['p_cdp', 'p_hin', 'p_eng', 'p_math', 'p_evs'],
        'what': 'Primary level paper (Classes I–V), with English as Language II',
    },
    {
        'id': 'uptet-2019-junior-maths-science',
        'pkg': 'u19', 'qprefix': 'uptet19', 'year': 2019, 'exam': EXAM19,
        'title': {'en': 'UPTET 2019 · Junior level (Classes VI–VIII) · Maths & Science',
                  'hi': 'UPTET 2019 · उच्च प्राथमिक स्तर (कक्षा 6–8) · गणित एवं विज्ञान'},
        'paper_code': 'UPTET-2019-P2-MS',
        'level': 'junior',
        'sections': ['j_cdp', 'j_hin', 'j_eng', 'j_math', 'j_sci'],
        'what': 'Junior level paper (Classes VI–VIII), with English as Language II and the Mathematics & Science option',
    },
    {
        'id': 'uptet-2019-junior-social-studies',
        'pkg': 'u19', 'qprefix': 'uptet19', 'year': 2019, 'exam': EXAM19,
        'title': {'en': 'UPTET 2019 · Junior level (Classes VI–VIII) · Social Studies',
                  'hi': 'UPTET 2019 · उच्च प्राथमिक स्तर (कक्षा 6–8) · सामाजिक अध्ययन'},
        'paper_code': 'UPTET-2019-P2-SST',
        'level': 'junior',
        'sections': ['j_cdp', 'j_hin', 'j_eng', 'j_sst'],
        'what': 'Junior level paper (Classes VI–VIII), with English as Language II and the Social Studies option',
    },
]

PAPERS += [
    {
        'id': 'uptet-2021-junior-social-studies',
        'pkg': 'u21', 'qprefix': 'uptet21', 'year': 2021, 'exam': EXAM21,
        'title': {'en': 'UPTET 2021 · Junior level (Classes VI–VIII) · Social Studies',
                  'hi': 'UPTET 2021 · उच्च प्राथमिक स्तर (कक्षा 6–8) · सामाजिक अध्ययन'},
        'paper_code': 'UPTET-2021-P2-SST',
        'level': 'junior',
        'sections': ['j_cdp', 'j_hin', 'j_eng', 'j_sst'],
        'what': 'Junior level paper (Classes VI–VIII), with English as Language II and the Social Studies option',
    },
    {
        'id': 'uptet-2021-primary-cancelled',
        'pkg': 'u21', 'qprefix': 'uptet21', 'year': 2021, 'exam': EXAM21P,
        'title': {'en': 'UPTET 2021 · Primary level (Classes I–V) · cancelled exam of 28 Nov 2021',
                  'hi': 'UPTET 2021 · प्राथमिक स्तर (कक्षा 1–5) · 28 नवम्बर 2021 की निरस्त परीक्षा'},
        'paper_code': 'UPTET-2021-P1-CANCELLED',
        'level': 'primary',
        'sections': ['p_cdp', 'p_hin', 'p_eng', 'p_math', 'p_evs'],
        'what': 'Primary level paper (Classes I–V), with English as Language II',
    },
    {
        'id': 'uptet-2018-primary',
        'pkg': 'u18', 'qprefix': 'uptet18', 'year': 2018, 'exam': EXAM18,
        'title': {'en': 'UPTET 2018 · Primary level (Classes I–V) · Paper I',
                  'hi': 'UPTET 2018 · प्राथमिक स्तर (कक्षा 1–5) · प्रथम प्रश्न-पत्र'},
        'paper_code': 'UPTET-2018-P1',
        'level': 'primary',
        'sections': ['p_cdp', 'p_hin', 'p_eng', 'p_math', 'p_evs'],
        'what': 'Primary level paper (Classes I–V), with English as Language II. The solved paper prints most '
                'questions in Hindi only',
    },
    {
        'id': 'uptet-2018-junior-social-studies',
        'pkg': 'u18', 'qprefix': 'uptet18', 'year': 2018, 'exam': EXAM18,
        'title': {'en': 'UPTET 2018 · Junior level (Classes VI–VIII) · Social Studies',
                  'hi': 'UPTET 2018 · उच्च प्राथमिक स्तर (कक्षा 6–8) · सामाजिक अध्ययन'},
        'paper_code': 'UPTET-2018-P2-SST',
        'level': 'junior',
        'sections': ['j_cdp', 'j_hin', 'j_eng', 'j_sst'],
        'what': 'Junior level paper (Classes VI–VIII), with English as Language II and the Social Studies option. '
                'The solved paper prints most questions in Hindi only',
    },
]

SUBJECTS = [
    ('cdp', None, []),
    ('hin', 'hi', [('hin.sahitya', 'Hindi literature', 'हिन्दी साहित्य'),
                   ('hin.gadyansh', 'Unseen passages', 'अपठित गद्यांश एवं पद्यांश'),
                   ('hin.shikshan', 'Teaching Hindi', 'हिन्दी शिक्षण')]),
    ('eng', 'en', [('eng.comprehension', 'Reading comprehension', 'अपठित गद्यांश एवं कविता'),
                   ('eng.pedagogy', 'Teaching English', 'अंग्रेज़ी शिक्षण')]),
    ('math', None, [('math.algebra', 'Algebra', 'बीजगणित')]),
    ('evs', None, []),
    ('sci', None, [('sci.physics', 'Force, motion, energy and electricity', 'बल, गति, ऊर्जा एवं विद्युत'),
                   ('sci.chemistry', 'Materials and chemical changes', 'पदार्थ एवं रासायनिक परिवर्तन'),
                   ('sci.biology', 'Living world and health', 'सजीव जगत एवं स्वास्थ्य'),
                   ('sci.pedagogy', 'Teaching science', 'विज्ञान शिक्षण')]),
    ('sst', None, [('sst.history', 'History', 'इतिहास'),
                   ('sst.geography', 'Geography', 'भूगोल'),
                   ('sst.civics', 'Civics and governance', 'नागरिक शास्त्र एवं शासन'),
                   ('sst.other', 'Physical education, agriculture, home science and music',
                    'शारीरिक शिक्षा, कृषि, गृह विज्ञान एवं संगीत'),
                   ('sst.pedagogy', 'Teaching social studies', 'सामाजिक अध्ययन शिक्षण')]),
]
SUBJECT_NAMES = {'sci': ('Science', 'विज्ञान'), 'sst': ('Social Studies', 'सामाजिक अध्ययन')}


def answer_keys(pdf):
    """{('main' | 'english' | 'sanskrit', n): 'a'..'d' or None when no single option is accepted}."""
    doc = pymupdf.open(pdf)
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
            keys[(section, int(n))] = a if a in 'abcd' else None
    return keys


def load(name):
    qs = json.load(open(f'{data_dir}/{name}.q.json', encoding='utf-8'))
    by_key, seen = {}, {}
    for q in qs:
        occ = seen[q['num']] = seen.get(q['num'], -1) + 1
        by_key[(q['num'], occ)] = q
    return by_key


def passage_text(lines, style, intro):
    body = lines[intro:]
    if style == 'verse':
        return '\n'.join(body)
    out = ''
    for line in body:
        out += line if out.endswith('-') or not out else ' ' + line
    return out


PASSAGE_PROMPT = {
    ('hi', 'prose'): 'नीचे दिए गए गद्यांश को पढ़कर प्रश्न का उत्तर दीजिए।',
    ('hi', 'verse'): 'नीचे दिए गए पद्यांश को पढ़कर प्रश्न का उत्तर दीजिए।',
    ('en', 'prose'): 'Read the passage below and answer the question.',
    ('en', 'verse'): 'Read the poem below and answer the question.',
}


def joined(*parts):
    return ' '.join(p for p in parts if p) or None


def build_section(mod, sources, keys, problems):
    # Sections the solved paper prints only in Hindi are built like the Hindi language section.
    lang = 'hi' if getattr(mod, 'HINDI_ONLY', False) else LANG.get(mod.SUBJECT)
    src = sources[mod.SOURCE]
    key_section = 'english' if mod.SUBJECT == 'eng' else 'main'
    topic_of = {n: t for t, ns in mod.TOPICS.items() for n in ns}
    passages = {}
    for after, (style, targets, intro, *override) in getattr(mod, 'PASSAGES', {}).items():
        lines = src[(after, 0)]['passage_after']
        assert lines or override, f'{mod.__name__}: no passage after {after}'
        for t in targets:
            passages[t] = (style, override[0] if override else passage_text(lines, style, intro))
    replace = getattr(mod, 'REPLACE', [])
    out = []
    for n in range(mod.RANGE[0], mod.RANGE[1] + 1):
        if n in mod.SKIP:
            continue
        q = src[(n, 0)]
        fix = mod.FIX.get(n, {})
        en, hi = fix.get('en', q['en']), fix.get('hi', q['hi'])
        options = [(o['en'], o['hi']) for o in q['options']]
        for i, letter in enumerate('abcd'):
            if letter in fix.get('options', {}):
                fe, fh = fix['options'][letter]
                options[i] = (fe if fe is not None else options[i][0], fh if fh is not None else options[i][1])
        if 'match' in fix:
            labels = fix.get('match_labels', ['A', 'B', 'C', 'D'])
            options = [(t, t) for t in (', '.join(f'{l}–{v}' for l, v in zip(labels, code.split()))
                                        for code in fix['match'])]
        if lang == 'hi':
            if 'hi' not in fix:
                hi = joined(en, hi)
            en, options = None, [(None, joined(e, h)) for e, h in options]
        elif lang == 'en':
            if hi:
                problems.append(f'{mod.__name__} {n}: Hindi text in an English question: {hi}')
            hi, options = None, [(e, None) for e, _ in options]
        else:
            options = [(e, h if h is not None else (e if e and not re.search('[a-z]{4,}|[A-Z][a-z]{3,}', e) else None))
                       for e, h in options]
        if n in passages:
            style, body = passages[n]
            if lang == 'hi':
                hi = f"{PASSAGE_PROMPT[('hi', style)]}\n\n{body}\n\n{hi}"
            else:
                en = f"{PASSAGE_PROMPT[('en', style)]}\n\n{body}\n\n{en}"

        def fixtext(t):
            if t is None:
                return None
            for a, b in GLOBAL_REPLACE + replace:
                t = t.replace(a, b)
            return t

        en, hi = fixtext(en), fixtext(hi)
        options = [(fixtext(e), fixtext(h)) for e, h in options]
        answer = fix.get('answer', keys[(key_section, n)])
        assert answer, f'{mod.__name__} {n}: no single answer in the key; add it to SKIP'
        exp_en, exp_hi = mod.EXPLAIN[n]
        topic = topic_of.get(n)
        assert topic, f'{mod.__name__} {n}: no topic'

        def text(e, h):
            d = {}
            if e is not None and lang != 'hi':
                d['en'] = e
            if h is not None and lang != 'en':
                d['hi'] = h
            return d

        question = {
            'num': n,
            'subject_id': mod.SUBJECT,
            'topic_id': topic,
            'text': text(en, hi),
            'options': [{'id': L, 'text': text(e, h)} for L, (e, h) in zip('ABCD', options)],
            'correct_option_id': answer.upper(),
            'explanation': text(exp_en, exp_hi),
        }
        check(mod.__name__, question, lang, problems)
        out.append(question)
    missing = set(mod.EXPLAIN) - {q['num'] for q in out}
    if missing:
        problems.append(f'{mod.__name__}: explanations for skipped/unknown questions {sorted(missing)}')
    return out


SUSPICIOUS = re.compile(r'Page \d|YCT|⟨|[\x00-\x08]|\s{3,}|\^|(?<![A-Za-z])_|□|^None$|/\s*$|^\s*/')


def check(name, q, lang, problems):
    n = q['num']
    fields = [('text', q['text'])] + [(f'option {o["id"]}', o['text']) for o in q['options']] + \
             [('explanation', q['explanation'])]
    for label, t in fields:
        for l in (['hi'] if lang == 'hi' else ['en'] if lang == 'en' else ['en', 'hi']):
            if not t.get(l):
                problems.append(f'{name} {n}: {label} missing {l}')
        for l, s in t.items():
            if SUSPICIOUS.search(s):
                problems.append(f'{name} {n}: {label} [{l}] looks odd: {s[:120]!r}')
            if l == 'hi' and lang is None and label != 'explanation' and re.search('[A-Za-z]{4,}', s) \
                    and not re.search('DNA|RNA|LCM|HCF', s):
                problems.append(f'{name} {n}: {label} [hi] has Latin text: {s[:100]!r}')
    if len({json.dumps(o['text'], ensure_ascii=False) for o in q['options']}) < 4:
        problems.append(f'{name} {n}: duplicate options')


class Lazy(dict):
    def __init__(self, make):
        super().__init__()
        self.make = make

    def __missing__(self, name):
        self[name] = self.make(name)
        return self[name]


def main():
    sources = Lazy(load)
    keys = Lazy(lambda name: answer_keys(f'{data_dir}/{name}.pdf'))
    problems = []
    built = {}
    papers = []
    for paper in PAPERS:
        try:
            mods = [importlib.import_module(f"{paper['pkg']}.{sec}") for sec in paper['sections']]
        except ModuleNotFoundError as e:
            print(f"skipping {paper['id']}: {e}")
            continue
        papers.append(paper)
        for sec, mod in zip(paper['sections'], mods):
            key = (paper['pkg'], sec)
            if key not in built:
                built[key] = (mod, build_section(mod, sources, keys[mod.SOURCE], problems), paper)

    pack = json.load(open(pack_path, encoding='utf-8'))
    pack['papers'] = [p for p in pack['papers'] if not p['id'].startswith('uptet-')]
    pack['questions'] = [q for q in pack['questions'] if not q['id'].startswith('q-uptet')]

    # Subjects in exam order, with the new subjects and topics.
    by_id = {s['id']: s for s in pack['subjects']}
    subjects = []
    for sid, language, new_topics in SUBJECTS:
        s = by_id.pop(sid, None) or {'id': sid, 'name': dict(zip(('en', 'hi'), SUBJECT_NAMES[sid])), 'topics': []}
        topics = s['topics'] + [{'id': t, 'name': {'en': e, 'hi': h}} for t, e, h in new_topics
                                if t not in {x['id'] for x in s['topics']}]
        subjects.append({'id': sid, 'name': s['name'], **({'language': language} if language else {}), 'topics': topics})
    subjects += by_id.values()
    pack['subjects'] = subjects

    for p in pack['papers']:
        if p['id'].startswith('ctet-'):
            p['exam'], p['level'] = 'ctet', 'primary'

    questions, new_papers = [], []
    ids_of = {}
    for key, (mod, qs, first_paper) in built.items():
        ids = []
        for q in qs:
            n = q.pop('num')
            qid = f"q-{first_paper['qprefix']}-{mod.ID_PREFIX}-{n:03d}"
            q_out = {'id': qid, **q,
                     'source': f"{first_paper['exam']}. {mod.PAPER_LABEL}, question {n}. Answer as given in the solved "
                               f"paper's key, still to be checked against the official final key. Explanation written "
                               f"by UPTET Saathi.",
                     'verification_status': 'pending_review'}
            questions.append(q_out)
            ids.append(qid)
        ids_of[key] = ids
    for paper in papers:
        secs = [(paper['pkg'], sec) for sec in paper['sections']]
        ids = [i for key in secs for i in ids_of[key]]
        skipped = sorted({f'{n}' for key in secs for n in built[key][0].SKIP}, key=int)
        new_papers.append({
            'id': paper['id'],
            'title': paper['title'],
            'year': paper['year'],
            'paper_code': paper['paper_code'],
            'exam': 'uptet',
            'level': paper['level'],
            'is_official_pyq': True,
            'distribution_cleared': False,
            'duration_minutes': 150,
            'marking': {'correct': 1, 'incorrect': 0, 'unanswered': 0},
            'pdf_asset': None,
            'source': f'{paper["exam"]}: {paper["what"]}. {SOLVED_PAPER} '
                      + (f'Question{"s" if len(skipped) > 1 else ""} {", ".join(skipped)} '
                         f'{"are" if len(skipped) > 1 else "is"} left out (no single accepted answer, a figure is '
                         f'needed, or the printed options are faulty). ' if skipped else '')
                      + paper.get('note', '') + 'Explanations are by UPTET Saathi.',
            'question_count': len(ids),
            'question_ids': ids,
        })

    # Keep each paper's keys in a readable order.
    order = ['id', 'title', 'year', 'paper_code', 'exam', 'level', 'is_official_pyq', 'distribution_cleared',
             'duration_minutes', 'marking', 'pdf_asset', 'source', 'question_count', 'question_ids']
    new_papers.sort(key=lambda p: -p['year'])  # newest first; stable within a year
    pack['papers'] = [{k: p[k] for k in order if k in p} for p in new_papers + pack['papers']]
    pack['questions'] += questions
    pack['content_version'] = '2026.10.28-uptet.2'

    open(pack_path, 'w', encoding='utf-8', newline='\n').write(dump(pack) + '\n')
    for p in new_papers:
        print(f"{p['id']}: {p['question_count']} questions")
    print(len(problems), 'problems')
    for line in problems:
        print(' -', line)
    if review_path:
        with open(review_path, 'w', encoding='utf-8') as f:
            for q in questions:
                f.write(f"\n{q['id']} [{q['topic_id']}] answer {q['correct_option_id']}\n")
                for l, t in q['text'].items():
                    f.write(f'  {l}: {t}\n')
                for o in q['options']:
                    f.write(f"  {o['id']}) {' || '.join(o['text'].values())}\n")


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
