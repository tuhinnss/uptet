"""Super TET 2019, Q81–100: Mathematics. Fractions and powers lose their layout in the text, so those
questions are written out in FIX."""

RANGE = (81, 100)
LANGUAGE = None

TOPICS = {
    'math.numbers': [84, 85, 86, 89, 90, 91, 92, 93, 94, 100],
    'math.algebra': [95, 96],
    'math.geometry': [82, 83, 87, 88, 97],
    'math.measurement': [98, 99],
}

SKIP = {
    81: 'b² + 8b ≥ 9b + 14 gives b² − b − 14 ≥ 0, whose bounds are not whole numbers, so the keyed answer '
        '(b ≥ 5 or b ≤ −4) does not follow from the printed question',
}


def same(*options):
    return {i: (o, o) for i, o in enumerate(options, 1)}


FIX = {
    82: {'hi': 'ABCD एक आयत है (AC उसका विकर्ण है)। यदि AB + AC = 5AD तथा AC − AD = 8 है, तो आयत ABCD का क्षेत्रफल है',
         'en': 'ABCD is a rectangle (AC is its diagonal). If AB + AC = 5AD and AC − AD = 8, then the area of the '
               'rectangle ABCD is'},
    84: {'options': same('9', '10', '11 2/9', '11 1/9')},
    89: {'hi': '(1001)³ का मान है', 'en': 'The value of (1001)³ is'},
    91: {'hi': 'निम्नलिखित में से सबसे छोटी भिन्न कौन-सी है?\n6/11, 13/18, 15/22, 19/36, 5/6',
         'en': 'Which one of the following is the smallest fraction?\n6/11, 13/18, 15/22, 19/36, 5/6',
         'options': same('6/11', '13/18', '15/22', '19/36')},
    93: {'hi': '1.2̅7̅ (अर्थात 1.272727…) बराबर है', 'en': '1.2̅7̅ (that is, 1.272727…) is equal to',
         'options': same('127/100', '73/100', '14/11', '11/14')},
    95: {'hi': 'यदि aˣ = bʸ = cᶻ तथा b² = ac हो, तब y है', 'en': 'If aˣ = bʸ = cᶻ and b² = ac, then y is',
         'options': same('xz/(x + y)', 'xz/(2(x − z))','xz/(2(z − x) + 3)', '2xz/(z + x)')},
    96: {'hi': 'x² − y² − 9z² + 6yz का गुणनखण्ड है', 'en': 'x² − y² − 9z² + 6yz is factorized as'},
    97: {'options': same('(a − b)/2', '(a + b)/2', 'ab/2', 'ab/(a + b)')},
    98: {'hi': 'किसी कक्षा के 6 छात्रों की आयु (वर्षों में) निम्नवत् है:\n13, 14, 18, 16, 19, 12\nइनकी माध्यिका होगी',
         'en': 'The ages (in years) of 6 students in a class are given as:\n13, 14, 18, 16, 19, 12\n'
               'Their median will be'},
    100: {'options': same('20%', '25%', '40/3 %', '50/3 %')},
}

EXPLAIN = {
    82: ('Let AD = b, AB = l and the diagonal AC = d. From AC − AD = 8, d = b + 8. From AB + AC = 5AD, '
         'l = 5b − d = 4b − 8. In the right triangle ABC, d² = l² + b², so (b + 8)² = (4b − 8)² + b², which '
         'simplifies to 16b² = 80b, giving b = 5. Then l = 12 and the area is 12 × 5 = 60 square units.',
         'मान लीजिए AD = b, AB = l और विकर्ण AC = d। AC − AD = 8 से d = b + 8। AB + AC = 5AD से l = 5b − d = 4b − 8। '
         'समकोण त्रिभुज ABC में d² = l² + b², अतः (b + 8)² = (4b − 8)² + b², जिससे 16b² = 80b और b = 5। '
         'तब l = 12 और क्षेत्रफल 12 × 5 = 60 वर्ग इकाई।'),
    83: ('The volume of a cone is (1/3)πr²h, so the volumes are in the ratio (r₁/r₂)² × (h₁/h₂). The diameters, '
         'and so the radii, are in the ratio 4 : 5, giving (16/25) × (1/4) = 4/25. The ratio is 4 : 25.',
         'शंकु का आयतन (1/3)πr²h है, अतः आयतनों का अनुपात (r₁/r₂)² × (h₁/h₂) होगा। व्यासों और इसलिए त्रिज्याओं का अनुपात 4 : 5 है, '
         'तो (16/25) × (1/4) = 4/25, यानी 4 : 25।'),
    84: ('The first 9 primes are 2, 3, 5, 7, 11, 13, 17, 19 and 23. Their sum is 100, so the average is '
         '100/9 = 11 1/9.',
         'पहली 9 अभाज्य संख्याएँ 2, 3, 5, 7, 11, 13, 17, 19 और 23 हैं। इनका योग 100 है, अतः औसत 100/9 = 11 1/9।'),
    85: ('Each step moves the decimal point two places, so the square root moves one place: √29.16 = 5.4, '
         '√0.2916 = 0.54, √0.002916 = 0.054 and √0.00002916 = 0.0054. Their sum is 5.9994.',
         'हर बार दशमलव दो स्थान खिसकता है, तो वर्गमूल में एक स्थान: √29.16 = 5.4, √0.2916 = 0.54, √0.002916 = 0.054 और '
         '√0.00002916 = 0.0054। इनका योग 5.9994 है।'),
    86: ('First : second = 2 : 3 = 10 : 15 and second : third = 5 : 8 = 15 : 24, so the three numbers are in the '
         'ratio 10 : 15 : 24, which adds to 49. The second number is 98 × 15/49 = 30.',
         'पहली : दूसरी = 2 : 3 = 10 : 15 और दूसरी : तीसरी = 5 : 8 = 15 : 24, अतः तीनों का अनुपात 10 : 15 : 24 है, जिसका योग 49 है। '
         'दूसरी संख्या = 98 × 15/49 = 30।'),
    87: ('A regular hexagon inscribed in a circle is made of six equilateral triangles whose sides equal the '
         'radius. Each side is r, so the perimeter is 6r.',
         'वृत्त के अंतर्गत बना समषट्भुज छह समबाहु त्रिभुजों से बनता है जिनकी भुजा त्रिज्या के बराबर होती है। हर भुजा r है, '
         'अतः परिमाप 6r है।'),
    88: ('The incentre is the point where the bisectors of the three angles of a triangle meet; it is the centre '
         'of the inscribed circle. Altitudes meet at the orthocentre, medians at the centroid and perpendicular '
         'bisectors at the circumcentre.',
         'त्रिभुज के तीनों कोणों के अर्धक जिस बिन्दु पर मिलते हैं वह अंतःकेन्द्र है; यही अंतःवृत्त का केन्द्र है। शीर्षलम्ब लम्बकेन्द्र पर, '
         'माध्यिकाएँ केन्द्रक पर और लम्बार्धक परिकेन्द्र पर मिलते हैं।'),
    89: ('(1000 + 1)³ = 1000³ + 3 × 1000² + 3 × 1000 + 1 = 1,000,000,000 + 3,000,000 + 3,000 + 1 = 1,003,003,001.',
         '(1000 + 1)³ = 1000³ + 3 × 1000² + 3 × 1000 + 1 = 1,00,00,00,000 + 30,00,000 + 3,000 + 1 = 1,00,30,03,001।'),
    90: ('If 20% of the number is 120, the number is 120 × 100/20 = 600. 120% of 600 is 720.',
         'यदि संख्या का 20% = 120, तो संख्या = 120 × 100/20 = 600। 600 का 120% = 720।'),
    91: ('As decimals: 6/11 ≈ 0.545, 13/18 ≈ 0.722, 15/22 ≈ 0.682, 19/36 ≈ 0.528 and 5/6 ≈ 0.833. The smallest is '
         '19/36.',
         'दशमलव में: 6/11 ≈ 0.545, 13/18 ≈ 0.722, 15/22 ≈ 0.682, 19/36 ≈ 0.528 और 5/6 ≈ 0.833। सबसे छोटी 19/36 है।'),
    92: ('For the same area, the new breadth must be 1/1.25 = 4/5 of the old one, a decrease of 1/5, or 20%. '
         'In general the decrease is 25/(100 + 25) × 100%.',
         'क्षेत्रफल समान रखने के लिए नई चौड़ाई पुरानी की 1/1.25 = 4/5 होनी चाहिए, यानी 1/5 या 20% की कमी। '
         'सूत्र: कमी = 25/(100 + 25) × 100%।'),
    93: ('Let x = 1.2727… Then 100x = 127.2727…, and subtracting gives 99x = 126, so x = 126/99 = 14/11. The bar '
         'over 27 shows that these digits repeat.',
         'मान लीजिए x = 1.2727… तब 100x = 127.2727…, घटाने पर 99x = 126, अतः x = 126/99 = 14/11। 27 पर लगी रेखा बताती है कि '
         'ये अंक दोहराते हैं।'),
    94: ('Under compound interest the money doubles every 15 years: 2 times after 15 years, 4 times after 30 and '
         '8 times after 45 years.',
         'चक्रवृद्धि ब्याज में धन हर 15 वर्ष में दोगुना होता है: 15 वर्ष में 2 गुना, 30 में 4 गुना और 45 वर्ष में 8 गुना।'),
    95: ('Let aˣ = bʸ = cᶻ = k, so a = k^(1/x), b = k^(1/y) and c = k^(1/z). From b² = ac, 2/y = 1/x + 1/z = '
         '(x + z)/xz, so y = 2xz/(x + z).',
         'मान लीजिए aˣ = bʸ = cᶻ = k, तो a = k^(1/x), b = k^(1/y), c = k^(1/z)। b² = ac से 2/y = 1/x + 1/z = (x + z)/xz, '
         'अतः y = 2xz/(x + z)।'),
    96: ('Group the last three terms: x² − (y² − 6yz + 9z²) = x² − (y − 3z)². As a difference of squares this is '
         '(x + y − 3z)(x − y + 3z).',
         'अंतिम तीन पदों को साथ लें: x² − (y² − 6yz + 9z²) = x² − (y − 3z)²। वर्गों के अंतर से यह '
         '(x + y − 3z)(x − y + 3z) है।'),
    97: ('The segment joining the midpoints of the non-parallel sides of a trapezium (its median) is parallel to '
         'the parallel sides and equal to half their sum: (a + b)/2.',
         'समलम्ब चतुर्भुज की असमांतर भुजाओं के मध्य-बिन्दुओं को मिलाने वाली रेखा समांतर भुजाओं के समांतर होती है और उनके '
         'योग की आधी होती है: (a + b)/2।'),
    98: ('In order the ages are 12, 13, 14, 16, 18, 19. With an even number of values, the median is the average '
         'of the two middle values: (14 + 16)/2 = 15.',
         'क्रम से आयु 12, 13, 14, 16, 18, 19 है। मानों की संख्या सम होने पर माध्यिका बीच के दो मानों का औसत होती है: '
         '(14 + 16)/2 = 15।'),
    99: ('Karl Pearson’s empirical relation for moderately skewed data is Mode = 3 Median − 2 Mean, which can be '
         'written 3 Median = Mode + 2 Mean.',
         'कार्ल पियर्सन का आनुभविक संबंध है: बहुलक = 3 माध्यिका − 2 माध्य, जिसे 3 माध्यिका = बहुलक + 2 माध्य भी लिखा जाता है।'),
    100: ('If the selling price is 100, the loss is 20, so the cost price is 120. The loss on cost price is '
          '20/120 × 100% = 50/3 % (16 2/3 %).',
          'यदि विक्रय मूल्य 100 है तो हानि 20 और क्रय मूल्य 120 है। क्रय मूल्य पर हानि 20/120 × 100% = 50/3 % (16 2/3 %) है।'),
}
