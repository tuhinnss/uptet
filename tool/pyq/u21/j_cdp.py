"""UPTET 2021 Junior (23 Jan 2022), Part I (Q1–30): Child Development and Pedagogy."""

SOURCE = 'junior_ss21'
ID_PREFIX = 'j'
PAPER_LABEL = 'Junior level paper'
RANGE = (1, 30)
SUBJECT = 'cdp'

TOPICS = {
    'cdp.theories': [1, 5, 8, 10, 12, 28, 29],
    'cdp.development': [3, 9, 16, 30],
    'cdp.learning': [11, 13, 18, 19, 20, 24],
    'cdp.assessment': [4, 7, 14, 15, 17, 21, 23, 25, 26, 27],
    'cdp.inclusive': [2, 6, 22],
}

SKIP = {}

REPLACE = [('Purpose of T.E.T. is measure', 'The purpose of T.E.T. is to measure'), ('explain which', 'explains which'),
           ('is not ductless glands', 'is not a ductless gland'), ('learing curve', 'learning curve'),
           ('to measue', 'to measure'), ('Aptiutude', 'Aptitude'), ("Ravan's test", "Raven's test"),
           ('learner content', 'learnt content'), ('Gorden', 'Gordon'), ('मंे', 'में'), ('स्किन्नर', 'स्किनर'),
           ('आगनात्मक', 'आगमनात्मक'), ('थॉयराइड', 'थायरॉयड')]

FIX = {
    12: {'options': {'b': (None, 'सामाजिक अधिगम सिद्धान्त')}},
    17: {'options': {
        'a': ('C.A. / M.A.', 'वास्तविक आयु / मानसिक आयु'),
        'b': ('(M.A. / C.A.) × 100', '(मानसिक आयु / वास्तविक आयु) × 100'),
        'c': ('(C.A. / M.A.) × 100', '(वास्तविक आयु / मानसिक आयु) × 100'),
        'd': ('M.A. / (C.A. × 100)', 'मानसिक आयु / (वास्तविक आयु × 100)'),
    }},
    27: {'en': 'The median of 7, 8, 9, 10, 11, 12 is:', 'hi': '7, 8, 9, 10, 11, 12 का मध्यांक है–'},
    29: {'options': {'d': (None, 'चिन्तन')}},
}

EXPLAIN = {
    1: ('Instincts are inborn, natural tendencies found in all living beings, not only in some.',
        'मूल प्रवृत्तियाँ जन्मजात और प्राकृतिक होती हैं तथा सभी प्राणियों में पाई जाती हैं।'),
    2: ('The 86th Amendment (2002) added Article 21A, making free and compulsory education for children aged 6–14 a '
        'fundamental right.',
        '86वें संशोधन (2002) ने अनुच्छेद 21A जोड़ा, जिससे 6–14 वर्ष के बच्चों की निःशुल्क और अनिवार्य शिक्षा मौलिक अधिकार बनी।'),
    3: ('Kretschmer classified people by build into pyknic (stout), athletic and asthenic (lean) types, so all of these.',
        'क्रेशमर ने शारीरिक बनावट के आधार पर व्यक्तियों को गोलकाय (पिकनिक), सुडौलकाय और लम्बकाय, तीनों प्रकारों में बाँटा।'),
    4: ('A teacher eligibility test checks a candidate\'s aptitude, the potential to become a good teacher.',
        'शिक्षक पात्रता परीक्षा अभ्यर्थी की शिक्षण अभिक्षमता, यानी अच्छा शिक्षक बनने की क्षमता, मापती है।'),
    5: ('Consolidation theory explains memory: a new memory trace becomes stable over time after learning.',
        'संघनन (समेकन) का सिद्धान्त स्मृति की व्याख्या करता है: सीखने के बाद स्मृति चिह्न समय के साथ स्थिर होते हैं।'),
    6: ('The answer key credits Cyril Burt, who studied backward children, with the concept of the educational quotient.',
        'उत्तर कुंजी के अनुसार पिछड़े बालकों के लिए शैक्षिक लब्धि की अवधारणा सिरिल बर्ट ने दी, जिन्होंने पिछड़े बालकों का अध्ययन किया।'),
    7: ('A good test must be valid, reliable and objective. Aptitude is a trait that tests measure, not a quality of a test.',
        'उत्तम परीक्षण वैध, विश्वसनीय और वस्तुनिष्ठ होना चाहिए। अभिक्षमता मापी जाने वाली योग्यता है, परीक्षण की विशेषता नहीं।'),
    8: ('Unifactor, two-factor and multifactor theories explain intelligence. Regression is a statistical idea, not a '
        'theory of intelligence.',
        'एक तत्व, द्वि तत्व और बहुतत्व सिद्धांत बुद्धि की व्याख्या करते हैं। प्रत्यागमन (रिग्रेशन) सांख्यिकी की अवधारणा है, बुद्धि का सिद्धांत नहीं।'),
    9: ('Salivary glands pour saliva through ducts, so they are not ductless (endocrine). Pituitary, adrenal and thyroid '
        'are endocrine glands.',
        'लार ग्रन्थियाँ नलिकाओं से लार छोड़ती हैं, इसलिए ये अन्तःस्रावी नहीं हैं। पीयूष, एड्रिनल और थायरॉयड अन्तःस्रावी ग्रन्थियाँ हैं।'),
    10: ('Piaget\'s stages are sensorimotor, pre-operational, concrete operational and formal operational; the second is '
         'pre-operational.',
         'पियाजे की अवस्थाएँ हैं: संवेदी-गामक, पूर्व-संक्रियात्मक, मूर्त संक्रियात्मक और औपचारिक संक्रियात्मक; दूसरी पूर्व-संक्रियात्मक है।'),
    11: ('Introspection, looking into one\'s own mind, depends entirely on the person, so it is the most subjective method.',
         'अन्तर्दर्शन, यानी अपने ही मन का निरीक्षण, पूरी तरह व्यक्ति पर निर्भर है, इसलिए यह सबसे व्यक्तिनिष्ठ विधि है।'),
    12: ('Albert Bandura gave the social learning theory: children learn by observing and imitating models.',
         'एल्बर्ट बण्डूरा ने सामाजिक अधिगम सिद्धान्त दिया: बच्चे दूसरों को देखकर और उनका अनुकरण करके सीखते हैं।'),
    13: ('The answer key gives fatigue: tiredness and loss of interest can stall progress for a while, producing a '
         'plateau in the learning curve.',
         'उत्तर कुंजी के अनुसार थकान से कुछ समय के लिए प्रगति रुक जाती है, जिससे अधिगम वक्र में पठार बनता है।'),
    14: ('The mirror drawing test is used to study transfer of learning, for example from one hand to the other.',
         'दर्पण चित्र परीक्षण अधिगम अन्तरण (जैसे एक हाथ से दूसरे हाथ में) के अध्ययन के लिए प्रयुक्त होता है।'),
    15: ('The Cloud Picture Test is a projective test of personality.', 'क्लाउड पिक्चर परीक्षण व्यक्तित्व मापन का प्रक्षेपी परीक्षण है।'),
    16: ('Physical development is affected by heredity, environment and sports and exercise.',
         'शारीरिक विकास पर वंशानुक्रम, वातावरण और खेल तथा व्यायाम, सभी का प्रभाव पड़ता है।'),
    17: ('IQ = (mental age ÷ chronological age) × 100.', 'बुद्धि लब्धि = (मानसिक आयु ÷ वास्तविक आयु) × 100।'),
    18: ('John Dewey described reflective thinking in "How We Think" (1910).', 'जॉन डीवी ने ‘हाउ वी थिंक’ (1910) में विचारात्मक चिन्तन की चर्चा की।'),
    19: ('Inductive reasoning moves through observation, experiment and generalisation. Imagination is not one of its steps.',
         'आगमनात्मक तर्क में अवलोकन, प्रयोग और सामान्यीकरण के चरण होते हैं; कल्पना इसका चरण नहीं है।'),
    20: ('Failing to retain or recall what was learnt is forgetting.', 'सीखी गई बात को धारण या पुनः स्मरण न कर पाना विस्मरण है।'),
    21: ('IQ = (8 ÷ 5) × 100 = 160.', 'बुद्धि लब्धि = (8 ÷ 5) × 100 = 160।'),
    22: ('Children with IQ of about 35–49 are classed as trainable; 50–69 as educable.', 'लगभग 35–49 बुद्धि लब्धि वाले बच्चे प्रशिक्षण योग्य और 50–69 वाले शिक्षण योग्य माने जाते हैं।'),
    23: ('The Rorschach ink-blot test is a projective test of personality.', 'रोर्शा स्याही-धब्बा परीक्षण व्यक्तित्व का प्रक्षेपी परीक्षण है।'),
    24: ('A desire to remember helps memory. Too little learning, mental conflict and faulty methods cause forgetting.',
         'स्मरण करने की इच्छा स्मृति में सहायक है। सीखने में कमी, मानसिक द्वन्द्व और दोषपूर्ण विधियाँ विस्मृति के कारण हैं।'),
    25: ('Statistics is the science of collecting, classifying, presenting, comparing and interpreting numerical data.',
         'संख्यात्मक आँकड़ों को एकत्र करने, वर्गीकृत करने, प्रस्तुत करने, तुलना और व्याख्या करने का विज्ञान सांख्यिकी है।'),
    26: ('16 PF, TAT and Draw-a-Man are personality tests; Raven\'s Progressive Matrices is an intelligence test.',
         '16 पी.एफ., टी.ए.टी. और ड्रा-ए-मैन व्यक्तित्व परीक्षण हैं; रैवेन का प्रगतिशील मैट्रिसेस बुद्धि परीक्षण है।'),
    27: ('With six values the median is the mean of the middle two: (9 + 10) ÷ 2 = 9.5.',
         'छह मानों में माध्यिका बीच के दो मानों का औसत है: (9 + 10) ÷ 2 = 9.5।'),
    28: ('The theory of insight learning was given by the Gestalt psychologists, especially Kohler.',
         'सूझ द्वारा सीखने का सिद्धांत गेस्टाल्टवादी मनोवैज्ञानिकों, विशेषकर कोहलर ने दिया।'),
    29: ('McDougall held that every instinct has an emotion attached to it, for example fear with escape.',
         'मैक्डूगल के अनुसार प्रत्येक मूल प्रवृत्ति के साथ एक संवेग जुड़ा होता है, जैसे पलायन के साथ भय।'),
    30: ('Perception is giving meaning to sensations on the basis of past experience.',
         'पूर्व अनुभव के आधार पर संवेदनाओं को अर्थ देना प्रत्यक्षज्ञान (प्रत्यक्षीकरण) है।'),
}
