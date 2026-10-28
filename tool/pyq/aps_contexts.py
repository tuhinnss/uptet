"""Example words that the APS converter cannot fully handle."""
import collections
import json
import re
import sys

sys.path.insert(0, sys.argv[1])
from aps2uni import convert

sys.stdout.reconfigure(encoding='utf-8')
words = collections.defaultdict(collections.Counter)
for f in sys.argv[2:]:
    for _, _, _, segs in json.load(open(f, encoding='utf-8')):
        for k, t in segs:
            if k != 'hi':
                continue
            for w in t.split():
                u = convert(w)
                bad = set(re.findall(r'⟨(.)⟩', u))
                bad |= {c for c in u if c in '\x01\x02' or c.isascii() and c.isalpha()}
                for c in bad:
                    words[repr(c)][w + ' → ' + u.replace('\x01', '¹').replace('\x02', '²')] += 1
for ch, c in sorted(words.items(), key=lambda x: -sum(x[1].values())):
    print(ch, sum(c.values()), ' | '.join(w for w, _ in c.most_common(8)))
