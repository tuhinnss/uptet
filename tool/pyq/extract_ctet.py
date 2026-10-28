"""pull English stems/options for Q1-90 out of a CTET booklet
(pdftotext -layout output) and pair them with the final answer key.

usage: python -I extract_ctet.py main.txt key.txt SET out.json
"""
import json
import re
import sys

main_path, key_path, set_letter, out_path = sys.argv[1:5]
lines = open(main_path, encoding="utf-8", errors="replace").read().splitlines()

# Answer key: block "Set :- S PAPER-I- MAIN" up to the next "Set :-".
key_lines = open(key_path, encoding="utf-8", errors="replace").read().splitlines()
key = {}
inside = False
for line in key_lines:
    if line.startswith("Set :-"):
        inside = re.match(rf"Set :- {set_letter} PAPER-I- MAIN", line) is not None
        continue
    if inside:
        for qno, ans in re.findall(r"\|\s*(\d{1,3})\s+([1-4A-FZ])\s", line):
            key[int(qno)] = ans

start = next(i for i, l in enumerate(lines) if "PART--I " in l or l.strip().startswith("PART--I /"))
end = next(i for i, l in enumerate(lines) if "PART--IV" in l)
body = lines[start:end]

skip = re.compile(r"(P\.T\.O\.|SPACE FOR ROUGH WORK|/P1\s+\d+|^\s*PART--|Direction :)")
blocks = {}
expected = 1
current = None
for line in body:
    if skip.search(line):
        continue
    m = re.match(r"^\s{0,8}(\d{1,3})\.\s+(.*)$", line)
    if m and int(m.group(1)) == expected:
        current = expected
        blocks[current] = [m.group(2)]
        expected += 1
        continue
    if current is not None:
        blocks[current].append(line)

opt_re = re.compile(r"\(([1-4])\)\s*(.*?)(?=\s{2,}\([1-4]\)|\s*$)")
out = []
for qno in range(1, 91):
    raw = blocks.get(qno, [])
    stem, options, stage = [], {}, "stem"
    for line in raw:
        if stage == "stem":
            if re.search(r"^\s*\(1\)", line):
                stage = "opts"
            else:
                if line.strip():
                    stem.append(line.strip())
                continue
        if stage == "opts":
            for n, text in opt_re.findall(line):
                options.setdefault(n, text.strip())
            if "4" in options:
                break
    out.append({
        "qno": qno,
        "stem": " / ".join(stem),
        "options": [options.get(n, "") for n in "1234"],
        "key": key.get(qno),
    })

json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
non_single = {q: a for q, a in key.items() if q <= 90 and a not in "1234"}
print("questions:", len(out), "| keys:", len([q for q in key if q <= 90]), "| multi/void keys:", non_single)
print("missing options:", [q["qno"] for q in out if not all(q["options"])])
