"""UPTET 2021 Primary (cancelled exam of 28 Nov 2021), Part V (Q121–150): Environmental Studies."""

SOURCE = 'primary21'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (121, 150)
SUBJECT = 'evs'

TOPICS = {
    'evs.earth': [121, 122, 123, 127, 130, 144, 145, 146, 147, 148, 150],
    'evs.living': [124, 125, 126, 128, 129, 131, 132, 133, 149],
    'evs.society': [134, 135, 136, 137, 138, 139, 140, 141, 142, 143],
}

SKIP = {}

REPLACE = [('Great dividing rage', 'The Great Dividing Range'), ('The temperature grasslands', 'The temperate grasslands'),
           ('Tainga', 'Taiga'), ('स्टॉपीज', 'स्टेपीज'), ('Cotopaxy', 'Cotopaxi'), ('harmones', 'hormones'),
           ('Paratharmone', 'Parathormone'), ('Mucar', 'Mucor'), ('Brassiaceae', 'Brassicaceae'), ('ऐस्टेरिसो', 'ऐस्टेरेसी'),
           ('Godawari', 'Godavari'), ('Austraia', 'Australia'), ('Metur Dame', 'Mettur Dam'), ('कर नाम', 'का नाम'),
           ('का राष्ट्रीय पक्षी', 'का राज्य पक्षी'), ('भारतीय के राष्ट्रीयगान', 'भारत के राष्ट्रगान'), ('कि मोटाई', 'की मोटाई'),
           ('नाइट्रोजन स्थिरता करने वाले', 'नाइट्रोजन का स्थिरीकरण करने वाले')]

FIX = {
    134: {'en': "Who established the Indian Women's University in Mumbai in 1916 A.D.?",
          'hi': '1916 ई. में मुम्बई में भारतीय महिला विश्वविद्यालय की स्थापना किसने की थी?'},
}

EXPLAIN = {
    121: ('The Great Dividing Range runs along the east of Australia.', 'ग्रेट डिवाइडिंग रेंज ऑस्ट्रेलिया के पूर्वी भाग में फैली पर्वत श्रेणी है।'),
    122: ('The temperate grasslands of south-eastern Europe and Central Asia are called steppes.',
          'दक्षिण-पूर्वी यूरोप और मध्य एशिया के शीतोष्ण घास के मैदान स्टेपीज कहलाते हैं।'),
    123: ('Aconcagua (about 6,961 m) in the Andes of Argentina is the highest peak of South America.',
          'अर्जेंटीना के एंडीज़ में स्थित अकोंकागुआ (लगभग 6,961 मी) दक्षिण अमेरिका की सबसे ऊँची चोटी है।'),
    124: ('Euglena has chloroplasts with chlorophyll and can make its own food; Hydra, jellyfish and Sycon cannot.',
          'युग्लीना में क्लोरोफिल युक्त हरितलवक होते हैं और यह अपना भोजन बना सकता है; हाइड्रा, जेलिफ़िश और साईकान नहीं।'),
    125: ('The Sarus crane is the state bird of Uttar Pradesh.', 'सारस क्रेन उत्तर प्रदेश का राज्य पक्षी है।'),
    126: ('Parathormone from the parathyroid glands raises blood calcium; calcitonin from the thyroid lowers it.',
          'पैराथायरॉयड ग्रन्थियों से निकलने वाला पैराथार्मोन रक्त में कैल्शियम बढ़ाता है; थायरॉयड का कैल्सीटोनिन इसे घटाता है।'),
    127: ('The thickness of the ozone layer is measured in Dobson units (DU).', 'ओजोन परत की मोटाई डॉब्सन इकाई (DU) में मापी जाती है।'),
    128: ('Nitrogen-fixing Rhizobium bacteria live in the root nodules of pulses (legumes).',
          'नाइट्रोजन स्थिर करने वाले राइजोबियम जीवाणु दलहनी पौधों की जड़ ग्रन्थिकाओं में रहते हैं।'),
    129: ('Agaricus is the common edible mushroom. Puccinia causes rust, and Mucor and Rhizopus are moulds.',
          'एगेरिकस सामान्य खाने योग्य मशरूम है। पक्सीनिया गेरुई रोग फैलाता है, और म्यूकर तथा राइजोपस फफूंद हैं।'),
    130: ('Mangroves grow in coastal swamps and deltas, such as the Sundarbans in the Ganga–Brahmaputra delta.',
          'मैंग्रोव तटीय दलदलों और डेल्टाओं में उगते हैं, जैसे गंगा–ब्रह्मपुत्र डेल्टा का सुंदरवन।'),
    131: ('In flowering plants the endosperm forms from the fusion of a male gamete with two polar nuclei, so it is '
          'triploid (3n).',
          'आवृतबीजी पौधों में भ्रूणपोष एक नर युग्मक और दो ध्रुवीय केन्द्रकों के मिलने से बनता है, इसलिए यह त्रिगुणित (3n) है।'),
    132: ('The mustard family (Brassicaceae) has parietal placentation, with ovules on the inner wall of the ovary.',
          'सरसों कुल (ब्रेसिकेसी) में भित्तिलग्न बीजाण्डन्यास होता है, जिसमें बीजाण्ड अण्डाशय की भीतरी दीवार पर लगे होते हैं।'),
    133: ('Anaerobic respiration (fermentation) in yeast produces ethyl alcohol and carbon dioxide.',
          'यीस्ट में अनॉक्सी श्वसन (किण्वन) से एथिल ऐल्कोहल और कार्बन डाइऑक्साइड बनते हैं।'),
    134: ('D.K. (Dhondo Keshav) Karve founded the Indian Women\'s University (now SNDT) in 1916.',
          'डी.के. (धोंडो केशव) कर्वे ने 1916 में भारतीय महिला विश्वविद्यालय (अब SNDT) की स्थापना की।'),
    135: ('The Rath Yatra at Puri, Odisha, is the chariot festival of Lord Jagannath.', 'ओडिशा के पुरी की रथ यात्रा भगवान जगन्नाथ का रथोत्सव है।'),
    136: ('The Nashik Kumbh is held on the banks of the Godavari.', 'नासिक का कुम्भ मेला गोदावरी नदी के तट पर लगता है।'),
    137: ('"Sandhya" was a Bengali newspaper started by Brahmabandhab Upadhyay in 1904.',
          '‘संध्या’ ब्रह्मबांधव उपाध्याय द्वारा 1904 में शुरू किया गया बांग्ला अखबार था।'),
    138: ('The Uttar Pradesh Legislative Council has 100 members.', 'उत्तर प्रदेश विधान परिषद में 100 सदस्य हैं।'),
    139: ('The Flag Code of India, 2002 came into effect on 26 January 2002.', 'भारतीय ध्वज संहिता, 2002, 26 जनवरी 2002 से प्रभावी हुई।'),
    140: ('The Constituent Assembly adopted "Jana Gana Mana" as the National Anthem on 24 January 1950.',
          'संविधान सभा ने 24 जनवरी 1950 को ‘जन-गण-मन’ को राष्ट्रगान के रूप में अपनाया।'),
    141: ('Om Birla became Speaker of the 17th Lok Sabha in 2019.', 'ओम बिड़ला 2019 में सत्रहवीं लोकसभा के अध्यक्ष बने।'),
    142: ('The Inter-State Council (Article 263) is chaired by the Prime Minister.', 'अंतर-राज्यीय परिषद (अनुच्छेद 263) की अध्यक्षता प्रधानमंत्री करते हैं।'),
    143: ('Under Article 76(3), the Attorney-General has the right of audience in all courts in India.',
          'अनुच्छेद 76(3) के अनुसार महान्यायवादी को भारत के सभी न्यायालयों में सुनवाई का अधिकार है।'),
    144: ('The Ganga enters Uttar Pradesh in Bijnor district.', 'गंगा नदी बिजनौर जिले में उत्तर प्रदेश में प्रवेश करती है।'),
    145: ('Chambal, Betwa and Ken are tributaries of the Yamuna. The Gandak joins the Ganga directly.',
          'चम्बल, बेतवा और केन यमुना की सहायक नदियाँ हैं। गंडक सीधे गंगा में मिलती है।'),
    146: ('K2 (Godwin-Austen, 8,611 m), in the part of Kashmir India claims, is regarded as India\'s highest peak; '
          'Kangchenjunga is the highest within India\'s administered territory.',
          'के2 (गॉडविन-ऑस्टिन, 8,611 मी), कश्मीर के उस भाग में है जिस पर भारत दावा करता है, इसलिए इसे भारत की सबसे ऊँची चोटी माना जाता है; '
          'भारत के प्रशासनिक क्षेत्र में सबसे ऊँची कंचनजंगा है।'),
    147: ('The Kimberley plateau is in north-western Australia. Colorado is in the USA, Katanga in Africa and Patagonia '
          'in South America.',
          'किम्बर्ले पठार उत्तर-पश्चिमी ऑस्ट्रेलिया में है। कोलोरैडो अमेरिका में, कटंगा अफ्रीका में और पेटागोनिया दक्षिण अमेरिका में है।'),
    148: ('Jhansi, Lalitpur and Hamirpur lie on the Bundelkhand plateau. Mirzapur is part of the Vindhyan region.',
          'झाँसी, ललितपुर और हमीरपुर बुन्देलखंड पठार पर हैं। मिर्जापुर विंध्य क्षेत्र का भाग है।'),
    149: ('Dudhwa National Park is in Lakhimpur Kheri district of Uttar Pradesh.', 'दुधवा राष्ट्रीय उद्यान उत्तर प्रदेश के लखीमपुर खीरी जिले में है।'),
    150: ('The Mettur Dam in Tamil Nadu is built on the Kaveri.', 'तमिलनाडु का मैटूर बाँध कावेरी नदी पर बना है।'),
}
