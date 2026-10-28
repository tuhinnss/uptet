"""UPTET 2019 Primary, Part IV (Q91–120): Mathematics."""

SOURCE = 'primary'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (91, 120)
SUBJECT = 'math'

TOPICS = {
    'math.numbers': [92, 93, 96, 97, 98, 103, 104, 106, 108, 109, 110, 112, 113, 114, 115, 119, 120],
    'math.geometry': [91, 94, 95, 101, 102, 107, 111, 116],
    'math.measurement': [100, 105, 117, 118],
}

SKIP = {99: 'needs the figure'}


def opts(values):
    return {o: (v, v) for o, v in zip('abcd', values)}


FIX = {
    91: {'options': {o: (f'{v} m²', f'{v} मी²') for o, v in zip('abcd', [120, 132, 289, 112])}},
    92: {
        'en': 'On simplifying {(2⁻¹)}⁻¹, the number obtained is:\nA. Prime number\nB. Even number\nC. Multiple of 2\nD. Odd number',
        'hi': '{(2⁻¹)}⁻¹ के सरलीकरण से प्राप्त संख्या होगी–\nA. अभाज्य संख्या\nB. सम संख्या\nC. 2 का गुणक\nD. विषम संख्या',
    },
    94: {
        'en': 'The difference between the interior and exterior angles of a regular polygon is 60°. The number of sides in the polygon is:',
        'hi': 'एक बहुभुज के अन्तः एवं बाह्य कोणों का अंतर 60° है तो बहुभुज में भुजाओं की संख्या है–',
    },
    97: {'hi': 'Z का मान ज्ञात कीजिए यदि संख्या 417Z8, 9 से विभाज्य हो।'},
    98: {
        'en': 'If 2160 = 2ᵃ × 3ᵇ × 5ᶜ, then find the value of 3ᵃ × 2⁻ᵇ × 5⁻ᶜ.',
        'hi': 'यदि 2160 = 2ᵃ × 3ᵇ × 5ᶜ, तो 3ᵃ × 2⁻ᵇ × 5⁻ᶜ का मान ज्ञात कीजिए।',
        'options': opts(['0', '81/40', '37/39', '1/2']),
    },
    103: {'hi': '2018 में अमित का वेतन रुपये 1,26,500 है। वर्ष 2016 से उसका वेतन प्रतिवर्ष क्रमशः 10% व 15% बढ़कर 2018 '
                'के वेतन तक पहुँच गया। वर्ष 2016 में उसका वेतन कितना था?'},
    103: {'options': {o: (f'Rs. {v}', f'रु. {v}') for o, v in zip('abcd', ['1,15,000', '1,25,000', '1,00,000', '95,000'])}},
    104: {'options': opts(['27', '42', '54', '52'])},
    105: {'en': 'If the third Friday of a month is on the 16th, then what will be the date of the fourth (4th) Tuesday of '
                'the same month?'},
    106: {
        'en': 'If (a + b)/c = (b + c)/a = (c + a)/b = K, then the value of K is:',
        'hi': 'यदि (a + b)/c = (b + c)/a = (c + a)/b = K हो, तो K का मान है–',
        'options': opts(['2', '1/2', '3/2', '1']),
    },
    108: {'options': opts(['1/9', '2/5', '1/3', '4/9'])},
    109: {
        'en': 'Simplify: (−9) − {(−8) + (24 ÷ (13 − 7))}',
        'hi': 'सरल कीजिए: (−9) − {(−8) + (24 ÷ (13 − 7))}',
        'options': {'a': ('−5', '−5'), 'b': ('−8', '−8'), 'c': ('None of these', 'इनमें से कोई नहीं'), 'd': ('5', '5')},
    },
    110: {'hi': "यदि म.स. (a, 8) = 4 और ल.स. (a, 8) = 24 हो, तो 'a' का मान है–"},
    112: {'hi': 'किसी कमरे के 15 मी. 17 सेमी लम्बे और 9 मी. 2 सेमी चौड़े फर्श पर लगाई जा सकने वाली वर्गाकार टाइलों की '
                'न्यूनतम संख्या कितनी है?'},
    113: {'en': 'The unit digit of the product (2153)¹⁶⁷ is', 'hi': 'गुणनफल (2153)¹⁶⁷ में इकाई का अंक होगा–'},
    114: {
        'en': 'If the numerator of a fraction is increased by 20% and its denominator by 25%, the fraction becomes 3/5. '
              'The original fraction is:',
        'hi': 'यदि एक भिन्न के अंश को 20% और उसके हर को 25% बढ़ा दिया जाए, तो भिन्न 3/5 हो जाता है, तो मूल भिन्न है–',
        'options': opts(['5/8', '8/5', '8/3', '3/8']),
    },
    115: {
        'en': 'The numbers divisible by 8 are:\ni. 5240  ii. 5220  iii. 97128  iv. 97124',
        'hi': '8 से भाज्य होने वाली संख्यायें हैं–\ni. 5240  ii. 5220  iii. 97128  iv. 97124',
        'options': {'a': ('ii and iii', 'ii और iii'), 'b': ('i, iii and iv', 'i, iii और iv'),
                    'c': ('i and iii', 'i और iii'), 'd': ('i and ii', 'i और ii')},
    },
    116: {'en': 'How many vertices are there in a triangular prism?'},
    117: {
        'en': 'What will be the loss percentage if bananas are bought at 6 for ₹10 and sold at 4 for ₹6?',
        'hi': '₹10 के 6 की दर से केले खरीदकर ₹6 में 4 की दर से बेचने पर कितने प्रतिशत हानि होगी?',
    },
    118: {
        'en': 'Which options correctly fill the blank? 1 gram = ............ kilogram\nA. 1/1000 kg\nB. 10⁻³ kg\nC. 0.0001 kg\nD. 1000 kg',
        'hi': 'रिक्त स्थान के लिए कौन–कौन से विकल्प सही हैं? 1 ग्राम = ............ किग्रा.\nA. 1/1000 किग्रा.\nB. 10⁻³ किग्रा.\n'
              'C. 0.0001 किग्रा.\nD. 1000 किग्रा.',
    },
    119: {
        'en': '(0.01)² written as a percentage is:\nA. 0.01%\nB. 1/100\nC. 1%\nD. (1/100)%',
        'hi': '(0.01)² को प्रतिशत के रूप में लिखने पर–\nA. 0.01%\nB. 1/100\nC. 1%\nD. (1/100)%',
    },
    120: {'options': opts(['31/36', '5/9', '9/5', '5/36'])},
}

EXPLAIN = {
    91: ('Let the sides be l and b. Perimeter 46 m gives l + b = 23, and the diagonal gives l² + b² = 17² = 289. Then '
         '2lb = (l + b)² − (l² + b²) = 529 − 289 = 240, so the area lb = 120 m² (the sides are 15 m and 8 m).',
         'माना भुजाएँ l और b हैं। परिमाप 46 मी से l + b = 23, और विकर्ण से l² + b² = 17² = 289। तब 2lb = (l + b)² − (l² + b²) '
         '= 529 − 289 = 240, अतः क्षेत्रफल lb = 120 मी² (भुजाएँ 15 मी और 8 मी)।'),
    92: ('(2⁻¹)⁻¹ = 2. The number 2 is prime, even and a multiple of 2, but not odd, so A, B and C are true.',
         '(2⁻¹)⁻¹ = 2। संख्या 2 अभाज्य है, सम है और 2 का गुणक है, पर विषम नहीं है; अतः A, B और C सही हैं।'),
    93: ('A composite number can be odd, for example 9 or 15. The smallest prime is 2 (not 1), 2 is an even prime, and '
         '2 + 3 = 5 but 3 + 5 = 8 is not prime.',
         'भाज्य संख्या विषम हो सकती है, जैसे 9 या 15। सबसे छोटी अभाज्य संख्या 2 है (1 नहीं), 2 एक सम अभाज्य संख्या है, और '
         'दो अभाज्य संख्याओं का योग सदैव अभाज्य नहीं होता (3 + 5 = 8)।'),
    94: ('Interior + exterior = 180° and interior − exterior = 60°, so the exterior angle is 60°. Number of sides = '
         '360° ÷ 60° = 6.',
         'अन्तः कोण + बाह्य कोण = 180° और अंतर 60° है, अतः बाह्य कोण = 60°। भुजाओं की संख्या = 360° ÷ 60° = 6।'),
    95: ('A straight line extends endlessly in both directions, so it contains infinitely many points.',
         'सरल रेखा दोनों ओर अनन्त तक फैली होती है, इसलिए उस पर असंख्य (अनन्त) बिन्दु होते हैं।'),
    96: ('For an even number 2m, (2m, m² − 1, m² + 1) is a Pythagorean triplet. With 2m = 8, m = 4: (8, 15, 17). '
         'Check: 8² + 15² = 64 + 225 = 289 = 17².',
         'सम संख्या 2m के लिए (2m, m² − 1, m² + 1) पाइथागोरस त्रिक होता है। 2m = 8, m = 4 लेने पर (8, 15, 17)। '
         'जाँच: 8² + 15² = 64 + 225 = 289 = 17²।'),
    97: ('A number is divisible by 9 when its digit sum is. 4 + 1 + 7 + Z + 8 = 20 + Z, and the next multiple of 9 is 27, '
         'so Z = 7.',
         'कोई संख्या 9 से तभी विभाज्य है जब उसके अंकों का योग 9 से विभाज्य हो। 4 + 1 + 7 + Z + 8 = 20 + Z; 9 का अगला गुणज '
         '27 है, अतः Z = 7।'),
    98: ('2160 = 2⁴ × 3³ × 5, so a = 4, b = 3, c = 1. Then 3⁴ × 2⁻³ × 5⁻¹ = 81/(8 × 5) = 81/40.',
         '2160 = 2⁴ × 3³ × 5, अतः a = 4, b = 3, c = 1। तब 3⁴ × 2⁻³ × 5⁻¹ = 81/(8 × 5) = 81/40।'),
    100: ('The mode can be located graphically from a histogram: the tallest bar is joined to the adjacent bars by '
          'crossing lines, and the point where they meet gives the mode. Ogives give the median.',
          'बहुलक को आयत चित्र (हिस्टोग्राम) से आलेखीय रूप में ज्ञात किया जाता है: सबसे ऊँचे आयत के कोनों को पास के आयतों से '
          'मिलाने वाली रेखाओं का कटान बिन्दु बहुलक देता है। संचयी बारम्बारता वक्र (ओजाइव) से माध्यिका मिलती है।'),
    101: ('New length = 1.6 l. To keep the area the same, the width must become b/1.6 = 0.625 b, a decrease of 37.5%.',
          'नई लम्बाई = 1.6 l। क्षेत्रफल वही रखने के लिए चौड़ाई b/1.6 = 0.625 b होनी चाहिए, अर्थात् 37.5% की कमी।'),
    102: ('A cube has 12 edges, so a³ = 12a, giving a² = 12. Total surface area = 6a² = 72 square units.',
          'घन में 12 किनारे होते हैं, अतः a³ = 12a, जिससे a² = 12। सम्पूर्ण पृष्ठीय क्षेत्रफल = 6a² = 72 वर्ग इकाई।'),
    103: ('Salary in 2016 = 126500 ÷ (1.10 × 1.15) = 126500 ÷ 1.265 = ₹1,00,000.',
          '2016 का वेतन = 126500 ÷ (1.10 × 1.15) = 126500 ÷ 1.265 = ₹1,00,000।'),
    104: ('Product of two numbers = HCF × LCM = 6 × 432 = 2592. Other number = 2592 ÷ 48 = 54.',
          'दो संख्याओं का गुणनफल = म.स. × ल.स. = 6 × 432 = 2592। दूसरी संख्या = 2592 ÷ 48 = 54।'),
    105: ('If the third Friday is the 16th, the Fridays are 2, 9, 16, 23 and 30. Tuesday comes 4 days after Friday, so '
          'the Tuesdays are 6, 13, 20 and 27, and the fourth Tuesday is the 27th.',
          'तीसरा शुक्रवार 16 तारीख है, तो शुक्रवार 2, 9, 16, 23 और 30 तारीख को हैं। मंगलवार 6, 13, 20 और 27 तारीख को '
          'पड़ेंगे, अतः चौथा मंगलवार 27 तारीख को होगा।'),
    106: ('Add the numerators and the denominators: K = 2(a + b + c)/(a + b + c) = 2 (when a + b + c ≠ 0).',
          'अंशों और हरों को जोड़ने पर K = 2(a + b + c)/(a + b + c) = 2 (जब a + b + c ≠ 0)।'),
    107: ('Three lengths form a triangle only if the sum of the two shorter sides is greater than the longest. Only '
          '4.2, 5.9, 8.1 works (10.1 > 8.1); every set with 1.2 cm fails. So one triangle.',
          'तीन माप तभी त्रिभुज बनाते हैं जब दो छोटी भुजाओं का योग सबसे बड़ी भुजा से अधिक हो। केवल 4.2, 5.9, 8.1 (10.1 > 8.1) '
          'से त्रिभुज बनता है; 1.2 सेमी वाला हर समूह असफल है। अतः एक त्रिभुज।'),
    108: ('Let the numerator be x; the denominator is 2x + 1. (x + 2)/(2x + 1 − 3) = 1 gives x + 2 = 2x − 2, so x = 4 '
          'and the fraction is 4/9.',
          'माना अंश x है; हर 2x + 1 है। (x + 2)/(2x + 1 − 3) = 1 से x + 2 = 2x − 2, अतः x = 4 और भिन्न 4/9 है।'),
    109: ('13 − 7 = 6 and 24 ÷ 6 = 4. Then (−8) + 4 = −4, and (−9) − (−4) = −5.',
          '13 − 7 = 6 और 24 ÷ 6 = 4। तब (−8) + 4 = −4, और (−9) − (−4) = −5।'),
    110: ('HCF × LCM = product of the numbers: 4 × 24 = 8a, so a = 12.',
          'म.स. × ल.स. = संख्याओं का गुणनफल: 4 × 24 = 8a, अतः a = 12।'),
    111: ('New volume = 0.9 × 0.8 × 1.05 = 0.756 of the original, so the volume decreases by 24.4%.',
          'नया आयतन = 0.9 × 0.8 × 1.05 = मूल का 0.756, अतः आयतन में 24.4% की कमी होती है।'),
    112: ('1517 cm = 37 × 41 and 902 cm = 22 × 41, so the largest square tile has side HCF = 41 cm. Tiles needed = '
          '37 × 22 = 814.',
          '1517 सेमी = 37 × 41 और 902 सेमी = 22 × 41, अतः सबसे बड़ी वर्गाकार टाइल की भुजा म.स. = 41 सेमी। टाइलों की संख्या '
          '= 37 × 22 = 814।'),
    113: ('The unit digit depends on 3¹⁶⁷. Powers of 3 end in 3, 9, 7, 1 in a cycle of 4. 167 = 4 × 41 + 3, so the unit '
          'digit is the third in the cycle: 7.',
          'इकाई का अंक 3¹⁶⁷ पर निर्भर है। 3 की घातों के इकाई अंक 3, 9, 7, 1 के चक्र में आते हैं। 167 = 4 × 41 + 3, अतः '
          'इकाई का अंक चक्र का तीसरा, 7 है।'),
    114: ('(1.2x)/(1.25y) = 3/5, so x/y = (3/5) × (1.25/1.2) = (3/5) × (25/24) = 5/8.',
          '(1.2x)/(1.25y) = 3/5, अतः x/y = (3/5) × (1.25/1.2) = (3/5) × (25/24) = 5/8।'),
    115: ('A number is divisible by 8 if its last three digits are. 240 = 8 × 30 and 128 = 8 × 16, but 220 and 124 are '
          'not multiples of 8. So i and iii.',
          'कोई संख्या 8 से तभी विभाज्य है जब उसके अंतिम तीन अंक 8 से विभाज्य हों। 240 = 8 × 30 और 128 = 8 × 16, पर 220 और '
          '124, 8 के गुणज नहीं हैं। अतः i और iii।'),
    116: ('A triangular prism has two triangular faces, each with 3 vertices, so it has 6 vertices (and 9 edges, 5 faces).',
          'त्रिभुजाकार प्रिज्म के दो त्रिभुजाकार फलक होते हैं, प्रत्येक में 3 शीर्ष, अतः कुल 6 शीर्ष (9 किनारे, 5 फलक)।'),
    117: ('Cost price of one banana = 10/6 = ₹5/3; selling price = 6/4 = ₹3/2. Loss = 5/3 − 3/2 = 1/6. Loss % = '
          '(1/6) ÷ (5/3) × 100 = 10%.',
          'एक केले का क्रय मूल्य = 10/6 = ₹5/3; विक्रय मूल्य = 6/4 = ₹3/2। हानि = 5/3 − 3/2 = 1/6। हानि % = '
          '(1/6) ÷ (5/3) × 100 = 10%।'),
    118: ('1 kg = 1000 g, so 1 g = 1/1000 kg = 10⁻³ kg. A and B are correct; 0.0001 kg is 10⁻⁴ kg.',
          '1 किग्रा = 1000 ग्राम, अतः 1 ग्राम = 1/1000 किग्रा = 10⁻³ किग्रा। A और B सही हैं; 0.0001 किग्रा = 10⁻⁴ किग्रा है।'),
    119: ('(0.01)² = 0.0001 = 0.0001 × 100% = 0.01%, which is also (1/100)%. So A and D.',
          '(0.01)² = 0.0001 = 0.0001 × 100% = 0.01%, जो (1/100)% के बराबर है। अतः A और D।'),
    120: ('If the numbers are a and b with a − b = 5 and ab = 36, then 1/b − 1/a = (a − b)/ab = 5/36.',
          'यदि संख्याएँ a और b हैं, a − b = 5 और ab = 36, तो 1/b − 1/a = (a − b)/ab = 5/36।'),
}
