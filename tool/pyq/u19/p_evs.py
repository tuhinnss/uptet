"""UPTET 2019 Primary, Part V (Q121–150): Environmental Studies."""

SOURCE = 'primary'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (121, 150)
SUBJECT = 'evs'

TOPICS = {
    'evs.society': [121, 122, 123, 124, 125, 130, 131, 132, 133, 134, 135, 146],
    'evs.earth': [126, 127, 128, 147, 148, 149, 150],
    'evs.living': [136, 137, 138, 139, 140, 141, 142, 143, 144, 145],
}

SKIP = {129: 'the answer key accepts two options'}

FIX = {
    123: {'options': {o: (v, f'{v} में') for o, v in zip('abcd', ['1961', '1971', '1981', '1951'])}},
    127: {'options': {'a': ('Campos', 'कैम्पोस')}},
    133: {
        'en': 'Match List-I with List-II and choose the correct code.\n'
              'List-I: A. Indian Union, B. State, C. Corporation, D. Village Panchayat\n'
              'List-II: 1. Prime Minister, 2. Sarpanch, 3. Governor, 4. Mayor',
        'hi': 'सूची–I और सूची–II का सुमेलन करते हुये सही कूट चुनें–\n'
              'सूची–I: A. भारतीय संघ, B. राज्य, C. नगर निगम, D. ग्राम पंचायत\n'
              'सूची–II: 1. प्रधानमंत्री, 2. सरपंच, 3. राज्यपाल, 4. मेयर',
        'match': ['2 3 4 1', '1 3 4 2', '3 4 1 2', '4 1 2 3'],
    },
    136: {'options': {'c': ('Cynodon dactylon (Doob grass)', 'सिनोडोन डेक्टाइलोन (दूब घास)')}},
    140: {'options': {o: (f'{v}-DNA', f'{v}-DNA') for o, v in zip('abcd', 'CBZA')}},
}

EXPLAIN = {
    121: ('India\'s first passenger train ran on 16 April 1853 from Bori Bunder (Bombay) to Thane, a distance of about '
          '34 km.',
          'भारत की पहली यात्री ट्रेन 16 अप्रैल 1853 को बोरीबंदर (बम्बई) से थाणे के बीच लगभग 34 किमी चली।'),
    122: ('The Sonepur cattle fair (Harihar Kshetra Mela) in Bihar, held on Kartik Purnima, is known as Asia\'s '
          'largest cattle fair.',
          'बिहार का सोनपुर पशु मेला (हरिहर क्षेत्र मेला), जो कार्तिक पूर्णिमा पर लगता है, एशिया का सबसे बड़ा पशु मेला माना जाता है।'),
    123: ('The National Integration Council was set up in 1961, after a conference called by Prime Minister Jawaharlal '
          'Nehru, to fight communalism, casteism and regionalism.',
          'राष्ट्रीय एकता परिषद का गठन 1961 में प्रधानमंत्री जवाहरलाल नेहरू द्वारा बुलाए गए सम्मेलन के बाद हुआ, ताकि साम्प्रदायिकता, '
          'जातिवाद और क्षेत्रवाद से निपटा जा सके।'),
    124: ('The Right to Equality is in Articles 14 to 18. Articles 19–22 cover freedom, 23–24 the right against '
          'exploitation and 25–28 freedom of religion.',
          'समता का अधिकार अनुच्छेद 14 से 18 में है। अनुच्छेद 19–22 स्वतंत्रता, 23–24 शोषण के विरुद्ध अधिकार और 25–28 धार्मिक '
          'स्वतंत्रता से सम्बन्धित हैं।'),
    125: ('The United Kingdom has an unwritten constitution that Parliament can change by ordinary law, so it is the '
          'classic flexible constitution. The USA has a rigid one; India\'s is partly rigid and partly flexible.',
          'युनाइटेड किंग्डम का संविधान अलिखित है और संसद उसे सामान्य कानून से बदल सकती है, इसलिए यह लचीले संविधान का उदाहरण है। '
          'अमेरिका का संविधान कठोर है, जबकि भारत का संविधान आंशिक रूप से कठोर और आंशिक रूप से लचीला है।'),
    126: ('Reindeer live in the cold tundra region, where people such as the Sami and the Inuit herd or hunt them.',
          'रेंडियर ठंडे टुण्ड्रा प्रदेश में पाए जाते हैं, जहाँ सामी और इनुइट जैसे लोग इन्हें पालते या इनका शिकार करते हैं।'),
    127: ('Downs (Australia), Prairies (North America) and Pampas (Argentina) are temperate grasslands. The Campos of '
          'Brazil are a tropical grassland.',
          'डाउन्स (ऑस्ट्रेलिया), प्रेयरीज़ (उत्तरी अमेरिका) और पम्पास (अर्जेंटीना) शीतोष्ण घास प्रदेश हैं। ब्राज़ील के कैम्पोस उष्णकटिबंधीय '
          'घास प्रदेश हैं।'),
    128: ('Asia is the most populous continent, with about 60% of the world\'s people.',
          'एशिया सबसे अधिक जनसंख्या वाला महाद्वीप है; विश्व की लगभग 60% जनसंख्या यहीं रहती है।'),
    130: ('The Bhilai Steel Plant, built with Soviet help in 1959, is in Durg district of Chhattisgarh.',
          'भिलाई इस्पात संयंत्र, जो 1959 में सोवियत संघ की सहायता से बना, छत्तीसगढ़ के दुर्ग जिले में है।'),
    131: ('The 73rd and 74th Amendments (1992) reserved at least one-third of seats for women in Panchayati Raj '
          'institutions and urban local bodies. (Reservation in Lok Sabha and Vidhan Sabhas came only with the 2023 '
          'Act, after this exam.)',
          '73वें और 74वें संविधान संशोधन (1992) द्वारा पंचायती राज संस्थाओं और नगरीय निकायों में महिलाओं के लिए कम से कम एक-तिहाई '
          'स्थान आरक्षित किए गए। (लोक सभा और विधान सभाओं में आरक्षण 2023 के अधिनियम से आया, जो इस परीक्षा के बाद है।)'),
    132: ('Under Article 157, a person must be a citizen of India and at least 35 years old to be appointed Governor.',
          'अनुच्छेद 157 के अनुसार राज्यपाल बनने के लिए व्यक्ति का भारत का नागरिक होना और कम से कम 35 वर्ष का होना आवश्यक है।'),
    133: ('The Prime Minister heads the Union government, the Governor is the head of a State, the Mayor heads a '
          'Municipal Corporation and the Sarpanch (Pradhan) heads a Village Panchayat. So A–1, B–3, C–4, D–2.',
          'प्रधानमंत्री संघ सरकार का, राज्यपाल राज्य का, मेयर नगर निगम का और सरपंच (प्रधान) ग्राम पंचायत का प्रमुख होता है। '
          'अतः A–1, B–3, C–4, D–2।'),
    134: ('Article 356 (President\'s Rule) was first used in Punjab in 1951. Among the options, Kerala in 1959, when the '
          'elected E.M.S. Namboodiripad government was dismissed, is the case the answer key accepts.',
          'अनुच्छेद 356 (राष्ट्रपति शासन) का पहला प्रयोग 1951 में पंजाब में हुआ था। दिए गए विकल्पों में उत्तर कुंजी केरल 1959 को सही '
          'मानती है, जब ई.एम.एस. नम्बूदिरीपाद की निर्वाचित सरकार को बर्खास्त किया गया था।'),
    135: ('A Municipal Corporation can levy house (property) tax, toll or octroi and entertainment tax under state law, '
          'so all the options are correct.',
          'राज्य कानून के अंतर्गत नगर निगम गृह कर, चुंगी कर और मनोरंजन कर लगा सकता है, इसलिए सभी विकल्प सही हैं।'),
    136: ('Water hyacinth (Eichhornia crassipes) spreads fast over ponds and lakes, blocking light and oxygen, and is '
          'called the "Terror of Bengal".',
          'जलकुम्भी (आइकॉर्निया क्रैसिपीज़) तालाबों और झीलों पर तेजी से फैलकर प्रकाश और ऑक्सीजन रोक देती है, इसलिए इसे '
          '‘बंगाल का आतंक’ कहते हैं।'),
    137: ('Outside a host cell a virus is inert and can be crystallised like a chemical (W.M. Stanley crystallised the '
          'tobacco mosaic virus). This is its non-living property; viruses do contain protein and DNA or RNA.',
          'पोषी कोशिका के बाहर वाइरस निष्क्रिय रहता है और रसायन की तरह क्रिस्टल बनाया जा सकता है (डब्ल्यू.एम. स्टैनली ने तम्बाकू '
          'मोज़ेक वाइरस को क्रिस्टलीकृत किया)। यही इसका अजैविक लक्षण है; वाइरस में प्रोटीन और DNA या RNA होता है।'),
    138: ('Ethylene is a gaseous plant hormone that speeds up the ripening of fruits.',
          'इथाइलीन एक गैसीय पादप हार्मोन है जो फलों के पकने की क्रिया को तेज करता है।'),
    139: ('Clostridium is a free-living, anaerobic, nitrogen-fixing soil bacterium. Azotobacter is free-living but '
          'aerobic, and Rhizobium lives in root nodules of legumes.',
          'क्लॉस्ट्रिडियम मिट्टी में स्वतंत्र रूप से रहने वाला अवायवीय, नाइट्रोजन स्थिर करने वाला जीवाणु है। एजोटोबैक्टर स्वतंत्र '
          'रहता है पर वायवीय है, और राइजोबियम दलहनी पौधों की जड़ ग्रन्थिकाओं में रहता है।'),
    140: ('B-DNA, the right-handed double helix described by Watson and Crick, is the common form of DNA in cells.',
          'वाटसन और क्रिक द्वारा बताया गया दक्षिणावर्ती द्विकुण्डली B-DNA ही कोशिकाओं में सामान्य रूप से पाया जाता है।'),
    141: ('Euplectella (Venus\'s flower basket) is a sponge that stays fixed to the sea floor, so it is sessile. Leech, '
          'chiton and Echinus can move.',
          'यूप्लेक्टेला (वीनस का फूलदान) एक स्पंज है जो समुद्र तल से चिपका रहता है, इसलिए यह अचल है। लीच, काइटन और इकाइनस चल सकते हैं।'),
    142: ('Proteins are long chains of amino acids joined by peptide bonds.',
          'प्रोटीन अमीनो अम्लों की लम्बी शृंखलाएँ हैं, जो पेप्टाइड बन्ध से जुड़ी होती हैं।'),
    143: ('The centrosome (with centrioles) is found in animal cells but absent in most plant cells. Plastids, large '
          'vacuoles and a cellulose cell wall are features of plant cells.',
          'तारककाय (सेंट्रोसोम) जन्तु कोशिका में होता है पर अधिकांश पादप कोशिकाओं में नहीं। लवक, बड़ी रिक्तिका और सेल्यूलोस '
          'कोशिका भित्ति पादप कोशिका की विशेषताएँ हैं।'),
    144: ('The liver is the largest gland of the human body; it secretes bile.',
          'यकृत मानव शरीर की सबसे बड़ी ग्रन्थि है; यह पित्त का स्राव करता है।'),
    145: ('The Sarus crane is the state bird of Uttar Pradesh; it is the world\'s tallest flying bird.',
          'सारस क्रेन उत्तर प्रदेश का राज्य पक्षी है; यह विश्व का सबसे ऊँचा उड़ने वाला पक्षी है।'),
    146: ('A hamlet (purva) is a small cluster of houses lying apart from the main village, so it is a type of rural '
          'settlement.',
          'पुरवा (हैमलेट) मुख्य गाँव से अलग बसे कुछ घरों का छोटा समूह है, इसलिए यह ग्रामीण अधिवास का एक प्रकार है।'),
    147: ('Kilimanjaro in Tanzania is a dormant volcano and Africa\'s highest peak. The Urals, Appalachians and Aravallis '
          'are old fold mountains.',
          'तंजानिया का किलिमंजारो एक प्रसुप्त ज्वालामुखी और अफ्रीका की सबसे ऊँची चोटी है। यूराल, अप्लेशियन और अरावली पुराने वलित पर्वत हैं।'),
    148: ('Elephanta Island, known for its rock-cut cave temples, is in the harbour off the Mumbai coast.',
          'ऐलीफेण्टा द्वीप, जो अपनी शैलकृत गुफाओं के लिए प्रसिद्ध है, मुम्बई तट के पास बन्दरगाह में स्थित है।'),
    149: ('Tropical deciduous (monsoon) forests grow where annual rainfall is about 70 to 200 cm.',
          'उष्णकटिबंधीय पर्णपाती (मानसूनी) वन उन क्षेत्रों में मिलते हैं जहाँ वार्षिक वर्षा लगभग 70 से 200 सेमी होती है।'),
    150: ('The Karbi Anglong plateau in Assam, like the Meghalaya plateau, is an extension of the Peninsular plateau, '
          'separated from it by the Malda gap.',
          'असम का कार्बी ऐंगलोंग पठार, मेघालय पठार की तरह, प्रायद्वीपीय पठार का विस्तार है, जो मालदा भ्रंश द्वारा उससे अलग हुआ है।'),
}
