"""words in the Hindi font containing given characters, with their conversion.

Usage: glyph_words.py <chars> <lines.json>...
"""
import collections
import json
import sys

sys.path.insert(0, __file__.replace('\\', '/').rsplit('/', 1)[0])
from aps2uni import convert  # noqa: E402

sys.stdout.reconfigure(encoding='utf-8')
chars = sys.argv[1]
seen = collections.Counter()
for f in sys.argv[2:]:
    for _, _, _, segs in json.load(open(f, encoding='utf-8')):
        for k, t in segs:
            if k != 'hi':
                continue
            for w in t.split():
                for ch in chars:
                    if ch in w and seen[ch] < 6:
                        seen[ch] += 1
                        u = convert(w).replace('\x01', '¹').replace('\x02', '²')
                        print(repr(ch), f.split('.')[0], repr(w), '→', u)
