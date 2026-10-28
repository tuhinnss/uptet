"""UPTET 2019 Junior, Part IV (1) (Q121–150): Science."""

SOURCE = 'junior_ms'
ID_PREFIX = 'jms'
PAPER_LABEL = 'Junior level paper, Mathematics and Science option'
RANGE = (121, 150)
SUBJECT = 'sci'

TOPICS = {
    'sci.physics': [121, 122, 123, 124, 125, 136, 137, 138, 139, 140],
    'sci.chemistry': [131, 132, 133, 134, 135, 141, 142, 143, 144, 145],
    'sci.biology': [126, 127, 129, 130, 146, 147, 148, 149, 150],
}

SKIP = {128: 'the answer key accepts no single option'}


def opts(values):
    return {o: (v, v) for o, v in zip('abcd', values)}


FIX = {
    121: {'options': opts(['x₁ ⋚ x₂', 'x₁ < x₂', 'x₁ > x₂', 'x₁ = x₂'])},
    124: {'options': {o: (f'10⁻{e} micron', f'10⁻{e} माइक्रॉन') for o, e in zip('abcd', ['¹⁰', '²', '⁴', '⁶'])}},
    129: {'options': {'b': (None, 'वो पौधे और जन्तु जो केवल एक विशिष्ट भौगोलिक क्षेत्र में पाए जाते हों।')}},
    133: {'en': 'Consider the following compounds:\nI. BF₃  II. IF₇  III. CO₂  IV. PCl₅\nAmong these compounds, the electrophiles are:',
          'hi': 'निम्न यौगिकों पर विचार कीजिए:\nI. BF₃  II. IF₇  III. CO₂  IV. PCl₅\nइन यौगिकों में इलेक्ट्रानस्नेही हैं–',
          'options': {'a': ('I, II, III and IV', 'I, II, III और IV'), 'b': ('I and II', 'I और II'),
                      'c': ('III and IV', 'III और IV'), 'd': ('I, III and IV', 'I, III और IV')}},
    134: {'options': opts(['NO₂–C₆H₄–CHO', 'C₆H₅CHO', 'CH₃–C₆H₄–CHO', 'CH₃O–C₆H₄–CHO'])},
    135: {'en': 'On moving down a group in the periodic table:\nA. The value of electronegativity decreases\n'
                'B. Atomic radius increases\nC. The value of ionisation enthalpy decreases',
          'hi': 'आवर्त सारणी के एक वर्ग में ऊपर से नीचे की ओर आने पर–\nA. विद्युत ऋणात्मकता के मान में कमी आती है\n'
                'B. परमाणु त्रिज्या में वृद्धि होती है\nC. आयनन एन्थैल्पी के मान में कमी आती है',
          'options': {'a': ('A, B and C', 'A, B और C'), 'b': ('Only A', 'केवल A'), 'c': ('Only B', 'केवल B'),
                      'd': ('Only C', 'केवल C')}},
    136: {'options': {'b': ('X-rays', 'X-किरणें')}},
    140: {'en': 'The kinetic energy of a particle of mass m is E. Its momentum will be:',
          'hi': 'm द्रव्यमान के एक कण की गतिज ऊर्जा E है। इसका संवेग होगा–',
          'options': opts(['√(2mE)', '(1/2)mE', '2mE', '√(mE/2)'])},
    142: {'en': 'The number of 3° (tertiary) carbons in 2-methylpropane is:',
          'hi': '2-मेथिल प्रोपेन में 3° (तृतीयक) कार्बन की संख्या है–'},
    143: {'en': 'The IUPAC name of the compound CH₃–CH(CH₃)–OCH₃ is:',
          'hi': 'यौगिक CH₃–CH(CH₃)–OCH₃ का आई.यू.पी.ए.सी. नाम क्या होगा?',
          'options': opts(['Isopropyl methyl ether', '1-methoxy-1-methylethane', '2-methoxy-2-methylethane',
                           '2-methoxypropane'])},
    144: {'en': 'In catenation (bond energy for self-linking), the element next to carbon is:',
          'hi': 'कार्बन के बाद शृंखलन हेतु बंध ऊर्जा (शृंखलन क्षमता) किस तत्व की है?'},
    145: {'en': 'nx mole of substance x was dissolved in ny mole of substance y.\n'
                'A. The total of the mole fractions of x and y is 1.\n'
                'B. Mole fraction of x = (number of moles of x) / (number of moles of solution)\n'
                'C. Mole fraction of y = ny / (nx + ny)\n'
                'D. Mole fraction of x = nx / (ny + ny)',
          'hi': 'पदार्थ x के nx मोल को पदार्थ y के ny मोल में घोला गया।\n'
                'A. पदार्थ x तथा y के मोल अंश का योगफल 1 होता है।\n'
                'B. x का मोल अंश = (x के मोलों की संख्या) / (विलयन के मोलों की संख्या)\n'
                'C. y का मोल अंश = ny / (nx + ny)\n'
                'D. x का मोल अंश = nx / (ny + ny)',
          'options': {'a': ('A, B and C', 'A, B और C'), 'b': ('Only D', 'केवल D'), 'c': ('Only A', 'केवल A'),
                      'd': ('Only A, B', 'केवल A, B')}},
}

EXPLAIN = {
    121: ('A convex mirror always forms a virtual, erect and diminished image, so the image is shorter: x₁ > x₂.',
          'उत्तल दर्पण सदैव आभासी, सीधा और छोटा प्रतिबिम्ब बनाता है, इसलिए प्रतिबिम्ब छोटा होगा: x₁ > x₂।'),
    122: ('Heat is a form of energy, so its SI unit is the joule. The calorie and erg are older units.',
          'ऊष्मा ऊर्जा का एक रूप है, इसलिए इसकी SI इकाई जूल है। कैलोरी और अर्ग पुरानी इकाइयाँ हैं।'),
    123: ('Sound travels through air and other fluids as longitudinal waves of compression and rarefaction.',
          'ध्वनि वायु और अन्य तरल माध्यमों में सम्पीडन और विरलन वाली अनुदैर्ध्य तरंगों के रूप में चलती है।'),
    124: ('1 Å = 10⁻¹⁰ m and 1 micron = 10⁻⁶ m, so 1 Å = 10⁻⁴ micron.',
          '1 Å = 10⁻¹⁰ मी और 1 माइक्रॉन = 10⁻⁶ मी, अतः 1 Å = 10⁻⁴ माइक्रॉन।'),
    125: ('Sound travels fastest in solids such as steel (about 5000 m/s), slower in water and slowest in air. It cannot '
          'travel in a vacuum.',
          'ध्वनि ठोसों जैसे इस्पात में सबसे तेज (लगभग 5000 मी/से), जल में कम और वायु में सबसे धीमी चलती है। निर्वात में ध्वनि नहीं चलती।'),
    126: ('Riccia fluitans is a floating aquatic liverwort (bryophyte); the other species grow on moist soil.',
          'रिक्सिया फ्लूटेन्स पानी पर तैरने वाला जलीय ब्रायोफाइट है; अन्य जातियाँ नम मिट्टी पर उगती हैं।'),
    127: ('Cuscuta (amarbel) is leafless, has no chlorophyll and depends completely on the host\'s stem, so it is a total '
          'stem parasite. Viscum and sandalwood are partial parasites.',
          'अमरबेल (कस्कुटा) पत्ती रहित है, इसमें पर्णहरित नहीं होता और यह पूरी तरह पोषी के तने पर निर्भर है, इसलिए यह पूर्ण स्तम्भ परजीवी है। '
          'विस्कम और चन्दन आंशिक परजीवी हैं।'),
    129: ('Endemic species are found naturally only in one particular geographical area and nowhere else.',
          'स्थानिक जातियाँ प्राकृतिक रूप से केवल एक विशेष भौगोलिक क्षेत्र में पाई जाती हैं, और कहीं नहीं।'),
    130: ('The pistil, from top to bottom, has the stigma, style and ovary, and sits on the thalamus.',
          'स्त्रीकेसर में ऊपर से नीचे की ओर वर्तिकाग्र, वर्तिका और अण्डाशय होते हैं, और यह पुष्पासन पर स्थित होता है।'),
    131: ('Calcination is heating an ore (usually a carbonate) in little or no air so that it decomposes: MgCO₃ → MgO + CO₂. '
          'Heating a sulphide in air, as in (d), is roasting.',
          'कैल्शिनेशन (निस्तापन) में अयस्क (प्रायः कार्बोनेट) को वायु की अनुपस्थिति या कम वायु में गर्म कर विघटित किया जाता है: '
          'MgCO₃ → MgO + CO₂। (d) की तरह सल्फाइड को वायु में गर्म करना भर्जन है।'),
    132: ('Hydrogen sulphide reacts with lead acetate to form black lead sulphide (PbS), so it blackens lead acetate paper.',
          'हाइड्रोजन सल्फाइड लेड एसिटेट से अभिक्रिया कर काला लेड सल्फाइड (PbS) बनाती है, इसलिए यह लेड एसिटेट पेपर को काला कर देती है।'),
    133: ('All four can accept an electron pair: BF₃ has an incomplete octet, IF₇ and PCl₅ can expand their octets, and the '
          'carbon in CO₂ is electron-poor. So all are electrophiles (Lewis acids).',
          'चारों यौगिक इलेक्ट्रॉन युग्म ग्रहण कर सकते हैं: BF₃ का अष्टक अपूर्ण है, IF₇ और PCl₅ अपना अष्टक बढ़ा सकते हैं, और CO₂ का '
          'कार्बन इलेक्ट्रॉन-न्यून है। इसलिए सभी इलेक्ट्रानस्नेही (लुईस अम्ल) हैं।'),
    134: ('The electron-withdrawing –NO₂ group makes the carbonyl carbon more positive, so p-nitrobenzaldehyde reacts '
          'fastest with nucleophiles. –CH₃ and –OCH₃ donate electrons and slow the reaction.',
          'इलेक्ट्रॉन खींचने वाला –NO₂ समूह कार्बोनिल कार्बन को अधिक धनात्मक बनाता है, इसलिए p-नाइट्रोबेन्जैल्डिहाइड नाभिकस्नेही योगज '
          'अभिक्रिया में सबसे अधिक क्रियाशील है। –CH₃ और –OCH₃ इलेक्ट्रॉन देते हैं और अभिक्रिया धीमी करते हैं।'),
    135: ('Down a group, new shells are added: atomic radius increases, and the outer electrons are held less tightly, so '
          'electronegativity and ionisation enthalpy decrease. All three statements are true.',
          'वर्ग में नीचे जाने पर नए कोश जुड़ते हैं: परमाणु त्रिज्या बढ़ती है और बाहरी इलेक्ट्रॉन कम मजबूती से बँधे रहते हैं, इसलिए '
          'विद्युत ऋणात्मकता और आयनन एन्थैल्पी घटती हैं। तीनों कथन सही हैं।'),
    136: ('Ultrasonic waves are sound (mechanical) waves of high frequency. Infrared, X-rays and microwaves are '
          'electromagnetic waves.',
          'पराश्रव्य तरंगें उच्च आवृत्ति की ध्वनि (यांत्रिक) तरंगें हैं। अवरक्त, X-किरणें और सूक्ष्मतरंगें विद्युत चुम्बकीय तरंगें हैं।'),
    137: ('At the magnetic equator the earth\'s field is horizontal, so the angle of dip is 0°. At the magnetic poles it is 90°.',
          'चुम्बकीय भूमध्य रेखा पर पृथ्वी का चुम्बकीय क्षेत्र क्षैतिज होता है, इसलिए नतिकोण 0° है। चुम्बकीय ध्रुवों पर यह 90° होता है।'),
    138: ('The decibel (dB) is a unit for measuring the intensity (level) of sound.',
          'डेसीबल (dB) ध्वनि की तीव्रता (स्तर) मापने की इकाई है।'),
    139: ('Kirchhoff\'s current law says the current entering a junction equals the current leaving it, which follows '
          'from the conservation of charge.',
          'किरचॉफ के धारा नियम के अनुसार किसी संधि पर आने वाली धारा उससे जाने वाली धारा के बराबर होती है; यह आवेश संरक्षण पर आधारित है।'),
    140: ('E = p²/2m, so p = √(2mE).', 'E = p²/2m, अतः p = √(2mE)।'),
    141: ('Sulphide ores such as copper pyrites (CuFeS₂) are concentrated by froth floatation, using pine oil to make the '
          'ore particles float.',
          'कॉपर पाइराइट (CuFeS₂) जैसे सल्फाइड अयस्कों का सान्द्रण फेन उत्प्लवन विधि से होता है, जिसमें चीड़ के तेल से अयस्क कण झाग के साथ ऊपर आते हैं।'),
    142: ('2-Methylpropane is (CH₃)₃CH. Only the central carbon is joined to three other carbons, so there is one 3° carbon.',
          '2-मेथिल प्रोपेन (CH₃)₃CH है। केवल बीच का कार्बन तीन कार्बनों से जुड़ा है, अतः 3° कार्बन एक है।'),
    143: ('The longest carbon chain has three carbons (propane) with –OCH₃ on carbon 2, so the name is 2-methoxypropane. '
          '"Isopropyl methyl ether" is its common name.',
          'सबसे लम्बी कार्बन शृंखला में तीन कार्बन (प्रोपेन) हैं और –OCH₃ कार्बन 2 पर है, अतः नाम 2-मेथॉक्सीप्रोपेन है। '
          '"आइसोप्रोपिल मेथिल ईथर" इसका सामान्य नाम है।'),
    144: ('The answer key gives silicon: in group 14, catenation falls as C > Si > Ge > Sn, because Si–Si bonds are weaker '
          'than C–C bonds. (Sulphur also shows strong catenation.)',
          'उत्तर कुंजी सिलिकॉन को सही मानती है: वर्ग 14 में शृंखलन क्षमता C > Si > Ge > Sn के क्रम में घटती है, क्योंकि Si–Si बन्ध '
          'C–C बन्ध से कमजोर है। (सल्फर भी अच्छा शृंखलन दिखाता है।)'),
    145: ('Mole fractions add up to 1, and the mole fraction of a component is its moles divided by the total moles, so '
          'A, B and C are true. D is wrong: the denominator should be nx + ny.',
          'मोल अंशों का योग 1 होता है, और किसी घटक का मोल अंश उसके मोलों को कुल मोलों से भाग देने पर मिलता है, अतः A, B और C सही हैं। '
          'D गलत है: हर nx + ny होना चाहिए।'),
    146: ('Vitamin D (calcitriol) is made in the skin in sunlight and acts like a hormone, controlling calcium absorption.',
          'विटामिन D (कैल्सिट्रियॉल) धूप में त्वचा में बनता है और हार्मोन की तरह कैल्शियम अवशोषण को नियंत्रित करता है।'),
    147: ('In Whittaker\'s five-kingdom system, prokaryotes such as bacteria and blue-green algae (cyanobacteria) are '
          'placed in Monera.',
          'व्हिटेकर के पाँच जगत वर्गीकरण में बैक्टीरिया और नील हरित शैवाल (सायनोबैक्टीरिया) जैसे प्रोकैरियोट मोनेरा जगत में रखे गए हैं।'),
    148: ('Blood is a fluid connective tissue. The lung, ovary and kidney are organs made of several tissues.',
          'रक्त एक तरल संयोजी ऊतक है। फेफड़ा, अण्डाशय और वृक्क कई ऊतकों से बने अंग हैं।'),
    149: ('A surge of luteinising hormone (LH) in mid-cycle triggers ovulation, the release of the egg.',
          'मासिक चक्र के बीच ल्यूटिनाइजिंग हार्मोन (LH) में तेज वृद्धि अण्डोत्सर्ग (अण्डे के मुक्त होने) को प्रेरित करती है।'),
    150: ('Hippocampus is the sea horse, a bony fish.', 'हिप्पोकैम्पस समुद्री घोड़ा (सी-हॉर्स) है, जो एक अस्थिल मछली है।'),
}
