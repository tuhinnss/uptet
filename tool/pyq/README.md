# Previous-paper import scripts

Python scripts that turned the source PDFs into content-pack entries. The PDFs and
intermediate files are not committed (copyright); keep them in `tool/pyq/data/`,
which is git-ignored.

```
python -m venv .venv && .venv/Scripts/pip install -r tool/pyq/requirements.txt
```

Run every script with `python -I` and pass paths as arguments.

## UPTET 2017, 2018, 2019, 2021 (YCT solved papers)

The Hindi text uses the APS-DV-Priyanka legacy font; `aps2uni.py` converts it to Unicode.

1. `extract_lines.py <pdf> <name>.lines.json`: font-tagged text lines.
2. `parse_uptet.py <pdf> <name>.lines.json <last question page> <name>.q.json`: questions and options.
3. `show_q.py <name> <first> <last>` (inside the data directory): review parsed questions next to the book's key.
4. `build_uptet.py <data dir> assets/content/content_pack.json [review.txt]`: builds the papers and merges
   them into the pack, replacing what an earlier run added.

PDF names expected in the data directory: `primary`, `junior_ss`, `junior_ms` (2019),
`primary17`, `junior_ss17`, `primary18`, `junior_ss18`, `primary21`, `junior_ss21`.

Each section of a paper is a module in `u17/`, `u18/`, `u19/` or `u21/` (`p_` Primary, `j_` Junior) with:
`TOPICS`, `SKIP` (questions left out, with the reason), `PASSAGES`, `REPLACE` (text fixes),
`FIX` (whole-field overrides) and `EXPLAIN` (our own explanations, `(en, hi)`).

`aps_contexts.py` and `glyph_words.py` help find words the converter gets wrong.

### UPTET PDFs for the in-app viewer

The Drive folders 17, 18, 19 and 21 hold the YCT solved papers as `UPTET_<level>_<year>_Questions_AnswerKey_Explanations.pdf`.
Each has the questions, an answer key page, then YCT's explanations (from the first page with "Ans :" or
"Ans."). Only the pages before the explanations are bundled, saved as `assets/pdfs/<paper id>.pdf`:

```python
d = pymupdf.open(src)
i = next(i for i, p in enumerate(d) if re.search(r'Ans\s*[:.]', p.get_text()))
d.select(list(range(i)))
d.save(f'assets/pdfs/{paper_id}.pdf', garbage=4, deflate=True)
```

The 2021 Primary file is the cancelled sitting of 28 November 2021 (`uptet-2021-primary-cancelled`).

## UP Super TET 2019 (ATRE 2019, Booklet Series A)

Source: the retypeset Series A booklet with all four answer keys at the end
(`UP_Super_TET_2019_Question_Paper_Clean.pdf` in the project's Drive folder; save it as
`data/supertet/st19_clean.pdf`). Its Hindi is real Unicode, so PyMuPDF reads it directly; only doubled
vowel signs need collapsing. The scanned booklet in the same folder has a candidate's pen marks, and the
"2018" file there is not a Super TET paper (short-answer questions from a third-party site).

```
.venv/Scripts/python -I tool/pyq/build_supertet.py tool/pyq/data/supertet/st19_clean.pdf --dump parsed.txt
.venv/Scripts/python -I tool/pyq/build_supertet.py tool/pyq/data/supertet/st19_clean.pdf assets/content/content_pack.json [review.txt]
```

The first form writes the parsed questions before any fixes. Each section is a module in `st19/` with
`RANGE`, `LANGUAGE` (set for Hindi, Sanskrit and English), `TOPICS`, `SKIP`, `FIX` (whole-field or
per-option overrides, used for verses, fractions and powers the text layer flattens) and `EXPLAIN`
(`(en, hi)`). Copy the PDF to `assets/pdfs/supertet-2019.pdf` for the in-app viewer.

## CTET Feb 2026 Paper I, Set S

`extract_ctet.py` reads `pdftotext -layout` output of the booklet and the final key;
`build_ctet_feb26_p1s.py` merges the result into the pack.
