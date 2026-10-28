"""UPTET 2019 Primary, Part I (Q1–30): Child Development and Teaching Method."""

SOURCE = 'primary'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (1, 30)
SUBJECT = 'cdp'

TOPICS = {
    'cdp.theories': [1, 7, 13, 16, 21, 26, 27],
    'cdp.inclusive': [2, 3, 11, 14, 18],
    'cdp.development': [5, 6, 8, 17, 20],
    'cdp.learning': [4, 9, 10, 12, 15, 19, 22, 23, 24, 25, 28, 30],
    'cdp.assessment': [29],
}

SKIP = {}

FIX = {
    12: {'options': {'c': ('Professional development of students', None)}},
    16: {
        'en': 'Match Column A with Column B.\n'
              'Column A: A. Animal Intelligence, B. Schedule of reinforcement, C. Law of Pragnanz, D. Adaptation\n'
              'Column B: I. Gestalt, II. Piaget, III. Thorndike, IV. Skinner',
        'hi': 'स्तम्भ–A तथा स्तम्भ–B को सुमेलित कीजिए।\n'
              'स्तम्भ–A: A. एनिमल इंटैलिजेंस, B. पुनर्बलन की अनुसूची, C. सारगर्भिता का नियम, D. अनुकूलन\n'
              'स्तम्भ–B: I. गेस्टॉल्ट, II. पियाजे, III. थॉर्नडाइक, IV. स्किनर',
        'match': ['I IV III II', 'II IV III I', 'II IV I III', 'III IV I II'],
    },
    22: {
        'en': 'Match List A with List B.\n'
              'List A: A. Bruner, B. Ausubel, C. Glaser, D. Gordon\n'
              'List B: I. Basic teaching model, II. Synectics teaching model, III. Advance organiser teaching model, '
              'IV. Concept attainment teaching model, V. Inquiry training model',
        'hi': 'सूची–A तथा सूची–B को सुमेलित कीजिए।\n'
              'सूची–A: A. ब्रुनर, B. ऑसुबेल, C. ग्लेजर, D. गॉर्डन\n'
              'सूची–B: I. बुनियादी शिक्षण प्रतिमान, II. सायनेक्टिक्स शिक्षण प्रतिमान, III. अग्रिम संगठक शिक्षण प्रतिमान, '
              'IV. सम्प्रत्यय उपलब्धि शिक्षण प्रतिमान, V. पृच्छा प्रशिक्षण प्रतिमान',
        'match': ['IV III I II', 'IV III II I', 'I II III V', 'III I II V'],
    },
    28: {
        'en': 'Morrison has described five steps in his teaching model at the understanding level:\n'
              'I. Presentation, II. Exploration, III. Organisation, IV. Assimilation, V. Recitation\n'
              'The correct sequence is:',
        'hi': 'मॉरीसन ने बोध स्तर के शिक्षण प्रतिमान में पाँच पदों का वर्णन किया है:\n'
              'I. प्रस्तुतीकरण, II. खोज, III. संगठन, IV. आत्मीकरण, V. वाचन (अभिव्यक्तिकरण)\n'
              'इनका सही क्रम है–',
        'options': {o: (t, t) for o, t in zip('abcd', ['IV, V, III, I, II', 'II, I, IV, III, V',
                                                        'II, I, III, IV, V', 'I, II, III, IV, V'])},
    },
}

EXPLAIN = {
    1: ('Howard Gardner proposed the theory of multiple intelligences in "Frames of Mind" (1983). He described '
        'linguistic, logical-mathematical, spatial, bodily-kinaesthetic, musical, interpersonal, intrapersonal and '
        'naturalist intelligences. Spearman is known for the two-factor theory and Goleman for emotional intelligence.',
        'बहुबुद्धि (बहुविमात्मक प्रज्ञा) का सिद्धांत हॉवर्ड गार्डनर ने 1983 में "फ्रेम्स ऑफ माइंड" में दिया। उन्होंने भाषायी, '
        'तार्किक-गणितीय, स्थानिक, शारीरिक-गतिक, संगीतात्मक, अंतर्वैयक्तिक, अंतःवैयक्तिक और प्रकृतिवादी बुद्धि बताई। स्पीयरमैन '
        'द्वि-कारक सिद्धांत और गोलमैन संवेगात्मक बुद्धि के लिए जाने जाते हैं।'),
    2: ('Dyslexia is a learning disability that mainly affects reading and spelling: the child finds it hard to link '
        'letters with their sounds, confuses or reverses letters, and reads slowly.',
        'डिस्लेक्सिया एक अधिगम अक्षमता है जिसमें मुख्य रूप से पढ़ने और वर्तनी में कठिनाई होती है। बच्चा अक्षरों को उनकी ध्वनियों से '
        'जोड़ने में कठिनाई महसूस करता है, अक्षरों को उलट-पलट देता है और धीरे पढ़ता है।'),
    3: ('In an inclusive classroom the teacher must give special attention to children with disabilities, along with '
        'suitable seating, encouragement and extra time. Ignoring differently abled children is not the role of a teacher.',
        'समावेशी कक्षा में शिक्षक को निःशक्त बच्चों पर विशेष ध्यान देना चाहिए, साथ ही उचित बैठने की व्यवस्था, प्रोत्साहन और '
        'अतिरिक्त समय देना चाहिए। निःशक्त बच्चों की उपेक्षा करना शिक्षक की भूमिका नहीं है।'),
    4: ('Students\' questions show curiosity and active participation, so a teacher should encourage them. Questioning '
        'helps children clear doubts and build understanding.',
        'छात्रों के प्रश्न उनकी जिज्ञासा और सक्रिय भागीदारी दिखाते हैं, इसलिए शिक्षक को उन्हें प्रेरित करना चाहिए। प्रश्न पूछने से '
        'बच्चे अपनी शंकाएँ दूर करते हैं और समझ विकसित करते हैं।'),
    5: ('Growth means quantitative change in the body, such as height, weight and the size of organs. So growth is '
        'mainly related to physical development; development is the wider, qualitative change.',
        'वृद्धि का अर्थ है शरीर में मात्रात्मक परिवर्तन, जैसे लम्बाई, भार और अंगों के आकार में बढ़ोतरी। इसलिए वृद्धि मुख्यतः शारीरिक '
        'विकास से सम्बन्धित है; विकास इससे व्यापक, गुणात्मक परिवर्तन है।'),
    6: ('Human development begins at conception, in the pre-natal stage (in the womb), and continues through infancy, '
        'childhood, adolescence and adulthood.',
        'मानव विकास गर्भाधान के साथ ही, गर्भावस्था (प्रसवपूर्व अवस्था) से आरम्भ होता है और शैशवावस्था, बाल्यावस्था, किशोरावस्था '
        'तथा प्रौढ़ावस्था तक चलता रहता है।'),
    7: ('"The Conditions of Learning" (1965) was written by Robert M. Gagne, who described eight types of learning '
        'arranged in a hierarchy, from signal learning to problem solving.',
        '"द कंडीशन्स ऑफ लर्निंग" (1965) के लेखक रॉबर्ट एम. गेने हैं। उन्होंने संकेत अधिगम से समस्या समाधान तक अधिगम के आठ '
        'प्रकारों का एक पदानुक्रम बताया।'),
    8: ('G. Stanley Hall, the father of the study of adolescence, described adolescence as a period of great "stress '
        'and strain, storm and strife".',
        'किशोरावस्था के अध्ययन के जनक जी. स्टेनले हॉल ने किशोरावस्था को "बड़े संघर्ष, तनाव, तूफान और विरोध" की अवस्था कहा।'),
    9: ('In the Indian model of micro-teaching the cycle takes 36 minutes: teach 6 min, feedback 6 min, re-plan 12 min, '
        're-teach 6 min and re-feedback 6 min.',
        'सूक्ष्म शिक्षण के भारतीय प्रतिमान में एक चक्र 36 मिनट का होता है: शिक्षण 6 मिनट, प्रतिपुष्टि 6 मिनट, पुनर्योजना 12 मिनट, '
        'पुनर्शिक्षण 6 मिनट और पुनर्प्रतिपुष्टि 6 मिनट।'),
    10: ('The answer key credits this definition of the learning plateau, a stage in which practice shows no visible '
         'improvement, to Ross.',
         'उत्तर कुंजी के अनुसार अधिगम के पठार (वह अवस्था जिसमें अभ्यास के बावजूद प्रगति दिखाई नहीं देती) की यह परिभाषा रॉस की है।'),
    11: ('A problem child needs to be understood, not punished or ignored. Counselling helps find the cause of the '
         'behaviour and guide the child.',
         'समस्यात्मक बालक को दण्ड देने या अनदेखा करने के बजाय समझने की आवश्यकता होती है। परामर्श से व्यवहार का कारण पता चलता '
         'है और बच्चे का उचित मार्गदर्शन होता है।'),
    12: ('Co-curricular activities such as sports, music, debates and scouting develop physical, social, emotional and '
         'moral qualities, so they serve the all-round development of students.',
         'खेल, संगीत, वाद-विवाद, स्काउटिंग जैसी पाठ्य-सहगामी क्रियाएँ शारीरिक, सामाजिक, संवेगात्मक और नैतिक गुणों का विकास करती हैं, '
         'इसलिए ये छात्रों के सर्वांगीण विकास से सम्बन्धित हैं।'),
    13: ('Kohler (insight), Skinner (operant conditioning) and Thorndike (trial and error) gave learning theories. '
         'B.S. Bloom is known for the taxonomy of educational objectives, not a learning theory.',
         'कोहलर (सूझ), स्किनर (क्रिया-प्रसूत अनुबंधन) और थॉर्नडाइक (प्रयास एवं त्रुटि) ने अधिगम सिद्धांत दिए। बी.एस. ब्लूम शैक्षिक '
         'उद्देश्यों के वर्गीकरण के लिए जाने जाते हैं, अधिगम सिद्धांत के लिए नहीं।'),
    14: ('Stagnation means a child stays in the same class for more than one year because of failing. Leaving school '
         'before completing a stage is called wastage or dropout.',
         'अवरोधन (स्टैग्नेशन) का अर्थ है असफल होने के कारण बालक का एक वर्ष से अधिक समय तक एक ही कक्षा में रहना। स्तर पूरा किए बिना '
         'विद्यालय छोड़ देना अपव्यय या ड्रॉपआउट कहलाता है।'),
    15: ('In the skill of introducing a lesson (set induction) the teacher tests and links the pupils\' previous '
         'knowledge to the new topic.',
         'प्रस्तावना कौशल में शिक्षक नए पाठ को शुरू करने से पहले छात्रों के पूर्व ज्ञान का परीक्षण करता है और उसे नए विषय से जोड़ता है।'),
    16: ('Animal Intelligence is Thorndike\'s work, schedules of reinforcement are Skinner\'s, the law of Pragnanz is a '
         'Gestalt law and adaptation is a concept of Piaget. So A–III, B–IV, C–I, D–II.',
         'एनिमल इंटैलिजेंस थॉर्नडाइक की कृति है, पुनर्बलन की अनुसूची स्किनर ने दी, सारगर्भिता (प्रैग्नैंज) का नियम गेस्टॉल्ट का है और '
         'अनुकूलन पियाजे की संकल्पना है। अतः A–III, B–IV, C–I, D–II।'),
    17: ('According to the principle of continuity, development is a never-ending process that goes on from '
         'conception until death.',
         'निरन्तरता के सिद्धांत के अनुसार विकास कभी न रुकने वाली प्रक्रिया है जो गर्भाधान से मृत्यु तक चलती रहती है।'),
    18: ('The 86th Constitutional Amendment Act, 2002 added Article 21A, making free and compulsory education for '
         'children aged 6 to 14 a fundamental right. The RTE Act, 2009 put it into effect.',
         '86वें संविधान संशोधन अधिनियम, 2002 द्वारा अनुच्छेद 21A जोड़ा गया, जिससे 6 से 14 वर्ष के बच्चों की निःशुल्क और अनिवार्य '
         'शिक्षा मौलिक अधिकार बनी। शिक्षा का अधिकार अधिनियम, 2009 ने इसे लागू किया।'),
    19: ('William McDougall gave the instinct theory of motivation, listing 14 instincts, each linked with an emotion.',
         'अभिप्रेरणा का मूल-प्रवृत्ति सिद्धांत विलियम मैक्डूगल ने दिया। उन्होंने 14 मूल प्रवृत्तियाँ बताईं, जिनमें से प्रत्येक के साथ '
         'एक संवेग जुड़ा होता है।'),
    20: ('Cole and Bruce called childhood "a unique period of emotional development", as emotions become more stable '
         'and socially directed in this stage.',
         'कोल तथा ब्रूस ने बाल्यावस्था को "संवेगात्मक विकास का अनोखा काल" कहा, क्योंकि इस अवस्था में संवेग अधिक स्थिर और '
         'सामाजिक रूप से नियंत्रित होने लगते हैं।'),
    21: ('J.P. Guilford defined learning as "any change in behaviour resulting from behaviour".',
         'जे.पी. गिलफोर्ड के अनुसार "व्यवहार के कारण व्यवहार में होने वाला कोई भी परिवर्तन अधिगम है।"'),
    22: ('Bruner gave the concept attainment model, Ausubel the advance organiser model, Glaser the basic teaching '
         'model and Gordon the synectics model. So A–IV, B–III, C–I, D–II.',
         'ब्रुनर ने सम्प्रत्यय उपलब्धि प्रतिमान, ऑसुबेल ने अग्रिम संगठक प्रतिमान, ग्लेजर ने बुनियादी शिक्षण प्रतिमान और गॉर्डन ने '
         'सायनेक्टिक्स प्रतिमान दिया। अतः A–IV, B–III, C–I, D–II।'),
    23: ('Problem solving starts with identifying and defining the problem. Hypotheses are formed and tested, and data '
         'collected, only after that.',
         'समस्या समाधान का पहला चरण समस्या की पहचान और उसे स्पष्ट करना है। परिकल्पना बनाना, आँकड़े एकत्र करना और परीक्षण '
         'इसके बाद आते हैं।'),
    24: ('Learning is most effective when it develops all three domains together: cognitive (knowing), affective '
         '(feeling) and psychomotor (doing). Rote skills alone, an autocratic system or passive children do not help.',
         'अधिगम सबसे प्रभावी तब होता है जब तीनों पक्षों, संज्ञानात्मक (जानना), भावात्मक (अनुभव करना) और मनोचालक (करना), का साथ-साथ '
         'विकास हो। केवल रटंत कौशल, एकाधिकारवादी व्यवस्था या निष्क्रिय बच्चे इसमें सहायक नहीं हैं।'),
    25: ('Both the memory-level (Herbart) and understanding-level (Morrison) teaching models include presentation, so '
         'it is the step common to both.',
         'स्मृति स्तर (हरबर्ट) और बोध स्तर (मॉरीसन) दोनों शिक्षण प्रतिमानों में प्रस्तुतीकरण का सोपान आता है, इसलिए यही दोनों में '
         'उभयनिष्ठ है।'),
    26: ('Skinner\'s operant conditioning is also called the theory of reinforcement, because a response that is '
         'reinforced is more likely to be repeated.',
         'स्किनर के क्रिया-प्रसूत अनुबंधन सिद्धांत को पुनर्बलन का सिद्धांत भी कहते हैं, क्योंकि जिस अनुक्रिया को पुनर्बलन मिलता है '
         'उसके दोहराए जाने की सम्भावना बढ़ जाती है।'),
    27: ('Bruner described three modes of representation: enactive (action), iconic (images) and symbolic (language and '
         'symbols). The intuitive stage belongs to Piaget\'s pre-operational period, not to Bruner.',
         'ब्रूनर ने संज्ञानात्मक विकास की तीन अवस्थाएँ बताईं: क्रियात्मक, प्रतिबिम्बात्मक और संकेतात्मक। अंतःप्रज्ञ (इंट्यूटिव) '
         'अवस्था पियाजे की पूर्व-संक्रियात्मक अवस्था का भाग है, ब्रूनर का नहीं।'),
    28: ('Morrison\'s understanding-level model has five steps in this order: exploration, presentation, assimilation, '
         'organisation and recitation, which is II, I, IV, III, V.',
         'मॉरीसन के बोध स्तर के प्रतिमान के पाँच पद इस क्रम में हैं: खोज, प्रस्तुतीकरण, आत्मीकरण, संगठन और वाचन, अर्थात् '
         'II, I, IV, III, V।'),
    29: ('In Bloom\'s taxonomy the cognitive domain includes knowledge, comprehension (understanding), application, '
         'analysis, synthesis and evaluation. Valuing belongs to the affective domain.',
         'ब्लूम के वर्गीकरण में संज्ञानात्मक क्षेत्र में ज्ञान, बोध, अनुप्रयोग, विश्लेषण, संश्लेषण और मूल्यांकन आते हैं। अनुमूल्यन '
         '(वैल्यूइंग) भावात्मक क्षेत्र का भाग है।'),
    30: ('Learning curves are of three types: convex (fast progress first), concave (slow progress first) and mixed '
         '(combination). There is no "longitudinal" learning curve.',
         'अधिगम वक्र तीन प्रकार के होते हैं: उन्नतोदर (पहले तेज प्रगति), नतोदर (पहले धीमी प्रगति) और मिश्रित। "लम्बवत्" नाम का कोई '
         'अधिगम वक्र नहीं होता।'),
}
