"""UPTET 2021 Junior (23 Jan 2022), Part IV (Q91–150): Social Studies and other subjects."""

SOURCE = 'junior_ss21'
ID_PREFIX = 'jss'
PAPER_LABEL = 'Junior level paper, Social Studies option'
RANGE = (91, 150)
SUBJECT = 'sst'

TOPICS = {
    'sst.geography': [91, 92, 93, 94, 95, 101, 102, 103, 113, 114, 115],
    'sst.civics': [96, 97, 98, 99, 100, 131, 132, 133, 134, 135],
    'sst.history': [106, 107, 108, 109, 110, 116, 117, 118, 119, 120],
    'sst.pedagogy': [105, 111, 112],
    'sst.other': [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145,
                  146, 147, 148, 149, 150],
}

SKIP = {104: 'the answer key accepts no single option'}

REPLACE = [('is associate with fault', 'is associated with a fault'), ('tropicana desert', 'tropical desert'),
           ('Directive Principles related', 'Directive Principles is related'), ('In whose region', 'In whose reign'),
           ('With which Gayald', 'With which gayaki is'), ('Gajanavi', 'Ghaznavi'), ('Fathehpur', 'Fatehpur'),
           ('Bitthore', 'Bithoor'), ('Barrack-pore', 'Barrackpore'), ('marmalad making', 'marmalade making'),
           ('Golakh Nath', 'Golak Nath'), ('Keshwanand Bharti', 'Kesavananda Bharati'), ('On which day in', 'On which day is'),
           ('In which clothes are resin starch used?', 'In which clothes is gum starch used?'),
           ('When "Sports Day" is celebrated?', 'When is National Sports Day celebrated?'), ('Pluto', 'Plato'),
           ('India has divided in how many', 'India has been divided into how many'), ('Shrutees', 'shrutis'),
           ('swaraas', 'swaras'), ('ज्यामितीय आकरों', 'ज्यामितीय आकारों'), ('पुष्प वर्तिका से', 'पुष्प वर्तिकाग्र से')]

FIX = {}

EXPLAIN = {
    91: ('The Bhilai Steel Plant is in Durg district of Chhattisgarh.', 'भिलाई इस्पात कारखाना छत्तीसगढ़ के दुर्ग जिले में है।'),
    92: ('Shale forms from layers of mud and clay, so it is sedimentary. Marble and slate are metamorphic, granite igneous.',
         'शैल (शेल) मिट्टी और चिकनी मिट्टी की परतों से बनती है, इसलिए अवसादी है। संगमरमर और स्लेट रूपान्तरित, ग्रेनाइट आग्नेय शैल है।'),
    93: ('The solar wind and radiation pressure push a comet\'s tail away from the Sun.',
         'सौर पवन और विकिरण दाब के कारण धूमकेतु की पूँछ सदैव सूर्य से दूर की ओर रहती है।'),
    94: ('A graben is a block that has sunk between two faults, forming a rift valley.',
         'ग्राबेन दो भ्रंशों के बीच नीचे धँसा हुआ भूखण्ड है, जिससे भ्रंश घाटी बनती है।'),
    95: ('The Gobi is a cold, mid-latitude desert. The Arabian, Atacama and Kalahari are tropical deserts.',
         'गोबी मध्य अक्षांशों का ठंडा मरुस्थल है। अरब, अटाकामा और कालाहारी उष्णकटिबंधीय मरुस्थल हैं।'),
    96: ('Fundamental Rights are in Part III (Articles 12–35).', 'मौलिक अधिकार संविधान के भाग III (अनुच्छेद 12–35) में हैं।'),
    97: ('The 73rd Amendment (1992) gave constitutional status to Panchayati Raj.', '73वें संशोधन (1992) ने पंचायती राज को संवैधानिक दर्जा दिया।'),
    98: ('The International Court of Justice sits at the Peace Palace in The Hague, Netherlands.',
         'अन्तर्राष्ट्रीय न्यायालय नीदरलैंड के द हेग में पीस पैलेस में स्थित है।'),
    99: ('Population control and family planning was added to the Concurrent List by the 42nd Amendment (1976).',
         'जनसंख्या नियंत्रण और परिवार नियोजन को 42वें संशोधन (1976) द्वारा समवर्ती सूची में जोड़ा गया।'),
    100: ('Article 51 directs the State to promote international peace and security, which concerns foreign policy.',
          'अनुच्छेद 51 राज्य को अन्तर्राष्ट्रीय शांति और सुरक्षा बढ़ाने का निर्देश देता है, जो विदेश नीति से सम्बन्धित है।'),
    101: ('Normally temperature falls with height; in an inversion it rises with height instead.',
          'सामान्यतः ऊँचाई के साथ तापमान घटता है; तापक्रम विलोमता में ऊँचाई के साथ तापमान बढ़ता है।'),
    102: ('The Rihand Dam (Sonbhadra, UP) forms the Govind Ballabh Pant Sagar reservoir.',
          'रिहन्द बाँध (सोनभद्र, उत्तर प्रदेश) से गोविन्द वल्लभ पंत सागर जलाशय बना है।'),
    103: ('Shipki La, through which the Satluj enters India, is in Himachal Pradesh.', 'शिपकी ला दर्रा, जहाँ से सतलुज भारत में आती है, हिमाचल प्रदेश में है।'),
    105: ('Maps are the most useful aid for teaching geography.', 'भूगोल शिक्षण के लिए मानचित्र सबसे उपयोगी सहायक सामग्री है।'),
    106: ('The Sanskrit grammar "Ashtadhyayi" was written by Panini.', 'संस्कृत व्याकरण ग्रन्थ ‘अष्टाध्यायी’ पाणिनि ने लिखा।'),
    107: ('The Second Buddhist Council was held at Vaishali about 383 BCE under King Kalashoka.',
          'द्वितीय बौद्ध संगीति लगभग 383 ई.पू. में वैशाली में राजा कालाशोक के समय हुई।'),
    108: ('Akbar built the Ibadat Khana (house of worship) at Fatehpur Sikri in 1575.', 'अकबर ने 1575 में फतेहपुर सीकरी में इबादत खाना बनवाया।'),
    109: ('Swami Dayanand Saraswati founded the Arya Samaj in Bombay in 1875.', 'स्वामी दयानन्द सरस्वती ने 1875 में बम्बई में आर्य समाज की स्थापना की।'),
    110: ('Ram Prasad Bismil, Ashfaqullah Khan and Rajendra Lahiri were in the Kakori case (1925). Surya Sen led the '
          'Chittagong armoury raid.',
          'रामप्रसाद बिस्मिल, अशफाकउल्ला खाँ और राजेन्द्र लाहिड़ी काकोरी कांड (1925) से जुड़े थे। सूर्य सेन ने चटगाँव शस्त्रागार कांड का नेतृत्व किया।'),
    111: ('Flat maps distort area and shape; a globe shows the true proportions of continents.',
          'समतल मानचित्र क्षेत्र और आकार को विकृत करते हैं; ग्लोब महाद्वीपों का सही अनुपात दिखाता है।'),
    112: ('The answer key gives the tour (field trip) method, which lets pupils observe geography directly.',
          'उत्तर कुंजी भ्रमण विधि को उपयुक्त मानती है, जिसमें छात्र भौगोलिक तथ्यों को प्रत्यक्ष देखते हैं।'),
    113: ('Conventional signs and symbols form the common language of maps everywhere.', 'रूढ़ चिह्न (परम्परागत संकेत) मानचित्र की सर्वमान्य भाषा हैं।'),
    114: ('Glaciers carve U-shaped valleys; rivers carve V-shaped ones.', 'हिमनदी U-आकार की और नदी V-आकार की घाटी बनाती है।'),
    115: ('Canberra is the capital of Australia.', 'कैनबरा ऑस्ट्रेलिया की राजधानी है।'),
    116: ('Akbar started Din-i-Ilahi in 1582.', 'अकबर ने 1582 में दीन-ए-इलाही की शुरुआत की।'),
    117: ('Hsuan-tsang visited India in the reign of Harshavardhana (7th century).', 'ह्वेन सांग हर्षवर्धन के शासनकाल (7वीं शताब्दी) में भारत आया।'),
    118: ('Babur was called "Qalandar" for his generosity.', 'बाबर को उसकी उदारता के कारण ‘कलन्दर’ कहा जाता था।'),
    119: ('Lord Curzon partitioned Bengal in 1905.', 'लॉर्ड कर्जन ने 1905 में बंगाल का विभाजन किया।'),
    120: ('Kunwar Singh, a leader of the 1857 revolt, was the zamindar of Jagdishpur in Bihar.',
          '1857 की क्रांति के नायक कुँवर सिंह बिहार के जगदीशपुर के जमींदार थे।'),
    121: ('Hindustani music has 7 shuddha and 5 vikrit swaras, 12 in all.', 'हिन्दुस्तानी संगीत में 7 शुद्ध और 5 विकृत, कुल 12 स्वर होते हैं।'),
    122: ('Chautal (Char taal) accompanies Dhrupad singing; Dhamar taal goes with Dhamar.', 'चौताल (चार ताल) ध्रुपद गायकी के साथ बजाया जाता है।'),
    123: ('Zakir Hussain, Pt. Kishan Maharaj and Ahmed Jan Thirakwa are tabla players; the answer key says Ram Das '
          'Sharma is not.',
          'ज़ाकिर हुसैन, पं. किशन महाराज और अहमद जान थिरकवा तबला वादक हैं; उत्तर कुंजी के अनुसार राम दास शर्मा तबला वादक नहीं हैं।'),
    124: ('The answer key gives Mumbai. Some sources place the first edition, then called the Indian Olympic Games, in '
          'Lahore in 1924, so this answer may be disputed.',
          'उत्तर कुंजी मुम्बई को सही मानती है। कुछ स्रोत पहले आयोजन (तब ‘इंडियन ओलम्पिक गेम्स’) को 1924 में लाहौर में बताते हैं, '
          'इसलिए यह उत्तर विवादित हो सकता है।'),
    125: ('Swami Vivekananda urged youth to build strength first, saying they would be nearer heaven through football '
          'than through the Gita.',
          'स्वामी विवेकानन्द ने युवाओं को पहले शक्ति अर्जित करने को कहा और फुटबाल के मैदान की आवश्यकता बताई।'),
    126: ('Seed multiplication goes nucleus → breeder → foundation → certified seed.', 'बीज गुणन का क्रम है: केन्द्रिक → प्रजनक → आधारीय → प्रमाणित बीज।'),
    127: ('CIMAP (Central Institute of Medicinal and Aromatic Plants) is in Lucknow.', 'केन्द्रीय औषधीय एवं सगंध पौधा संस्थान (CIMAP) लखनऊ में है।'),
    128: ('Marmalade is made from citrus fruits such as malta (sweet orange).', 'मार्मलेड खट्टे-मीठे नींबू वर्गीय फलों जैसे माल्टा से बनता है।'),
    129: ('CFTRI is in Mysuru, Karnataka.', 'केन्द्रीय खाद्य प्रौद्योगिकी अनुसंधान संस्थान (CFTRI) कर्नाटक के मैसूरु में है।'),
    130: ('The high sugar concentration in jelly acts as the preservative.', 'जैली में शर्करा की अधिक सांद्रता ही परिरक्षक का काम करती है।'),
    131: ('The Community Development Programme began on 2 October 1952.', 'सामुदायिक विकास कार्यक्रम 2 अक्टूबर 1952 को शुरू हुआ।'),
    132: ('The basic structure doctrine was laid down in Kesavananda Bharati v. State of Kerala (1973).',
          'बुनियादी ढाँचे का सिद्धान्त केशवानंद भारती बनाम केरल राज्य (1973) में दिया गया।'),
    133: ('Under Article 200 a Governor may reserve a bill for the President\'s consideration.',
          'अनुच्छेद 200 के अंतर्गत राज्यपाल किसी विधेयक को राष्ट्रपति के विचार के लिए सुरक्षित रख सकता है।'),
    134: ('Under Article 66, all members (elected and nominated) of both Houses of Parliament elect the Vice-President.',
          'अनुच्छेद 66 के अनुसार उपराष्ट्रपति का निर्वाचन संसद के दोनों सदनों के सभी (निर्वाचित और मनोनीत) सदस्य करते हैं।'),
    135: ('Japan is not a member of SAARC; Nepal, Bhutan and Bangladesh are.', 'जापान दक्षेस का सदस्य नहीं है; नेपाल, भूटान और बांग्लादेश हैं।'),
    136: ('Saffron is the dried stigma of the Crocus flower.', 'केसर क्रोकस पुष्प के सूखे वर्तिकाग्र से प्राप्त होता है।'),
    137: ('The human body has 12 pairs, i.e. 24 ribs.', 'मानव शरीर में 12 जोड़ी अर्थात् 24 पसलियाँ होती हैं।'),
    138: ('The TAB vaccine protects against typhoid and paratyphoid A and B.', 'टी.ए.बी. टीका टाइफाइड (मियादी बुखार) और पैराटाइफाइड A व B से बचाता है।'),
    139: ('International Yoga Day is celebrated on 21 June.', 'अंतर्राष्ट्रीय योग दिवस 21 जून को मनाया जाता है।'),
    140: ('Gum starch is used to stiffen silk clothes.', 'रेशमी वस्त्रों में गोंद का कलफ लगाया जाता है।'),
    141: ('National Sports Day is 29 August, the birthday of hockey player Major Dhyan Chand.',
          'राष्ट्रीय खेल दिवस 29 अगस्त को हॉकी खिलाड़ी मेजर ध्यानचंद के जन्मदिन पर मनाया जाता है।'),
    142: ('The Yoga Sutra (Yog Darshan) was written by Maharshi Patanjali.', '‘योग दर्शन’ (योगसूत्र) महर्षि पतंजलि ने लिखा।'),
    143: ('Zein is the main protein of maize.', 'ज़ीइन मक्का का प्रमुख प्रोटीन है।'),
    144: ('Tharparkar cattle are used both for milk and for draught work, so they are dual-purpose.',
          'थारपारकर नस्ल दूध और भार ढोने, दोनों कामों के लिए उपयोगी है, इसलिए दुकाजी है।'),
    145: ('The Planning Commission divided India into 15 agro-climatic zones.', 'योजना आयोग ने भारत को 15 कृषि जलवायु क्षेत्रों में बाँटा।'),
    146: ('"Rajput Painting" (1916) was written by Ananda K. Coomaraswamy.', '‘राजपूत पेंटिंग’ (1916) आनन्द के. कुमारस्वामी की पुस्तक है।'),
    147: ('Folk art is the traditional art of a region and its people.', 'लोक कला किसी क्षेत्र और वहाँ के लोगों की पारम्परिक कला है।'),
    148: ('A geometrical design is a design made from geometrical shapes.', 'ज्यामितीय डिज़ाइन ज्यामितीय आकारों से बनी आकृति है।'),
    149: ('Aipan is the traditional floor and wall art of Kumaon, Uttarakhand.', 'ऐपण उत्तराखण्ड के कुमाऊँ क्षेत्र की पारम्परिक भित्ति और भूमि अलंकरण कला है।'),
    150: ('Hindustani music recognises 22 shrutis.', 'हिन्दुस्तानी संगीत में 22 श्रुतियाँ मानी गई हैं।'),
}
