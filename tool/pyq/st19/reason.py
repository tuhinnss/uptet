"""Super TET 2019, Q141–145: Reasoning."""

RANGE = (141, 145)
LANGUAGE = None

TOPICS = {
    'reason.logic': [141, 142, 143, 144, 145],
}

SKIP = {}

FIX = {
    142: {'hi': 'निम्नलिखित में प्रश्नवाचक चिह्न (?) के स्थान पर क्या आना चाहिए?\nMK : 169/121 :: JH : ?',
          'en': 'What should come in place of question mark (?) in the following?\nMK : 169/121 :: JH : ?',
          'options': {1: ('100/64', '100/64'), 2: ('100/81', '100/81'), 3: ('61/120', '61/120'), 4: ('81/100', '81/100')}},
}

EXPLAIN = {
    141: ('A and B are siblings and C is B’s mother, so A is C’s daughter. D is C’s father, so A is D’s '
          'granddaughter. E is not needed.',
          'A और B भाई-बहन हैं और C, B की माँ है, अतः A, C की पुत्री है। D, C का पिता है, इसलिए A, D की पौत्री (नातिन) है। '
          'E की जानकारी की आवश्यकता नहीं है।'),
    142: ('M and K are the 13th and 11th letters, and 169/121 is 13²/11². J and H are the 10th and 8th letters, so '
          'the answer is 10²/8² = 100/64.',
          'M और K वर्णमाला के 13वें और 11वें अक्षर हैं, और 169/121 = 13²/11²। J और H 10वें और 8वें अक्षर हैं, अतः उत्तर '
          '10²/8² = 100/64।'),
    143: ('After 40 km east, 20 km north and then 20 km west (a left turn from north), Rahul is 20 km east and '
          '20 km north of the start. The distance is √(20² + 20²) = 20√2 km.',
          '40 किमी पूर्व, 20 किमी उत्तर और फिर बायें (पश्चिम) 20 किमी चलने पर राहुल प्रारम्भ से 20 किमी पूर्व और 20 किमी उत्तर में है। '
          'दूरी = √(20² + 20²) = 20√2 किमी।'),
    144: ('“are” is common to 256 and 637, so are = 6. “good” is common to 256 and 358, so good = 5. “bad” is common '
          'to 637 and 358, so bad = 3. In 358 the remaining digit, 8, means “and”.',
          '256 और 637 में ‘are’ समान है, अतः are = 6। 256 और 358 में ‘good’ समान है, अतः good = 5। 637 और 358 में ‘bad’ समान है, '
          'अतः bad = 3। 358 में बचा अंक 8 ‘and’ के लिए है।'),
    145: ('FORGE → FPTJI moves the letters forward by 0, 1, 2, 3, 4. Applying 0 to 6 to CULPRIT gives C, V, N, S, V, '
          'N, Z: CVNSVNZ.',
          'FORGE → FPTJI में अक्षर क्रमशः 0, 1, 2, 3, 4 स्थान आगे बढ़ते हैं। CULPRIT पर 0 से 6 तक लगाने पर C, V, N, S, V, N, Z '
          'यानी CVNSVNZ मिलता है।'),
}
