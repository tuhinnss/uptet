"""Converts text in the APS-DV-Priyanka legacy Devanagari encoding to Unicode.

The font draws most consonants as a half form plus the vertical bar "e", puts
the i-matra ("ef") before its consonant cluster and the reph after it, and
adds the hook that turns प into फ (and makes क) after any vowel signs.
"""
import re

HALANT = '्'
NUKTA = '़'

# Half forms: completed by a following "e".
HALF = {
    'k': 'क', 'h': 'प', 'm': 'स', 'l': 'त', 'c': 'म', 'v': 'न', 'Ù': 'य', 'J': 'व',
    'u': 'ल', 'i': 'ग', 'M': 'श', 'y': 'ब', 'p': 'ज', 'Û': 'च', 'O': 'ध', 'C': 'ण',
    'Ø': 'प्र', 'Y': 'भ', 'L': 'थ', 'K': 'ख', '<': 'ष', '#': 'क्ष', '$': 'त्र',
    '%': 'ज्ञ', 'ò': 'त्त', 'I': 'घ', '›': 'क्र', 'D': 'अ', 'ß': 'श्र', '«': 'ग्र',
    'Å': 'द्य', 'Ã': 'ञ्च', 'Œ': 'स्त्र', 'ë': 'श', '¢': 'ह्य', '¿': 'ङ्क', '§': 'श्च',
    'À': 'ञ्ज', 'ÿ': 'ह्म', '»': 'ज्र', 'œ': 'स्र', 'å': 'ह', 'Õ': 'श्व', '©': 'द्म',
    'V': 'न्न', 'P': 'झ', 'Ÿ': '्य',
}
# Complete letters (no bar).
FULL = {
    'n': 'ह', 'j': 'र', '[': 'ड', '"': 'ठ', 'Ú': 'छ', '{': 'ढ', 'š': 'ट', 'o': 'द',
    'É': 'द्व', 'æ': 'द्ध', 'ó': 'ट्ट', '°': 'ष्ट', '™': 'रू', '®': 'रु', 'õ': 'द्र',
    '‰': 'ष्ठ', 'ö': 'द्द', 'Á': 'ङ्ग', 'Â': 'दृ', 'Ü': 'ह्र', 'ñ': 'ड्ड', 'Ö': 'ह्न',
    'ù': 'हृ', '„': 'ष्ट', 'ª': 'ट्ठ', '*': 'ङ', 'F': 'इ', 'G': 'उ', 'T': 'ऊ', 'S': 'ए', 'è': 'ऋ',
}
SIGNS = {
    's': 'े', 'w': 'ै', 'W': 'ें', 'Q': 'ैं', 'g': 'ु', 't': 'ू', '=': 'ृ', '¸': 'ॄ',
    'b': 'ं', 'B': 'ँ', 'd': HALANT, '~': '।', '@': 'ॅ', '^': '्र', 'Ç': '्र', 'ü': '्र',
    'Ó': 'ऽ', '±': '+', '·': '=', '³': '%', 'Ò': 'ू', 'Ï': 'ु',
}
# Glyphs seen only in the 2018 and 2021 solved papers.
HALF.update({'H': 'प', '‹': 'क्ष', '_': 'ञ'})
SIGNS.update({'>': '्न'})
FULL.update({'Æ': 'द्भ', 'º': 'ड्ढ', 'û': 'द्य', 'ú': 'ट्ठ', '”': 'ङ्ग'})
HOOKED = {'k': 'क', 'h': 'फ', 'H': 'फ', 'ò': 'क्त', '›': 'क्र', 'ø': 'फ्र', 'Ø': 'फ्र'}
MARKS = 'sw=bWQ&B@gtÇd'


def _is_deva(ch):
    return 'ऀ' <= ch <= 'ॿ'


def convert(s, unknown=None):
    s = re.sub(rf'([{"".join(HOOKED)}])e([{MARKS}]*)â', lambda m: HOOKED[m[1]] + m[2], s)
    s = re.sub(r'([kh])eä', lambda m: HOOKED[m[1]] + HALANT, s)
    # Justified lines sometimes split a word before a vowel sign or reph.
    s = re.sub(r' +(?=[swWQrRfgt=bBX&a@x])', '', s)
    s = s.replace('FË', 'ईं').replace('F&', 'ई').replace('$e+', 'ऋ')
    out = []
    i = 0
    while i < len(s):
        ch = s[i]
        nxt = s[i + 1] if i + 1 < len(s) else ''
        if ch == 'e':
            if nxt and nxt in 'fq':
                out.append('\x01')  # i-matra, moved after its cluster below
                i += 2
                continue
            if nxt == 'E':
                out.append('\x03')  # i-matra with anusvara, moved likewise
                i += 2
                continue
            if nxt in ('|', '\\'):
                out.append('\x05' if nxt == '|' else '\x06')  # i-matra (+ anusvara) with a reph
                i += 2
                continue
            if nxt == 'r':
                out.append('ी'); i += 2; continue
            if nxt == 'R':
                out.append('ीं'); i += 2; continue
            if nxt == 'a':
                out.append('ी'); out.append(''); i += 2; continue
            if out and out[-1].endswith(HALANT) and out[-1] not in ('्र', HALANT):
                out[-1] = out[-1][:-1]
            else:
                out.append('ा')
        elif ch == 'Ì' and nxt in FULL:
            out.append(FULL[nxt] + NUKTA); i += 2; continue
        elif ch == ']':
            out.append('\x04')  # nukta typed before its consonant, moved after it below
        elif ch == 's' and nxt == 'a':
            out.append('ें'); i += 2; continue
        elif ch in HALF:
            out.append(HALF[ch] + HALANT)
        elif ch in FULL:
            out.append(FULL[ch])
        elif ch in SIGNS:
            out.append(SIGNS[ch])
        elif ch == '&':
            out.append('\x02')  # reph, moved before its cluster below
        elif ch == 'x':
            out.append('े'); out.append('')
        elif ch == 'X':
            out.append('ें'); out.append('\x02')
        elif ch == 'Ë':
            out.append('\x02'); out.append('ं')
        elif ch == ':':
            out.append('ः' if out and out[-1] and _is_deva(out[-1][-1]) else ':')
        elif _is_deva(ch) or ord(ch) < 128 or ch in '‘’“–—':
            out.append(ch)
        else:
            out.append('⟨' + ch + '⟩')
            if unknown is not None:
                unknown[ch] = unknown.get(ch, 0) + 1
        i += 1
    t = ''.join(out)
    t = t.replace('अा', 'आ')
    # Vowel signs typed as bar + e/ai sign.
    for a, b in [('ाें', 'ों'), ('ाैं', 'ौं'), ('ाे', 'ो'), ('ाै', 'ौ'), ('ाॅ', 'ॉ'),
                 ('आें', 'ओं'), ('आे', 'ओ'), ('आै', 'औ'), ('आॅ', 'ऑ'), ('एे', 'ऐ')]:
        t = t.replace(a, b)
    cons = '[क-हक़-य़]़?'
    cluster = f'(?:{cons}्)*{cons}'
    t = re.sub('\x04([क-ह])', r'\1' + NUKTA, t)
    t = re.sub('\x01(' + cluster + ')', r'\1' + 'ि', t)
    t = re.sub('\x03(' + cluster + ')', r'\1' + 'िं', t)
    t = re.sub('\x05(' + cluster + ')', 'र्' + r'\1' + 'ि', t)
    t = re.sub('\x06(' + cluster + ')', 'र्' + r'\1' + 'िं', t)
    # Reph goes before the cluster it follows, ahead of any vowel signs.
    t = re.sub('(' + cluster + ')([ा-ौँं]*)\x02', 'र्' + r'\1\2', t)
    # A ra-sign typed after the vowel sign (पे्र → प्रे), and anusvara before u/uu (यंु → युं).
    t = re.sub('([ा-ौ])्र', '्र' + r'\1', t)
    t = re.sub('([ंँ])([ा-ौ])', r'\2\1', t)
    # Doubled bars and अ + ai-sign from loosely kerned text.
    t = t.replace('ाा', 'ा').replace('अै', 'औ')
    return t
