"""UPTET 2019 Junior, Part IV (1) (Q91–120): Mathematics."""

SOURCE = 'junior_ms'
ID_PREFIX = 'jms'
PAPER_LABEL = 'Junior level paper, Mathematics and Science option'
RANGE = (91, 120)
SUBJECT = 'math'

TOPICS = {
    'math.numbers': [92, 93, 97, 99, 108, 111, 113, 114, 116],
    'math.algebra': [95, 96, 100, 105, 107, 110, 112, 115, 117, 119],
    'math.geometry': [91, 94, 98, 101, 103, 106, 109],
    'math.measurement': [102, 120],
}

SKIP = {104: 'no option, as printed, is the correct answer (5m/4)', 118: 'two options are printed the same'}


def opts(values):
    return {o: (v, v) for o, v in zip('abcd', values)}


FIX = {
    91: {'hi': 'यदि त्रिभुज ABC के अन्तःवृत्त का केन्द्र O हो और ∠BOC = 110° हो, तो ∠BAC का मान होगा–',
         'en': 'If O is the centre of the incircle of a triangle ABC and ∠BOC = 110°, then the value of ∠BAC will be:'},
    92: {'hi': 'यदि किसी संख्या के 75% में 75 जोड़कर वही संख्या प्राप्त हो जाए, तो वह संख्या होगी–'},
    93: {'en': 'The greatest number among 2⁵⁰, 3⁴⁰, 4³⁰ and 5²⁰ is:', 'hi': '2⁵⁰, 3⁴⁰, 4³⁰ तथा 5²⁰ में सबसे बड़ी संख्या है–'},
    94: {'en': 'AB is a diameter of a circle and ABCD is a cyclic quadrilateral in it. If ∠ACD = 40°, then the measure of ∠BAD is:',
         'hi': 'AB एक वृत्त का व्यास है और ABCD उसके भीतर का चक्रीय चतुर्भुज है। यदि ∠ACD = 40° हो, तो ∠BAD का माप होगा–'},
    95: {'en': 'If 0 ≤ x ≤ 5 and 5 ≤ y ≤ 10, then the maximum value of (x/y) will be:',
         'hi': 'यदि 0 ≤ x ≤ 5 और 5 ≤ y ≤ 10 हो, तब (x/y) का अधिकतम मान होगा–',
         'options': opts(['2', '0', '1', '1/2'])},
    96: {'options': {'b': (None, 'इसका कोई हल नहीं है।')}},
    97: {'en': '(49)¹⁵ − 1 is completely divisible by which numbers?\ni. 50  ii. 48  iii. 29  iv. 8',
         'hi': '(49)¹⁵ − 1 किस संख्या से पूर्णतः विभाजित है?\ni. 50  ii. 48  iii. 29  iv. 8',
         'options': {'a': ('i and iii', 'i और iii'), 'b': ('i and ii', 'i और ii'),
                     'c': ('ii and iv', 'ii और iv'), 'd': ('iii and iv', 'iii और iv')}},
    98: {'en': 'The value of (cos 135° · sin 210° · cos 150°) / (sin 270° · cos 315°) is:',
         'hi': '(cos 135° · sin 210° · cos 150°) / (sin 270° · cos 315°) का मान होगा–',
         'options': opts(['√3', '√3/2', '1/√3', '√3/4'])},
    99: {'en': 'The product of two consecutive odd numbers is 6723. The square root of the smaller number is:'},
    100: {'en': 'If the highest common factor of x² + px − q and 5x² − 3px − 15q is (x − 3), then the values of p and q are:',
          'hi': 'यदि x² + px − q तथा 5x² − 3px − 15q का महत्तम समापवर्तक (x − 3) हो, तो p तथा q के मान होंगे–',
          'options': opts(['5/3, 4', '4, −3/5', '−5/3, 4', '−5/3, −4'])},
    101: {'options': opts(['√2 : 1 : √3', '√2 : √2 : 1', '√3 : √3 : 1', '1 : √3 : √3'])},
    103: {'en': 'If ΔABC is an isosceles triangle such that ∠ABC = 90°, then the true statement about ΔABC is:',
          'hi': 'यदि ΔABC एक समद्विबाहु त्रिभुज है जिसमें ∠ABC = 90° हो, तब ΔABC के बारे में सत्य कथन है–',
          'options': opts(['(BC)² + (AC)² = (AB)²', '(AC)² = 2(AB)²', '2(AC)² = (AB)²', '(AB)² + (AC)² = (BC)²'])},
    105: {'en': 'If x + y = 2z, then the value of x/(x − z) + z/(y − z) is:',
          'hi': 'यदि x + y = 2z है, तो x/(x − z) + z/(y − z) का मान होगा–'},
    109: {'options': opts(['27 : 64', '3 : 8', '3 : 4', '9 : 16'])},
    110: {'en': 'If x⁴ + 1/x⁴ = 14, then the value of x³ + 1/x³ is:\nA. 3√6\nB. 18/√6\nC. 9√(2/3)\nD. 3√2',
          'hi': 'यदि x⁴ + 1/x⁴ = 14 हो, तो x³ + 1/x³ का मान है–\nA. 3√6\nB. 18/√6\nC. 9√(2/3)\nD. 3√2'},
    111: {'options': opts(['942', '945', '630', '238'])},
    112: {'en': 'If x = (2 − √3)⁻¹, then the value of x³ − 2x² − 7x + 5 is:',
          'hi': 'यदि x = (2 − √3)⁻¹ हो, तब x³ − 2x² − 7x + 5 का मान है–'},
    114: {'options': opts(['16 : 5', '13 : 2', '15 : 4', '14 : 3'])},
    115: {'options': opts(['2/3', '1', '2', '1/2'])},
    116: {'options': opts(['7', '2', '3', '5'])},
    117: {'en': 'If (9/7)³ × (49/81)²ˣ⁻⁶ = (7/9)⁹, then the value of x is:',
          'hi': 'यदि (9/7)³ × (49/81)²ˣ⁻⁶ = (7/9)⁹ है, तो x का मान है–'},
    120: {'hi': 'एक मूलधन, साधारण ब्याज की दर से 10 वर्षों में अपने का दोगुना हो जाता है। ब्याज की दर ज्ञात कीजिए।'},
}

EXPLAIN = {
    91: ('For the incentre O, ∠BOC = 90° + ∠A/2. So 110° = 90° + ∠A/2, giving ∠A = 40°.',
         'अन्तःकेन्द्र O के लिए ∠BOC = 90° + ∠A/2। अतः 110° = 90° + ∠A/2, जिससे ∠A = 40°।'),
    92: ('0.75x + 75 = x, so 0.25x = 75 and x = 300.', '0.75x + 75 = x, अतः 0.25x = 75 और x = 300।'),
    93: ('Write each as a 10th power: 2⁵⁰ = 32¹⁰, 3⁴⁰ = 81¹⁰, 4³⁰ = 64¹⁰, 5²⁰ = 25¹⁰. The largest base is 81, so 3⁴⁰ is greatest.',
         'प्रत्येक को 10वीं घात में लिखें: 2⁵⁰ = 32¹⁰, 3⁴⁰ = 81¹⁰, 4³⁰ = 64¹⁰, 5²⁰ = 25¹⁰। सबसे बड़ा आधार 81 है, अतः 3⁴⁰ सबसे बड़ी है।'),
    94: ('∠ABD = ∠ACD = 40° (angles on the same arc AD). ∠ADB = 90° (angle in a semicircle). So ∠BAD = 180° − 90° − 40° = 50°.',
         '∠ABD = ∠ACD = 40° (एक ही चाप AD पर बने कोण)। ∠ADB = 90° (अर्धवृत्त का कोण)। अतः ∠BAD = 180° − 90° − 40° = 50°।'),
    95: ('x/y is largest when x is largest and y smallest: 5/5 = 1.', 'x/y सबसे बड़ा तब होगा जब x अधिकतम और y न्यूनतम हो: 5/5 = 1।'),
    96: ('y = 7x − 2 is a linear equation in two variables: every value of x gives a y, so it has infinitely many solutions.',
         'y = 7x − 2 दो चरों का रैखिक समीकरण है: x के हर मान के लिए y मिलता है, इसलिए इसके अनन्त हल हैं।'),
    97: ('aⁿ − 1 is always divisible by a − 1, so 49¹⁵ − 1 is divisible by 48, and hence by 8. Since 49 ≡ −1 (mod 50), '
         '49¹⁵ − 1 ≡ −2, so it is not divisible by 50. Answer: ii and iv.',
         'aⁿ − 1 सदैव a − 1 से विभाज्य है, अतः 49¹⁵ − 1, 48 से और इसलिए 8 से भी विभाज्य है। 49 ≡ −1 (mod 50) होने से 49¹⁵ − 1 ≡ −2, '
         'अतः यह 50 से विभाज्य नहीं है। उत्तर: ii और iv।'),
    98: ('cos 135° = −1/√2, sin 210° = −1/2, cos 150° = −√3/2, sin 270° = −1, cos 315° = 1/√2. Numerator = −√3/(4√2), '
         'denominator = −1/√2, so the value is √3/4.',
         'cos 135° = −1/√2, sin 210° = −1/2, cos 150° = −√3/2, sin 270° = −1, cos 315° = 1/√2। अंश = −√3/(4√2), हर = −1/√2, '
         'अतः मान √3/4 है।'),
    99: ('6723 = 81 × 83, and 81 and 83 are consecutive odd numbers. The square root of 81 is 9.',
         '6723 = 81 × 83, और 81 तथा 83 सतत विषम संख्याएँ हैं। 81 का वर्गमूल 9 है।'),
    100: ('x = 3 makes both expressions zero: 9 + 3p − q = 0 and 45 − 9p − 15q = 0. Putting q = 9 + 3p in the second gives '
          '−90 − 54p = 0, so p = −5/3 and q = 4.',
          'x = 3 पर दोनों व्यंजक शून्य होंगे: 9 + 3p − q = 0 और 45 − 9p − 15q = 0। दूसरे में q = 9 + 3p रखने पर −90 − 54p = 0, '
          'अतः p = −5/3 और q = 4।'),
    101: ('Same base radius r and height r (the hemisphere\'s height). Curved areas: cylinder 2πr², hemisphere 2πr², cone '
          'πr × √2 r = √2 πr². Ratio 2 : 2 : √2 = √2 : √2 : 1.',
          'आधार त्रिज्या r और ऊँचाई r (अर्धगोले की ऊँचाई) समान है। वक्र पृष्ठ: बेलन 2πr², अर्धगोला 2πr², शंकु πr × √2 r = √2 πr²। '
          'अनुपात 2 : 2 : √2 = √2 : √2 : 1।'),
    102: ('Selling at 15% gain and at 15% loss differs by 30% of the cost price. 30% of CP = ₹450, so CP = ₹1,500.',
          '15% लाभ और 15% हानि पर विक्रय मूल्यों का अंतर क्रय मूल्य का 30% है। CP का 30% = ₹450, अतः CP = ₹1,500।'),
    103: ('With ∠B = 90° and AB = BC, Pythagoras gives AC² = AB² + BC² = 2AB².',
          '∠B = 90° और AB = BC होने पर पाइथागोरस प्रमेय से AC² = AB² + BC² = 2AB²।'),
    105: ('x + y = 2z means y − z = −(x − z). So x/(x − z) + z/(y − z) = (x − z)/(x − z) = 1.',
          'x + y = 2z से y − z = −(x − z)। अतः x/(x − z) + z/(y − z) = (x − z)/(x − z) = 1।'),
    106: ('Surface area varies as r². With r × 1.5, the area becomes 2.25 times, an increase of 125%.',
          'पृष्ठीय क्षेत्रफल r² के अनुपात में बदलता है। r को 1.5 गुना करने पर क्षेत्रफल 2.25 गुना हो जाता है, अर्थात् 125% वृद्धि।'),
    107: ('The vertical line x = 1 and the horizontal line y = 1 meet at (1, 1).',
          'ऊर्ध्वाधर रेखा x = 1 और क्षैतिज रेखा y = 1 बिन्दु (1, 1) पर मिलती हैं।'),
    108: ('a + b = 2 × 5 = 10 and ab = 3² = 9, so the numbers are 9 and 1.',
          'a + b = 2 × 5 = 10 और ab = 3² = 9, अतः संख्याएँ 9 और 1 हैं।'),
    109: ('Volume ratio 27 : 64 means side ratio 3 : 4, so the surface areas are in the ratio 9 : 16.',
          'आयतनों का अनुपात 27 : 64 है, अतः भुजाओं का अनुपात 3 : 4 और पृष्ठीय क्षेत्रफलों का अनुपात 9 : 16 है।'),
    110: ('x⁴ + 1/x⁴ = 14 gives x² + 1/x² = 4, then x + 1/x = √6, so x³ + 1/x³ = (√6)³ − 3√6 = 3√6. Also 18/√6 = 3√6 and '
          '9√(2/3) = 3√6, so A, B and C are correct.',
          'x⁴ + 1/x⁴ = 14 से x² + 1/x² = 4, फिर x + 1/x = √6, अतः x³ + 1/x³ = (√6)³ − 3√6 = 3√6। साथ ही 18/√6 = 3√6 और '
          '9√(2/3) = 3√6, अतः A, B और C सही हैं।'),
    111: ('Let the birds be 3k, 7k and 5k. B₂ − B₁ = 4k must be a multiple of both 9 and 7, i.e. of 63, so the least k is '
          '63. Total = 15k = 945.',
          'माना चिड़ियाँ 3k, 7k और 5k हैं। B₂ − B₁ = 4k, 9 और 7 दोनों का अर्थात् 63 का गुणज होना चाहिए, अतः न्यूनतम k = 63। '
          'कुल = 15k = 945।'),
    112: ('x = 1/(2 − √3) = 2 + √3. Then x² = 7 + 4√3 and x³ = 26 + 15√3. So x³ − 2x² − 7x + 5 = 26 + 15√3 − 14 − 8√3 − 14 − '
          '7√3 + 5 = 3.',
          'x = 1/(2 − √3) = 2 + √3। तब x² = 7 + 4√3 और x³ = 26 + 15√3। अतः x³ − 2x² − 7x + 5 = 26 + 15√3 − 14 − 8√3 − 14 − '
          '7√3 + 5 = 3।'),
    113: ('10³A + A = 1001A, and 1001 = 7 × 11 × 13. For 1001A to be a perfect square, A must contain 7 × 11 × 13, so the '
          'smallest A is 1001, which has 4 digits.',
          '10³A + A = 1001A, और 1001 = 7 × 11 × 13। 1001A पूर्ण वर्ग होने के लिए A में 7 × 11 × 13 होना चाहिए, अतः न्यूनतम A = 1001, '
          'जिसमें 4 अंक हैं।'),
    114: ('Let the son be s years old; the father is 68 − s. 60 − s = 12(s − 8) gives s = 12, father 56. After 4 years: '
          '60 : 16 = 15 : 4.',
          'माना पुत्र की आयु s वर्ष है; पिता की 68 − s। 60 − s = 12(s − 8) से s = 12, पिता 56। 4 वर्ष बाद: 60 : 16 = 15 : 4।'),
    115: ('The equation is abx² − (a + b)²x + (a + b)² = 0. Sum of reciprocals = (α + β)/αβ = [(a + b)²/ab] ÷ [(a + b)²/ab] = 1.',
          'समीकरण abx² − (a + b)²x + (a + b)² = 0 है। व्युत्क्रमों का योग = (α + β)/αβ = [(a + b)²/ab] ÷ [(a + b)²/ab] = 1।'),
    116: ('m, m + 2 and m + 4 leave different remainders when divided by 3, so one of them is a multiple of 3. (They need '
          'not be even: 1 × 3 × 5 = 15.)',
          'm, m + 2 और m + 4 को 3 से भाग देने पर अलग-अलग शेषफल आते हैं, इसलिए इनमें से एक 3 का गुणज होगा। (ये सम हों, '
          'आवश्यक नहीं: 1 × 3 × 5 = 15।)'),
    117: ('(9/7)³ = (7/9)⁻³ and (49/81)²ˣ⁻⁶ = (7/9)⁴ˣ⁻¹². So −3 + 4x − 12 = 9, giving x = 6.',
          '(9/7)³ = (7/9)⁻³ और (49/81)²ˣ⁻⁶ = (7/9)⁴ˣ⁻¹²। अतः −3 + 4x − 12 = 9, जिससे x = 6।'),
    119: ('The product of the roots is c/a. If one root is the reciprocal of the other, the product is 1, so c = a.',
          'मूलों का गुणनफल c/a होता है। यदि एक मूल दूसरे का व्युत्क्रम है तो गुणनफल 1 होगा, अतः a = c।'),
    120: ('The money doubles, so the interest equals the principal: 100% in 10 years, i.e. 10% a year.',
          'मूलधन दोगुना होता है, यानी ब्याज मूलधन के बराबर है: 10 वर्षों में 100%, अर्थात् 10% प्रति वर्ष।'),
}
