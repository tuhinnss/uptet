"""UPTET 2021 Primary (cancelled exam of 28 Nov 2021), Part IV (Q91–120): Mathematics."""

SOURCE = 'primary21'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (91, 120)
SUBJECT = 'math'

TOPICS = {
    'math.numbers': [92, 94, 96, 97, 98, 105, 106, 108, 109, 110, 111, 112, 113, 120],
    'math.geometry': [93, 100, 101, 102, 104, 107, 117],
    'math.measurement': [91, 95, 99, 103, 114, 116, 118, 119],
}

SKIP = {115: 'needs the pie chart'}

FIX = {
    91: {'en': 'If 15 workers can build a road in 48 hours, then the number of workers required to do the same work in 30 hours is:'},
    92: {'en': 'The least digit x for which the number 324x342 is divisible by 11 is:'},
    95: {'en': 'A sum of ₹600 amounts to ₹720 in 4 years at simple interest. What will it amount to if the rate of interest is '
               'increased by 2%?',
         'hi': '₹600 साधारण ब्याज की दर से 4 वर्ष में ₹720 हो जाता है। यदि ब्याज की दर 2% बढ़ा दी जाये, तो यह धन कितना होगा?'},
    98: {'en': 'The natural number nearest to 3070 which is completely divisible by 17 is:'},
    100: {'en': 'If the diagonal of a cube is 8√3 cm, then its surface area is:'},
    101: {'en': 'The area of a 120° sector of a circle is 66/7 cm². The diameter of the circle is (π = 22/7):',
          'hi': 'एक वृत्त के 120° वाले त्रिज्यखण्ड का क्षेत्रफल 66/7 सेमी² है, तो वृत्त का व्यास होगा (π = 22/7):'},
    102: {'en': 'If the diagonal of a square is doubled, its area will become:'},
    103: {'en': 'Vinay sold a watch for ₹75 and made a profit percentage equal to the cost price of the watch. The cost price '
                'of the watch is:',
          'hi': 'विनय एक घड़ी ₹75 में बेचता है, जिससे उसे घड़ी की लागत कीमत के बराबर प्रतिशत लाभ होता है, तो घड़ी का लागत मूल्य क्या है?'},
    104: {'options': {'d': ('One contains the other', 'एक-दूसरे को घेर लेंगे')}},
    105: {'en': 'The missing number in the pattern 1, 5, 2, 10, ..., 15, 4, 20 is:',
          'hi': 'अंक विन्यास 1, 5, 2, 10, ..., 15, 4, 20 में विलुप्त संख्या है–'},
    106: {'en': 'Two positive integers a and b leave remainders 4 and 5 respectively when divided by 6. The remainder when '
                'a² + b² is divided by 6 is:',
          'hi': 'यदि धन पूर्णांक a और b को 6 से विभाजित करने पर शेषफल क्रमशः 4 और 5 प्राप्त होते हैं, तब a² + b² को 6 से '
                'विभाजित करने पर शेषफल है–'},
    107: {'en': 'If the side of a square is increased by 10%, the percentage increase in its area will be:'},
    108: {'en': "The product of Mohan's age 5 years ago and his age 9 years from now is 15. Mohan's present age is:"},
    109: {'en': 'The value of (0.00032)⁰·⁶ is:', 'hi': '(0.00032)⁰·⁶ का मान है–'},
    110: {'en': 'If the sum of the numbers 5x9, 327 and 2y8 is 1114, then the largest value x can take is:'},
    111: {'en': 'Which rational number is bigger than the rational number 0/–5?',
          'hi': 'परिमेय संख्या 0/–5 से बड़ी परिमेय संख्या है–'},
    112: {'en': 'The product of the L.C.M. and H.C.F. of two numbers is 336 and their difference is 10. The numbers are:'},
    113: {'en': '4⁶¹ + 4⁶² + 4⁶³ + 4⁶⁴ + 4⁶⁵ is divisible by:', 'hi': '4⁶¹ + 4⁶² + 4⁶³ + 4⁶⁴ + 4⁶⁵ किस संख्या से भाज्य होगा–'},
    114: {'en': 'What was the time 5 hours 58 minutes before 3:57 PM?', 'hi': '3:57 PM से 5 घंटे 58 मिनट पहले क्या समय था–',
          'options': {o: (v, v) for o, v in zip('abcd', ['7:58 AM', '9:59 AM', '9:59 PM', '6:59 AM'])}},
    116: {'en': 'Today is 1st April, a Wednesday, in a leap year. What day of the week will this date be after 3 years?'},
    117: {'en': 'The difference between the complement and the supplement of a given acute angle is:'},
    118: {'en': 'In how many years will the simple interest at 16⅔% per annum be 5/6 of the principal?',
          'hi': 'कितने वर्षों में 16⅔% वार्षिक ब्याज की दर से साधारण ब्याज मूलधन का 5/6 हो जाएगा?',
          'options': {o: (f'{v} years', f'{v} वर्ष') for o, v in zip('abcd', [6, 5, 4, 7])}},
    119: {'en': 'What is the profit percentage if you buy bananas at ₹10 a dozen and sell them at 10 bananas for ₹12?',
          'hi': '₹10 दर्जन की दर से केले खरीदकर 12 रुपये के 10 केले की दर से बेचने पर लाभ प्रतिशत क्या होगा?'},
    120: {'en': 'If 30% of a number is 63 less than three-fourths of that number, then the number is:'},
}

EXPLAIN = {
    91: ('Workers × hours stays the same: 15 × 48 = x × 30, so x = 24.', 'मजदूर × घंटे समान रहते हैं: 15 × 48 = x × 30, अतः x = 24।'),
    92: ('For divisibility by 11, the alternating sum of digits must be a multiple of 11. From the right: 2 − 4 + 3 − x + '
         '4 − 2 + 3 = 6 − x, so x = 6.',
         '11 से विभाज्यता के लिए अंकों का एकान्तर योग 11 का गुणज होना चाहिए। दाएँ से: 2 − 4 + 3 − x + 4 − 2 + 3 = 6 − x, अतः x = 6।'),
    93: ('The largest square in a circle of radius r has area 2r², so the ratio πr² : 2r² = π : 2 is the same for every '
         'circle.',
         'त्रिज्या r के वृत्त में सबसे बड़े वर्ग का क्षेत्रफल 2r² होता है, अतः अनुपात πr² : 2r² = π : 2 हर वृत्त के लिए समान है।'),
    94: ('102.7 = 1027/10, and 1027 and 10 have no common factor, so q = 10.', '102.7 = 1027/10, और 1027 तथा 10 का कोई उभयनिष्ठ गुणनखण्ड नहीं, अतः q = 10।'),
    95: ('Interest = ₹120 in 4 years on ₹600, so the rate is 5%. At 7%, interest = 600 × 7 × 4/100 = ₹168, amount = ₹768.',
         '₹600 पर 4 वर्ष में ब्याज ₹120 है, अतः दर 5% है। 7% पर ब्याज = 600 × 7 × 4/100 = ₹168, मिश्रधन = ₹768।'),
    96: ('The sum of two irrational numbers can be rational: √2 + (−√2) = 0. The other statements are always true.',
         'दो अपरिमेय संख्याओं का योग परिमेय भी हो सकता है: √2 + (−√2) = 0। बाकी कथन सदैव सत्य हैं।'),
    97: ('x − 0.2x = 60, so 0.8x = 60 and x = 75.', 'x − 0.2x = 60, अतः 0.8x = 60 और x = 75।'),
    98: ('17 × 180 = 3060 and 17 × 181 = 3077. 3077 is 7 away from 3070 and 3060 is 10 away, so 3077 is nearest.',
         '17 × 180 = 3060 और 17 × 181 = 3077। 3077, 3070 से 7 दूर है और 3060, 10 दूर, अतः 3077 सबसे निकट है।'),
    99: ('If CP = 5 and SP = 4, loss = 1 on 5, i.e. 20%.', 'यदि क्रय मूल्य 5 और विक्रय मूल्य 4 है, तो 5 पर 1 की हानि, अर्थात् 20%।'),
    100: ('A cube\'s diagonal is a√3, so the side is 8 cm. Surface area = 6 × 8² = 384 cm².',
          'घन का विकर्ण a√3 होता है, अतः भुजा 8 सेमी। पृष्ठीय क्षेत्रफल = 6 × 8² = 384 सेमी²।'),
    101: ('A 120° sector is 1/3 of the circle: (1/3) × (22/7) × r² = 66/7 gives r² = 9, r = 3 cm, so the diameter is 6 cm.',
          '120° का त्रिज्यखण्ड वृत्त का 1/3 है: (1/3) × (22/7) × r² = 66/7 से r² = 9, r = 3 सेमी, अतः व्यास 6 सेमी।'),
    102: ('Area of a square = d²/2. Doubling d multiplies the area by 4.', 'वर्ग का क्षेत्रफल = d²/2। विकर्ण दोगुना करने पर क्षेत्रफल चार गुना हो जाता है।'),
    103: ('If the cost is C, then 75 = C + C × C/100. Trying C = 50: 50 + 25 = 75, so the cost price is ₹50.',
          'माना लागत C है, तो 75 = C + C × C/100। C = 50 रखने पर 50 + 25 = 75, अतः लागत मूल्य ₹50 है।'),
    104: ('When the distance between the centres is less than the sum of the radii (and more than their difference), '
          'the circles cut each other at two points.',
          'जब केन्द्रों की दूरी त्रिज्याओं के योग से कम (और उनके अंतर से अधिक) हो, तो वृत्त एक-दूसरे को दो बिन्दुओं पर काटते हैं।'),
    105: ('The pattern pairs n with 5n: (1, 5), (2, 10), (3, 15), (4, 20). The missing number is 3.',
          'विन्यास में n के साथ 5n आता है: (1, 5), (2, 10), (3, 15), (4, 20)। विलुप्त संख्या 3 है।'),
    106: ('a² leaves the same remainder as 4² = 16, i.e. 4; b² as 5² = 25, i.e. 1. So a² + b² leaves 4 + 1 = 5.',
          'a² का शेषफल 4² = 16 जैसा, यानी 4; b² का 5² = 25 जैसा, यानी 1। अतः a² + b² का शेषफल 4 + 1 = 5।'),
    107: ('New area = (1.1)² = 1.21 times, an increase of 21%.', 'नया क्षेत्रफल = (1.1)² = 1.21 गुना, अर्थात् 21% वृद्धि।'),
    108: ('(x − 5)(x + 9) = 15 gives x² + 4x − 60 = 0, so x = 6 (the positive root).',
          '(x − 5)(x + 9) = 15 से x² + 4x − 60 = 0, अतः x = 6 (धनात्मक मूल)।'),
    109: ('0.00032 = (0.2)⁵, so (0.00032)⁰·⁶ = (0.2)⁵ˣ⁰·⁶ = (0.2)³ = 0.008.',
          '0.00032 = (0.2)⁵, अतः (0.00032)⁰·⁶ = (0.2)³ = 0.008।'),
    110: ('509 + 10x + 327 + 208 + 10y = 1114 gives x + y = 7, so the largest x is 7 (with y = 0).',
          '509 + 10x + 327 + 208 + 10y = 1114 से x + y = 7, अतः x का अधिकतम मान 7 है (y = 0 पर)।'),
    111: ('0/–5 = 0. Only −3/−8 = 3/8 is positive, so it is the bigger number.', '0/–5 = 0। केवल −3/−8 = 3/8 धनात्मक है, इसलिए वही बड़ी है।'),
    112: ('LCM × HCF = product of the numbers = 336. 14 × 24 = 336 and 24 − 14 = 10.',
          'ल.स. × म.स. = संख्याओं का गुणनफल = 336। 14 × 24 = 336 और 24 − 14 = 10।'),
    113: ('4⁶¹(1 + 4 + 16 + 64 + 256) = 4⁶¹ × 341 = 4⁶¹ × 11 × 31, so it is divisible by 11.',
          '4⁶¹(1 + 4 + 16 + 64 + 256) = 4⁶¹ × 341 = 4⁶¹ × 11 × 31, अतः यह 11 से भाज्य है।'),
    114: ('3:57 PM minus 6 hours is 9:57 AM; adding back 2 minutes gives 9:59 AM.',
          '3:57 PM से 6 घंटे पहले 9:57 AM था; 2 मिनट वापस जोड़ने पर 9:59 AM।'),
    116: ('From 1 April each later year moves the weekday forward by 1 (365 days), and no 29 February falls in between, '
          'so after 3 years it is Wednesday + 3 = Saturday.',
          '1 अप्रैल से हर अगले वर्ष में दिन 1 आगे बढ़ता है (365 दिन), और बीच में कोई 29 फरवरी नहीं आती, इसलिए 3 वर्ष बाद बुधवार + 3 = शनिवार।'),
    117: ('Supplement − complement = (180° − x) − (90° − x) = 90°.', 'सम्पूरक − पूरक = (180° − x) − (90° − x) = 90°।'),
    118: ('Time = (SI × 100)/(P × R) = (5/6 × 100)/(50/3) = 5 years.', 'समय = (ब्याज × 100)/(मूलधन × दर) = (5/6 × 100)/(50/3) = 5 वर्ष।'),
    119: ('Cost of one banana = 10/12 = ₹5/6, selling price = 12/10 = ₹6/5. Profit % = (6/5 − 5/6) ÷ (5/6) × 100 = 44%.',
          'एक केले का क्रय मूल्य = 10/12 = ₹5/6, विक्रय मूल्य = 12/10 = ₹6/5। लाभ % = (6/5 − 5/6) ÷ (5/6) × 100 = 44%।'),
    120: ('(3/4)x − 0.3x = 63, so 0.45x = 63 and x = 140.', '(3/4)x − 0.3x = 63, अतः 0.45x = 63 और x = 140।'),
}
