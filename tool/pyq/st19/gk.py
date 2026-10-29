"""Super TET 2019, Q41–50: General Knowledge."""

RANGE = (41, 50)
LANGUAGE = None

TOPICS = {
    'gk.history': [41, 42, 49],
    'gk.polity': [43, 47, 48],
    'gk.geography': [44, 45, 46, 50],
}

SKIP = {}

FIX = {}

EXPLAIN = {
    41: ('Badruddin Tyabji presided over the third session of the Indian National Congress at Madras in 1887 and '
         'was its first Muslim president. Abul Kalam Azad presided later, in 1923 and 1940.',
         'बदरुद्दीन तैयबजी 1887 में मद्रास में हुए कांग्रेस के तीसरे अधिवेशन के अध्यक्ष बने और कांग्रेस के पहले मुस्लिम अध्यक्ष थे। '
         'मौलाना अबुल कलाम आज़ाद बाद में 1923 और 1940 में अध्यक्ष बने।'),
    42: ('Lala Lajpat Rai led a protest against the Simon Commission in Lahore on 30 October 1928. He was badly '
         'injured in a police lathi charge and died on 17 November 1928.',
         'लाला लाजपत राय ने 30 अक्टूबर 1928 को लाहौर में साइमन कमीशन के विरोध में प्रदर्शन का नेतृत्व किया। पुलिस के लाठी चार्ज '
         'में वे गंभीर रूप से घायल हुए और 17 नवंबर 1928 को उनकी मृत्यु हो गई।'),
    43: ('Under Article 109 of the Constitution, the Rajya Sabha must return a Money Bill, with or without '
         'recommendations, within 14 days. If it does not, the bill is deemed passed by both Houses.',
         'संविधान के अनुच्छेद 109 के अनुसार राज्य सभा को धन विधेयक 14 दिनों के भीतर सिफ़ारिशों सहित या बिना लौटाना होता है। '
         'ऐसा न करने पर विधेयक दोनों सदनों से पारित माना जाता है।'),
    44: ('Kanyakumari lies at about 8°N latitude. That is south of the Tropic of Cancer (23½°N) but still north of '
         'the Equator. India’s southernmost point overall, Indira Point in the Nicobar Islands, is also north of '
         'the Equator.',
         'कन्याकुमारी लगभग 8° उत्तरी अक्षांश पर है, यानी कर्क रेखा (23½° उ.) के दक्षिण में पर भूमध्य रेखा के उत्तर में। '
         'भारत का सबसे दक्षिणी बिन्दु इंदिरा पॉइंट (निकोबार) भी भूमध्य रेखा के उत्तर में है।'),
    45: ('The Agulhas Current is a warm current of the Indian Ocean that flows south along the east coast of Africa. '
         'The Labrador, Florida and Canary currents are all in the Atlantic Ocean.',
         'अगुलहास धारा हिन्द महासागर की गर्म धारा है जो अफ्रीका के पूर्वी तट के साथ दक्षिण की ओर बहती है। '
         'लेब्राडोर, फ्लोरिडा और कनारी धाराएँ अटलांटिक महासागर की हैं।'),
    46: ('Nathu La is a pass in the Himalayas in Sikkim, on the border with Tibet (China). It was reopened for '
         'trade in 2006 and is a route for the Kailash Mansarovar Yatra.',
         'नाथूला दर्रा सिक्किम में भारत-तिब्बत (चीन) सीमा पर है। 2006 में इसे व्यापार के लिए फिर खोला गया और '
         'कैलाश मानसरोवर यात्रा का एक मार्ग यहीं से जाता है।'),
    47: ('Poverty in India is measured from household consumption expenditure (monthly per capita consumption '
         'expenditure) collected in NSSO surveys and compared with a poverty line, not from income.',
         'भारत में गरीबी का आकलन आय से नहीं, बल्कि राष्ट्रीय प्रतिदर्श सर्वेक्षण (NSSO) से प्राप्त परिवार के उपभोग व्यय '
         '(मासिक प्रति व्यक्ति उपभोग व्यय) की तुलना गरीबी रेखा से करके किया जाता है।'),
    48: ('At the first sitting of the Constituent Assembly on 9 December 1946, Dr Sachchidananda Sinha, the oldest '
         'member, was its temporary (provisional) president. Dr Rajendra Prasad was elected permanent president on '
         '11 December 1946. The key takes “first president” to mean Sinha; some sources call Prasad the first '
         'president, so this answer may be disputed.',
         '9 दिसंबर 1946 को संविधान सभा की पहली बैठक में सबसे वरिष्ठ सदस्य डॉ० सच्चिदानंद सिन्हा अस्थायी अध्यक्ष बने। '
         '11 दिसंबर 1946 को डॉ० राजेन्द्र प्रसाद स्थायी अध्यक्ष चुने गए। उत्तरमाला ‘पहले अध्यक्ष’ के रूप में सिन्हा को मानती है; '
         'कुछ स्रोत राजेन्द्र प्रसाद को पहला अध्यक्ष कहते हैं, इसलिए यह उत्तर विवादित हो सकता है।'),
    49: ('The Kakori train robbery took place on 9 August 1925, when revolutionaries of the Hindustan Republican '
         'Association looted government money from a train near Kakori, Lucknow. Ram Prasad Bismil, Ashfaqulla '
         'Khan, Rajendra Lahiri and Roshan Singh were later hanged.',
         'काकोरी कांड 9 अगस्त 1925 को हुआ, जब हिंदुस्तान रिपब्लिकन एसोसिएशन के क्रांतिकारियों ने लखनऊ के पास काकोरी में ट्रेन से '
         'सरकारी खजाना लूटा। बाद में राम प्रसाद बिस्मिल, अशफ़ाक़उल्ला ख़ाँ, राजेन्द्र लाहिड़ी और रोशन सिंह को फाँसी दी गई।'),
    50: ('Jim Corbett National Park in Uttarakhand was set up in 1936 as Hailey National Park, India’s first '
         'national park. It was renamed after the hunter-naturalist Jim Corbett in 1956.',
         'उत्तराखण्ड का जिम कॉर्बेट राष्ट्रीय उद्यान 1936 में ‘हेली नेशनल पार्क’ नाम से बना और भारत का पहला राष्ट्रीय उद्यान है। '
         '1956 में इसका नाम जिम कॉर्बेट के नाम पर रखा गया।'),
}
