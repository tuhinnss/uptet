"""UPTET 2021 Primary (cancelled exam of 28 Nov 2021), Part I (Q1–30): Child Development and Teaching Method."""

SOURCE = 'primary21'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (1, 30)
SUBJECT = 'cdp'

TOPICS = {
    'cdp.theories': [1, 2, 3, 12, 14, 15, 22, 25, 26, 30],
    'cdp.development': [4, 5, 23],
    'cdp.learning': [7, 8, 9, 11, 13, 16, 17, 18, 20, 21, 24, 29],
    'cdp.assessment': [6, 10, 27, 28],
    'cdp.inclusive': [19],
}

SKIP = {}

REPLACE = [('believed learning to a function of', 'believed learning to be a function of'), ('Vyogotski', 'Vygotsky'),
           ('Vyogotsky', 'Vygotsky'), ('Glaserfled', 'Glasersfeld'), ('students pervious', "student's previous"),
           ('Trans formational', 'Transformational'), ('taxonmy', 'taxonomy'), ('Erykson', 'Erikson'),
           ('Singmund freud', 'Sigmund Freud'), ('सिंगमंड', 'सिगमंड'), ('marphic', 'morphic'), ('बाध्य मूल्यांकन', 'बाह्य मूल्यांकन'),
           ('मनोसमाजिक', 'मनोसामाजिक')]

FIX = {
    10: {'options': {'c': ('Both A and B', 'A एवं B दोनों')}},
    25: {'options': {'d': ('Both B and C', 'B व C दोनों')}},
}

EXPLAIN = {
    1: ('Thorndike\'s three main (primary) laws are readiness, exercise and effect. Attitude (set) is one of his '
        'secondary laws.',
        'थॉर्नडाइक के तीन मुख्य नियम तत्परता, अभ्यास और प्रभाव हैं। अभिवृत्ति (मनोवृत्ति) उनका गौण नियम है।'),
    2: ('Gestalt psychologists Kohler and Koffka held that learning happens through insight, a sudden grasp of the '
        'whole situation.',
        'गेस्टाल्ट मनोवैज्ञानिक कोहलर और कोफ्का के अनुसार सीखना सूझ द्वारा होता है, यानी पूरी स्थिति की अचानक समझ से।'),
    3: ('Lev Vygotsky is the father of social constructivism: children build knowledge through social interaction and '
        'language.',
        'लेव वाइगोत्सकी सामाजिक निर्माणवाद के जनक हैं: बच्चे सामाजिक अन्तःक्रिया और भाषा के माध्यम से ज्ञान का निर्माण करते हैं।'),
    4: ('Development is cumulative, directional and follows a pattern; it is not uncontrolled or independent of '
        'other influences.',
        'विकास संचयी और दिशात्मक होता है तथा एक निश्चित क्रम में चलता है; यह अनियंत्रित और स्वतंत्र नहीं होता।'),
    5: ('"Hereditary Genius" (1869) was written by Francis Galton.', '‘हेरिडिटरी जीनियस’ (1869) फ्रांसिस गाल्टन की पुस्तक है।'),
    6: ('In Bloom\'s cognitive domain, knowledge (recall) is the lowest level, and evaluation the highest.',
        'ब्लूम के संज्ञानात्मक पक्ष में ज्ञान (स्मरण) सबसे निचला स्तर है और मूल्यांकन सबसे ऊँचा।'),
    7: ('The micro-teaching cycle is plan, teach, feedback, re-plan, re-teach and re-feedback, so re-feedback is last.',
        'सूक्ष्म शिक्षण चक्र है: योजना, शिक्षण, प्रतिपुष्टि, पुनः योजना, पुनः शिक्षण और पुनः प्रतिपुष्टि। अतः अंतिम सोपान पुनः प्रतिपुष्टि है।'),
    8: ('Guilford described divergent thinking through fluency, flexibility, originality and elaboration, so it needs a '
        'free flow of ideas rather than one solution.',
        'गिल्फोर्ड के अनुसार अपसारी चिंतन में प्रवाह, लचीलापन, मौलिकता और विस्तार होते हैं, इसलिए इसमें एक समाधान नहीं, विचारों का प्रवाह आवश्यक है।'),
    9: ('Alex F. Osborn introduced brainstorming in the 1940s.', 'मस्तिष्क उद्वेलन (ब्रेनस्टॉर्मिंग) विधि एलेक्स एफ. ऑस्बोर्न ने 1940 के दशक में दी।'),
    10: ('The Thematic Apperception Test was developed by Henry A. Murray and Christiana D. Morgan (1935), so both are '
         'correct.',
         'प्रासंगिक अन्तर्बोध परीक्षण (TAT) हेनरी ए. मुरे और क्रिस्टियाना डी. मॉर्गन ने 1935 में बनाया, इसलिए दोनों सही हैं।'),
    11: ('Wallas\' stages of creative thinking are preparation, incubation, illumination and verification; '
         'preparation comes first.',
         'वालास के अनुसार सर्जनात्मक चिंतन की अवस्थाएँ आयोजन, उद्भवन, प्रबोधन और सत्यापन हैं; पहली अवस्था आयोजन है।'),
    12: ('E.L. Thorndike propounded the stimulus–response (connectionism) theory of learning.',
         'उद्दीपक–अनुक्रिया (सम्बन्धवाद) सिद्धान्त ई.एल. थॉर्नडाइक ने दिया।'),
    13: ('Learning is influenced by personal factors (ability, motivation), environmental factors and social factors, '
         'so all of them.',
         'अधिगम पर व्यक्तिगत (योग्यता, प्रेरणा), वातावरण सम्बन्धी और सामाजिक, सभी कारकों का प्रभाव पड़ता है।'),
    14: ('Howard Gardner gave the theory of multiple intelligences (1983).', 'बहुबुद्धि का सिद्धान्त हॉवर्ड गार्डनर ने 1983 में दिया।'),
    15: ('Charles Spearman gave the two-factor theory: a general factor (g) and specific factors (s).',
         'चार्ल्स स्पीयरमैन ने बुद्धि का द्विकारक सिद्धान्त दिया: सामान्य कारक (g) और विशिष्ट कारक (s)।'),
    16: ('The project method was developed by W.H. Kilpatrick, based on John Dewey\'s ideas.',
         'प्रोजेक्ट विधि डब्ल्यू.एच. किलपैट्रिक ने जॉन ड्यूवी के विचारों के आधार पर विकसित की।'),
    17: ('Introductory questions at the start of a lesson test and link the pupils\' previous knowledge.',
         'पाठ योजना में प्रस्तावना प्रश्न छात्रों के पूर्व ज्ञान की जाँच कर उसे नए पाठ से जोड़ते हैं।'),
    18: ('Children learn best in natural settings, by doing and through play. A tightly controlled environment does not '
         'help, so (d) is the wrong statement.',
         'बच्चे स्वाभाविक वातावरण में, करके और खेल-खेल में सबसे अच्छा सीखते हैं। नियंत्रित वातावरण सहायक नहीं है, इसलिए (d) गलत कथन है।'),
    19: ('The 86th Amendment (2002) added Article 21A, making education a fundamental right for children of 6 to 14.',
         '86वें संशोधन (2002) ने अनुच्छेद 21A जोड़कर 6 से 14 वर्ष के बच्चों के लिए शिक्षा को मौलिक अधिकार बनाया।'),
    20: ('Teaching includes diagnosing difficulties, remedial work and evaluating learning, so all of these.',
         'शिक्षण में कठिनाइयों का निदान, उपचारात्मक कार्य और मूल्यांकन, सभी शामिल हैं।'),
    21: ('Teaching is least effective when the teacher is autocratic, pupils are passive and only writing is stressed, '
         'so all of these.',
         'शिक्षक के एकाधिकारवादी होने, विद्यार्थियों के निष्क्रिय रहने और केवल लिखने पर बल देने से शिक्षण सबसे कम प्रभावी होता है।'),
    22: ('Noam Chomsky gave the theory of transformational (generative) grammar.',
         'रूपांतरण (रूपांतरणात्मक-प्रजनक) व्याकरण का सिद्धान्त नोम चोमस्की ने दिया।'),
    23: ('Sheldon classified body types as endomorphic, mesomorphic and ectomorphic. "Antagonistic" is not a body type.',
         'शेल्डन ने शारीरिक गठन के तीन प्रकार बताए: एण्डोमॉर्फिक, मेसोमॉर्फिक और एक्टोमॉर्फिक। ‘ऐन्टागोनिस्टिक’ कोई प्रकार नहीं है।'),
    24: ('The components of motivation are need, drive and incentive.', 'अभिप्रेरणा के घटक आवश्यकता, अन्तर्नोद और प्रोत्साहन हैं।'),
    25: ('Sigmund Freud propounded the psycho-analytic theory. Allport and Guilford are associated with trait theories.',
         'मनोविश्लेषणात्मक सिद्धान्त सिगमंड फ्रायड ने दिया। आलपोर्ट और गिल्फोर्ड शील-गुण सिद्धान्तों से जुड़े हैं।'),
    26: ('Skinner\'s operant conditioning led to programmed instruction, personalised instruction and behaviour '
         'modification. His programmes aim at errorless learning, so "learning through errors" is not his.',
         'स्किनर के सिद्धान्त से अभिक्रमित अनुदेशन, व्यक्ति निर्धारित अनुदेशन और व्यवहार रूपांतरण निकले। उनका अभिक्रम त्रुटिरहित अधिगम पर '
         'जोर देता है, इसलिए ‘त्रुटियों के माध्यम से सीखना’ उनसे सम्बन्धित नहीं है।'),
    27: ('Continuous and comprehensive evaluation looks at all aspects of a child over time, so it suits pupils with '
         'different abilities and interests.',
         'सतत एवं व्यापक मूल्यांकन बच्चे के सभी पक्षों का निरंतर आकलन करता है, इसलिए यह विभिन्न योग्यताओं और रुचियों वाले विद्यार्थियों के लिए उपयोगी है।'),
    28: ('The cognitive domain covers knowledge, comprehension, application, analysis, synthesis and evaluation. '
         'Character building belongs to the affective domain.',
         'संज्ञानात्मक पक्ष में ज्ञान, अवबोध, अनुप्रयोग, विश्लेषण, संश्लेषण और मूल्यांकन आते हैं। चरित्र निर्माण भावात्मक पक्ष का भाग है।'),
    29: ('The levels of teaching are memory, understanding and reflective. There is no "motivational level".',
         'शिक्षण के स्तर स्मृति, अवबोध और प्रत्यावर्ती (चिंतन) हैं। ‘अभिप्रेरणा स्तर’ कोई स्तर नहीं है।'),
    30: ('Erik Erikson gave the psycho-social theory of development, with eight stages across the life span.',
         'विकास का मनोसामाजिक सिद्धान्त एरिक एरिक्सन ने दिया, जिसमें जीवन भर की आठ अवस्थाएँ हैं।'),
}
