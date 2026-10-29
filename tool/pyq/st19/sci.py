"""Super TET 2019, Q71–80: Science."""

RANGE = (71, 80)
LANGUAGE = None

TOPICS = {
    'sci.physics': [72, 73, 74, 77, 80],
    'sci.chemistry': [71, 75, 79],
    'sci.biology': [76, 78],
}

SKIP = {}

POWERS = [('10⁻⁹ m', '10⁻⁹ m'), ('10⁻¹² m', '10⁻¹² m'), ('10⁻⁶ m', '10⁻⁶ m'), ('10⁻¹⁵ m', '10⁻¹⁵ m')]

FIX = {
    74: {'options': dict(enumerate(POWERS, 1))},
    77: {'hi': 'सरल रेखा पर गतिशील किसी कण की स्थिति x, समय के साथ संबंध x = 6t² − 5t के अनुसार बदलती है, जहाँ x मीटर में, '
               't सेकंड में है। कण का प्रारम्भिक वेग होगा',
         'en': 'The position x of a particle moving along a straight line path varies with time according to the '
               'relation x = 6t² − 5t, where x is in meter, t is in second. The initial velocity of the particle is'},
    79: {'hi': '4.4 g CO₂ का NTP पर आयतन होगा', 'en': 'The volume of 4.4 g CO₂ at NTP will be'},
}

EXPLAIN = {
    71: ('Common salt, sodium chloride (NaCl), is formed when hydrochloric acid (a strong acid) neutralises sodium '
         'hydroxide (a strong base): HCl + NaOH → NaCl + H₂O. That is why its solution is neutral.',
         'खाने का नमक सोडियम क्लोराइड (NaCl) हाइड्रोक्लोरिक अम्ल (प्रबल अम्ल) और सोडियम हाइड्रॉक्साइड (प्रबल क्षार) की उदासीनीकरण '
         'अभिक्रिया से बनता है: HCl + NaOH → NaCl + H₂O। इसीलिए इसका विलयन उदासीन होता है।'),
    72: ('Momentum p and kinetic energy K are related by p = √(2mK). If K becomes 4 times, p becomes √4 = 2 times '
         'its initial value.',
         'संवेग p और गतिज ऊर्जा K का संबंध p = √(2mK) है। K चार गुना होने पर p, √4 = 2 गुना हो जाता है।'),
    73: ('In sound waves the particles of the medium vibrate back and forth along the direction in which the wave '
         'travels, forming compressions and rarefactions, so sound waves are longitudinal. They are mechanical, '
         'not electromagnetic, and cannot travel through a vacuum.',
         'ध्वनि तरंगों में माध्यम के कण तरंग की दिशा में ही आगे-पीछे कंपन करते हैं और संपीडन तथा विरलन बनाते हैं, इसलिए ये '
         'अनुदैर्घ्य होती हैं। ये यांत्रिक तरंगें हैं, विद्युत-चुम्बकीय नहीं, और निर्वात में नहीं चल सकतीं।'),
    74: ('A micron (micrometre, μm) is one millionth of a metre: 1 μm = 10⁻⁶ m. A nanometre is 10⁻⁹ m and a '
         'picometre 10⁻¹² m.',
         'एक माइक्रॉन (माइक्रोमीटर, μm) एक मीटर का दस लाखवाँ भाग है: 1 μm = 10⁻⁶ m। नैनोमीटर 10⁻⁹ m और पिकोमीटर 10⁻¹² m होता है।'),
    75: ('Most of the ozone layer lies in the stratosphere, about 15 to 35 km above the Earth. It absorbs most of '
         'the Sun’s harmful ultraviolet rays.',
         'ओज़ोन परत का अधिकांश भाग समताप मंडल (स्ट्रैटोस्फीयर) में लगभग 15 से 35 किमी की ऊँचाई पर है। यह सूर्य की हानिकारक '
         'पराबैंगनी किरणों का अधिकांश भाग सोख लेती है।'),
    76: ('Insects such as the cockroach breathe through spiracles, small openings on the sides of the body that lead '
         'into a network of air tubes (tracheae). Fish use gills, the earthworm breathes through its moist skin and '
         'Pila (the apple snail) uses a gill and a lung sac.',
         'तिलचट्टे जैसे कीट श्वास-छिद्रों (स्पाइरेकल) से साँस लेते हैं, जो शरीर के किनारों पर होते हैं और वायु-नलिकाओं (ट्रेकिया) से '
         'जुड़े रहते हैं। मछली गलफड़ों से, केंचुआ नम त्वचा से और घोंघा (पाइला) गिल तथा फुफ्फुस-कोष से साँस लेता है।'),
    77: ('Velocity is the rate of change of position: v = dx/dt = 12t − 5. At the start (t = 0), v = −5 m/s. The '
         'minus sign means the particle starts moving in the negative x direction.',
         'वेग स्थिति के परिवर्तन की दर है: v = dx/dt = 12t − 5। प्रारम्भ में (t = 0) v = −5 m/s। ऋण चिह्न बताता है कि कण ऋणात्मक x '
         'दिशा में चलना शुरू करता है।'),
    78: ('Vitamin A is needed to make rhodopsin, the pigment in the rods of the retina that lets us see in dim '
         'light. Its deficiency causes night blindness.',
         'विटामिन A से रेटिना की छड़ों में रोडॉप्सिन वर्णक बनता है, जिससे हम कम रोशनी में देख पाते हैं। इसकी कमी से रतौंधी होती है।'),
    79: ('The molar mass of CO₂ is 12 + 2 × 16 = 44 g/mol, so 4.4 g is 0.1 mol. One mole of a gas occupies 22.4 L at '
         'NTP, so 0.1 mol occupies 2.24 L.',
         'CO₂ का मोलर द्रव्यमान 12 + 2 × 16 = 44 g/mol है, अतः 4.4 g = 0.1 मोल। NTP पर एक मोल गैस 22.4 L घेरती है, '
         'इसलिए 0.1 मोल 2.24 L घेरेगी।'),
    80: ('Of the fundamental forces, gravity is by far the weakest; the strong nuclear force is the strongest, and '
         'electric and magnetic forces are much stronger than gravity.',
         'मूल बलों में गुरुत्वाकर्षण बल सबसे क्षीण है; प्रबल नाभिकीय बल सबसे शक्तिशाली है, और विद्युत तथा चुम्बकीय बल गुरुत्व से '
         'कहीं अधिक प्रबल हैं।'),
}
