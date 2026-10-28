"""UPTET 2019 Junior, Part IV (2) (Q91–150): Social Studies and other subjects."""

SOURCE = 'junior_ss'
ID_PREFIX = 'jss'
PAPER_LABEL = 'Junior level paper, Social Studies option'
RANGE = (91, 150)
SUBJECT = 'sst'

TOPICS = {
    'sst.history': list(range(91, 101)),
    'sst.geography': list(range(101, 111)) + [136, 137, 138, 139, 140],
    'sst.civics': list(range(111, 121)),
    'sst.other': list(range(121, 136)) + [141, 142, 143, 146, 147, 148, 149, 150],
    'sst.pedagogy': [144, 145],
}

SKIP = {}

FIX = {
    92: {'options': {'d': (None, 'अलाउद्दीन खिलजी')}},
    93: {
        'en': 'Match the following:\nA. Raja Ram Mohan Roy, B. Vivekanand, C. Dayanand Saraswati, D. M.G. Ranade\n'
              'I. Ram Krishna Mission, II. Prarthana Samaj, III. Brahmo Samaj, IV. Arya Samaj',
        'hi': 'सुमेलित कीजिए:\nA. राजा राम मोहन राय, B. विवेकानन्द, C. दयानन्द सरस्वती, D. एम.जी. रानाडे\n'
              'I. रामकृष्ण मिशन, II. प्रार्थना समाज, III. ब्रह्म समाज, IV. आर्य समाज',
        'match': ['I II III IV', 'III I IV II', 'III IV II I', 'IV I II III'],
    },
    99: {'options': {'c': (None, 'हुमायूँ')}},
    107: {
        'en': 'Which of the following is/are the ideal conditions for temperature inversion to occur?\n'
              'A. Cloudy skies\nB. Calm and stable air\nC. Long summer days',
        'hi': 'निम्नलिखित में कौन–सा/से ताप–व्युत्क्रमण के लिए आदर्श स्थितियाँ हैं?\n'
              'A. बादलयुक्त आकाश\nB. शांत एवं स्थिर वायु\nC. लंबे ग्रीष्मकालीन दिन',
        'options': {'a': ('A, B and C', 'A, B और C'), 'b': ('B only', 'केवल B'), 'c': ('C only', 'केवल C'),
                    'd': ('B and C only', 'केवल B और C')},
    },
    113: {
        'en': 'Which of the following are included in the 73rd Amendment of the Constitution?\n'
              'A. Zilla Panchayat\nB. Kshetra Panchayat\nC. Gram Panchayat\nD. Nagar Nigam',
        'hi': 'निम्नलिखित में से कौन–से संविधान के 73वें संशोधन में सम्मिलित हैं?\n'
              'A. जिला पंचायत\nB. क्षेत्र पंचायत\nC. ग्राम पंचायत\nD. नगर निगम',
        'options': {'a': ('All the four', 'सभी चारों'), 'b': ('A, B and D', 'A, B और D'),
                    'c': ('B, C and D', 'B, C और D'), 'd': ('A, B and C', 'A, B और C')},
    },
    129: {'options': {o: (f'{v} g/cm³', f'{v} ग्राम/सेमी³') for o, v in zip('abcd', ['2.85', '2.56', '2.65', '2.75'])}},
    132: {'options': {'b': (None, 'भाप से पकाना')}},
    134: {'en': 'Name the virus that causes smallpox (chechak).'},
    137: {'options': {'c': ('Alligator', None), 'd': ('Gangetic dolphin', None)}},
    144: {'options': {'a': ('Herbart', None)}},
}

EXPLAIN = {
    91: ('Kalhana\'s "Rajatarangini" (c. 1148–49 CE), a chronicle of the kings of Kashmir, is the main source for '
         'twelfth-century Kashmir.',
         'कल्हण की ‘राजतरंगिणी’ (लगभग 1148–49 ई.), जिसमें कश्मीर के राजाओं का इतिहास है, बारहवीं शताब्दी के कश्मीर का मुख्य स्रोत है।'),
    92: ('Alauddin Khilji took the title "Sikandar-e-Sani" (the second Alexander) and had it put on his coins.',
         'अलाउद्दीन खिलजी ने ‘सिकन्दर-ए-सानी’ (दूसरा सिकन्दर) की उपाधि धारण की और इसे अपने सिक्कों पर अंकित कराया।'),
    93: ('Raja Ram Mohan Roy founded the Brahmo Samaj (1828), Vivekanand the Ramakrishna Mission (1897), Dayanand '
         'Saraswati the Arya Samaj (1875), and M.G. Ranade was a leader of the Prarthana Samaj. So A–III, B–I, C–IV, D–II.',
         'राजा राम मोहन राय ने ब्रह्म समाज (1828), विवेकानन्द ने रामकृष्ण मिशन (1897) और दयानन्द सरस्वती ने आर्य समाज (1875) की स्थापना की, '
         'तथा एम.जी. रानाडे प्रार्थना समाज के नेता थे। अतः A–III, B–I, C–IV, D–II।'),
    94: ('Madam Bhikaji Cama, who unfurled an Indian flag at Stuttgart in 1907, is called the "Mother of the Indian '
         'Revolution".',
         'मैडम भीकाजी कामा, जिन्होंने 1907 में स्टुटगार्ट में भारतीय ध्वज फहराया, ‘भारतीय क्रांति की जननी’ कहलाती हैं।'),
    95: ('Rudradaman\'s Junagadh inscription says the Sudarshan lake was built in the time of Chandragupta Maurya by his '
         'governor Pushyagupta.',
         'रुद्रदामन के जूनागढ़ अभिलेख के अनुसार सुदर्शन झील चन्द्रगुप्त मौर्य के समय उनके राज्यपाल पुष्यगुप्त ने बनवाई थी।'),
    96: ('The Banskhera and Madhuban inscriptions of Harsha begin the Pushyabhuti (Vardhana) genealogy with Naravardhana.',
         'हर्ष के बांसखेड़ा और मधुबन अभिलेखों में पुष्यभूति (वर्धन) वंश की वंशावली नरवर्धन के नाम से प्रारम्भ होती है।'),
    97: ('The answer key gives the Ahar (Banas) culture of south-east Rajasthan; dates from Ahar and Balathal go back to '
         'about the early third millennium BCE, earlier than the Kayatha, Malwa and Jorwe cultures.',
         'उत्तर कुंजी दक्षिण-पूर्वी राजस्थान की अहार (बनास) संस्कृति को प्राचीनतम मानती है; अहार और बालाथल की तिथियाँ लगभग ईसा पूर्व तीसरी '
         'सहस्राब्दी के प्रारम्भ तक जाती हैं, जो कायथा, मालवा और जोर्वे संस्कृतियों से पहले है।'),
    98: ('Before the Mauryas, north India was divided into the sixteen Mahajanapadas, some monarchies and some '
         'republics (ganas), as listed in the Anguttara Nikaya.',
         'मौर्यों से पहले उत्तर भारत सोलह महाजनपदों में बँटा था, जिनमें कुछ राजतंत्र और कुछ गणराज्य थे (अंगुत्तर निकाय के अनुसार)।'),
    99: ('Babur laid out the Aram Bagh in Agra, one of the earliest Mughal gardens.',
         'बाबर ने आगरा में आराम बाग बनवाया, जो सबसे पुराने मुगल बागों में से एक है।'),
    100: ('Bal Gangadhar Tilak started his Home Rule League at Belgaum in April 1916; Annie Besant started hers in '
          'September 1916. The key credits Tilak.',
          'बाल गंगाधर तिलक ने अप्रैल 1916 में बेलगाँव में होम रूल लीग शुरू की; एनी बेसेन्ट ने सितम्बर 1916 में अपनी लीग शुरू की। '
          'उत्तर कुंजी तिलक को सही मानती है।'),
    101: ('An antecedent river is older than the mountains it crosses and keeps cutting its valley as they rise. The '
          'Satluj (like the Indus and Brahmaputra) cuts across the Himalaya in deep gorges.',
          'पूर्ववर्ती नदी उन पर्वतों से पुरानी होती है जिन्हें वह काटती है, और पर्वतों के उठने के साथ अपनी घाटी काटती रहती है। सतलुज '
          '(सिन्धु और ब्रह्मपुत्र की तरह) हिमालय को गहरे महाखड्डों में काटती है।'),
    102: ('The outermost solid layer of the earth is the crust. (The lithosphere includes the crust and the upper mantle.)',
          'पृथ्वी की सबसे बाहरी ठोस परत भूपर्पटी (क्रस्ट) है। (स्थलमण्डल में भूपर्पटी और ऊपरी मैंटल दोनों आते हैं।)'),
    103: ('The Kuroshio is a warm current flowing north past Japan. The Kurile (Oyashio), Canary and Labrador currents are cold.',
          'क्यूरोशियो जापान के पास उत्तर की ओर बहने वाली गर्म धारा है। कुराइल (ओयाशियो), कनारी और लैब्राडोर ठंडी धाराएँ हैं।'),
    104: ('Water transport needs no tracks or roads to be built and can carry heavy loads, so it is the cheapest '
          'means of transport.',
          'जल परिवहन में सड़क या पटरी बनाने की आवश्यकता नहीं होती और यह भारी सामान ढो सकता है, इसलिए यह सबसे सस्ता साधन है।'),
    105: ('The Godavari rises at Trimbakeshwar near Nashik in Maharashtra.',
          'गोदावरी महाराष्ट्र में नासिक के पास त्र्यम्बकेश्वर से निकलती है।'),
    106: ('The Suez Canal in Egypt links the Mediterranean Sea with the Red Sea.',
          'मिस्र की स्वेज नहर भूमध्य सागर को लाल सागर से जोड़ती है।'),
    107: ('Temperature inversion happens on long winter nights with clear skies and calm, stable air, when the ground '
          'loses heat quickly. Cloudy skies and long summer days work against it, so only B is correct.',
          'ताप-व्युत्क्रमण लम्बी शीतकालीन रातों में साफ आकाश तथा शांत, स्थिर वायु में होता है, जब धरातल तेजी से ऊष्मा खोता है। '
          'बादल और लम्बे ग्रीष्मकालीन दिन इसके विपरीत हैं, इसलिए केवल B सही है।'),
    108: ('The Meghalaya (Shillong) plateau is an extension of the Peninsular plateau, separated by the Malda gap.',
          'मेघालय (शिलांग) का पठार प्रायद्वीपीय पठार का विस्तार है, जो मालदा भ्रंश से अलग हुआ है।'),
    109: ('Sand dunes are formed by wind, which piles up sand in deserts and along coasts.',
          'बालू के टीले पवन द्वारा बनते हैं, जो मरुस्थलों और तटों पर बालू का ढेर लगाती है।'),
    110: ('The troposphere is the lowest layer of the atmosphere, where weather happens; above it come the '
          'stratosphere, mesosphere and thermosphere.',
          'क्षोभमण्डल वायुमण्डल की सबसे निचली परत है, जहाँ मौसम की घटनाएँ होती हैं; इसके ऊपर समतापमण्डल, मध्यमण्डल और तापमण्डल हैं।'),
    111: ('Fundamental Duties (Article 51A) were added by the 42nd Amendment in 1976, on the Swaran Singh Committee\'s '
          'recommendation.',
          'मूल कर्त्तव्य (अनुच्छेद 51A) स्वर्ण सिंह समिति की सिफारिश पर 42वें संशोधन द्वारा 1976 में जोड़े गए।'),
    112: ('Panchayati Raj was first set up at Nagaur, Rajasthan, on 2 October 1959, following the Balwant Rai Mehta '
          'Committee.',
          'बलवंत राय मेहता समिति के बाद पंचायती राज की स्थापना सर्वप्रथम 2 अक्टूबर 1959 को राजस्थान के नागौर में हुई।'),
    113: ('The 73rd Amendment (1992) set up three-tier rural Panchayati Raj: village (Gram), intermediate (Kshetra) and '
          'district (Zilla) panchayats. Nagar Nigams come under the 74th Amendment.',
          '73वें संशोधन (1992) ने ग्रामीण पंचायती राज की त्रिस्तरीय व्यवस्था बनाई: ग्राम, क्षेत्र और जिला पंचायत। नगर निगम 74वें संशोधन के अंतर्गत आते हैं।'),
    114: ('Under Article 248, residuary powers (subjects in none of the three lists) belong to the Union Parliament, '
          'i.e. the Centre.',
          'अनुच्छेद 248 के अनुसार अवशिष्ट शक्तियाँ (जो विषय तीनों सूचियों में नहीं हैं) संसद अर्थात् केन्द्र के पास हैं।'),
    115: ('The 2019 G-7 summit was held at Biarritz, France, in August 2019, and Prime Minister Modi attended as a '
          'special invitee.',
          '2019 का G-7 शिखर सम्मेलन अगस्त 2019 में फ्रांस के बियारिट्ज़ में हुआ, जिसमें प्रधानमंत्री मोदी विशेष आमंत्रित के रूप में शामिल हुए।'),
    116: ('In 2019 the strength of the Supreme Court was raised to 34 judges (the Chief Justice and 33 others).',
          '2019 में सर्वोच्च न्यायालय में न्यायाधीशों की संख्या बढ़ाकर 34 (मुख्य न्यायाधीश और 33 अन्य) की गई।'),
    117: ('Prime Minister Modi announced the Act East Policy at the ASEAN–India summit in Myanmar in November 2014.',
          'प्रधानमंत्री मोदी ने नवम्बर 2014 में म्यांमार में आसियान–भारत शिखर सम्मेलन में ‘एक्ट ईस्ट पॉलिसी’ की घोषणा की।'),
    118: ('Land reform laws, including the UP Zamindari Abolition and Land Reforms Act, 1950, are placed in the Ninth '
          'Schedule (added by the 1st Amendment, 1951) to protect them from challenge in court.',
          'भूमि सुधार कानून, जिनमें उत्तर प्रदेश जमींदारी उन्मूलन और भूमि सुधार अधिनियम, 1950 भी है, नवीं अनुसूची (पहला संशोधन, '
          '1951) में रखे गए हैं ताकि उन्हें न्यायालय में चुनौती से बचाया जा सके।'),
    119: ('Sir B.N. Rau was the Constitutional Adviser to the Constituent Assembly and prepared its first draft.',
          'सर बी.एन. राव संविधान सभा के संवैधानिक सलाहकार थे और उन्होंने संविधान का पहला प्रारूप तैयार किया।'),
    120: ('The Estimates Committee, with 30 members, all from the Lok Sabha, is the largest parliamentary committee.',
          'प्राक्कलन समिति, जिसके 30 सदस्य सभी लोक सभा से होते हैं, संसद की सबसे बड़ी समिति है।'),
    121: ('The Olympic motto is "Citius, Altius, Fortius" (Latin for Faster, Higher, Stronger).',
          'ओलम्पिक का आदर्श वाक्य ‘सीटियस, आल्टियस, फोर्टियस’ है (लैटिन में: और तेज, और ऊँचा, और मजबूत)।'),
    122: ('Badminton player Pullela Gopichand received the Arjuna Award in 1999.',
          'बैडमिंटन खिलाड़ी पुलेला गोपीचन्द को 1999 में अर्जुन पुरस्कार मिला।'),
    123: ('The answer key says recreation is of five types (for example physical, social, cultural, creative and '
          'mental recreation).',
          'उत्तर कुंजी के अनुसार मनोरंजन पाँच प्रकार का होता है (जैसे शारीरिक, सामाजिक, सांस्कृतिक, रचनात्मक और मानसिक मनोरंजन)।'),
    124: ('Vajrasana, sitting on folded knees, strengthens the knees and legs and aids digestion.',
          'वज्रासन (घुटनों को मोड़कर बैठना) घुटनों और पैरों को मजबूत करता है और पाचन में सहायक है।'),
    125: ('India\'s first National Sports University was set up in Imphal, Manipur, in 2018.',
          'भारत का प्रथम राष्ट्रीय खेल विश्वविद्यालय 2018 में मणिपुर के इम्फाल में स्थापित हुआ।'),
    126: ('ICPH-8, released by ICRISAT in 1991, was the world\'s first hybrid of pigeon pea (arhar).',
          'आई.सी.पी.एच.-8, जिसे इक्रीसैट ने 1991 में जारी किया, अरहर की विश्व की पहली संकर किस्म थी।'),
    127: ('Madhya Pradesh produces the most soyabean in India and is called the "Soya State".',
          'मध्य प्रदेश भारत में सबसे अधिक सोयाबीन उत्पादन करता है, इसलिए इसे ‘सोया राज्य’ कहते हैं।'),
    128: ('Growing vegetables out of season in a protected structure such as a green house is called vegetable forcing.',
          'ग्रीन हाउस जैसी संरक्षित संरचना में बेमौसम सब्जियाँ उगाना वेजीटेबल फोर्सिंग कहलाता है।'),
    129: ('The particle density of most mineral soils is about 2.65 g/cm³, close to that of quartz.',
          'अधिकांश खनिज मृदाओं का कण घनत्व लगभग 2.65 ग्राम/सेमी³ होता है, जो क्वार्ट्ज के घनत्व के निकट है।'),
    130: ('On hill slopes, orchards are planted along the contour lines, which reduces soil erosion.',
          'पहाड़ी ढलानों पर बाग समोच्च रेखाओं के अनुसार लगाए जाते हैं, जिससे मृदा अपरदन कम होता है।'),
    131: ('Vitamins and minerals are called protective nutrients because they protect the body from deficiency diseases.',
          'विटामिन और खनिज लवण सुरक्षात्मक पोषक तत्व कहलाते हैं, क्योंकि ये शरीर को कमी से होने वाले रोगों से बचाते हैं।'),
    132: ('Steaming cooks food without dipping it in water or oil, so fewer nutrients are lost. (The Hindi version of '
          'the paper translates it as "उबालना", but steaming means cooking in steam.)',
          'भाप से पकाने (स्टीमिंग) में भोजन पानी या तेल में नहीं डूबता, इसलिए पोषक तत्व कम नष्ट होते हैं। (प्रश्नपत्र के हिन्दी संस्करण '
          'में इसे ‘उबालना’ लिखा गया था, पर स्टीमिंग का अर्थ भाप से पकाना है।)'),
    133: ('Trypsin, secreted by the pancreas, digests proteins into smaller peptides.',
          'अग्नाशय से निकलने वाला ट्रिप्सिन एन्जाइम प्रोटीन को छोटे पेप्टाइडों में तोड़ता है।'),
    134: ('Smallpox (chechak) is caused by the variola virus; it was declared eradicated in 1980. The English version of '
          'the paper said "chickenpox", which is caused by a different virus, varicella-zoster.',
          'चेचक (स्मॉलपॉक्स) वेरीयोला वाइरस से होता है; 1980 में इसके उन्मूलन की घोषणा हुई। प्रश्नपत्र के अंग्रेज़ी संस्करण में '
          '"चिकनपॉक्स" लिखा था, जो अलग विषाणु (वैरीसेला-ज़ोस्टर) से होता है।'),
    135: ('Schafer\'s method is a form of artificial respiration used to revive a person rescued from drowning.',
          'शेफर विधि कृत्रिम श्वसन की एक विधि है, जिसका प्रयोग पानी में डूबे व्यक्ति को होश में लाने के लिए किया जाता है।'),
    136: ('The Brundtland Commission\'s report "Our Common Future" (1987) defined sustainable development as meeting '
          'present needs without compromising the ability of future generations to meet theirs.',
          'ब्रुटलैंड आयोग की रिपोर्ट ‘हमारा साझा भविष्य’ (1987) ने संपोषणीय विकास को ऐसा विकास बताया जो भावी पीढ़ियों की आवश्यकताओं '
          'से समझौता किए बिना वर्तमान की आवश्यकताएँ पूरी करे।'),
    137: ('The Gangetic river dolphin was declared India\'s National Aquatic Animal in 2009.',
          'गंगा की डॉल्फिन को 2009 में भारत का राष्ट्रीय जलीय जीव घोषित किया गया।'),
    138: ('The Forest (Conservation) Act was passed in 1980.', 'वन (संरक्षण) अधिनियम 1980 में पारित किया गया।'),
    139: ('Methane, carbon dioxide and ozone are greenhouse gases. Nitrogen (N₂), most of the air, does not trap heat.',
          'मिथेन, कार्बन डाई-ऑक्साइड और ओजोन हरितगृह गैसें हैं। नाइट्रोजन (N₂), जो वायु का अधिकांश भाग है, ऊष्मा नहीं रोकती।'),
    140: ('Organic manure, crop rotation and checking erosion conserve soil. Chemical pesticides harm soil organisms and '
          'are not a conservation method.',
          'जैविक खाद, फसल चक्र और अपरदन रोकना मृदा संरक्षण के उपाय हैं। रासायनिक कीटनाशक मिट्टी के जीवों को हानि पहुँचाते हैं और संरक्षण की विधि नहीं हैं।'),
    141: ('A sewing machine runs heavily mainly when it is not oiled and cleaned, so dust and dried oil clog its parts.',
          'सिलाई मशीन मुख्यतः तेल न डालने और सफाई न करने से भारी चलती है, क्योंकि धूल और सूखा तेल उसके पुर्जों को जाम कर देते हैं।'),
    142: ('Lack of calcium in old age causes osteoporosis, in which bones become weak and brittle. Rickets is the '
          'childhood disease.',
          'वृद्धावस्था में कैल्शियम की कमी से ऑस्टियोपोरोसिस होता है, जिसमें हड्डियाँ कमजोर और भुरभुरी हो जाती हैं। रिकेट्स बच्चों का रोग है।'),
    143: ('Haemoglobin is made of haem (the iron-containing part) and globin, which is the protein part.',
          'हीमोग्लोबिन हीम (लौह युक्त भाग) और ग्लोबिन से बना है; ग्लोबिन इसका प्रोटीन भाग है।'),
    144: ('The five formal steps of lesson planning come from the German educationist J.F. Herbart and are widely used '
          'in Europe and India.',
          'पाठ योजना के पंचपदी सोपान जर्मन शिक्षाशास्त्री जे.एफ. हरबर्ट की देन हैं और यूरोप तथा भारत में व्यापक रूप से प्रचलित हैं।'),
    145: ('The project method (Kilpatrick, after Dewey) is based on learning by doing.',
          'योजना (प्रोजेक्ट) विधि (किलपैट्रिक, ड्यूवी के विचारों पर) करके सीखने पर आधारित है।'),
    146: ('Pancham Sawari taal has 15 matras.', 'पंचम सवारी ताल में 15 मात्राएँ होती हैं।'),
    147: ('"Vande Mataram" was written by Bankim Chandra Chatterjee and appears in his novel "Anandamath" (1882).',
          '‘वन्दे मातरम्’ बंकिम चन्द्र चटर्जी ने लिखा, और यह उनके उपन्यास ‘आनन्दमठ’ (1882) में है।'),
    148: ('Raag Bhairav is a morning raag, sung at dawn.', 'राग भैरव प्रातःकाल का राग है, जिसे सुबह गाया जाता है।'),
    149: ('The carbon to nitrogen (C:N) ratio of normal agricultural soil is about 10:1.',
          'सामान्य कृषि मृदा में कार्बन और नाइट्रोजन (C:N) का अनुपात लगभग 10:1 होता है।'),
    150: ('Soil texture is the relative proportion of sand, silt and clay particles in a soil.',
          'मृदा कणाकार (टेक्सचर) मिट्टी में बालू, गाद और चिकनी मिट्टी के कणों का आपेक्षिक अनुपात है।'),
}
