"""UPTET 2019 Junior, Part I (Q1–30): Child Development and Teaching Method. Shared by both junior papers."""

SOURCE = 'junior_ms'
ID_PREFIX = 'j'
PAPER_LABEL = 'Junior level paper'
RANGE = (1, 30)
SUBJECT = 'cdp'

TOPICS = {
    'cdp.theories': [10, 12, 13, 19, 20, 22, 23, 29],
    'cdp.inclusive': [16, 25],
    'cdp.development': [2, 7, 17, 18],
    'cdp.learning': [1, 3, 4, 6, 8, 9, 11, 14, 15, 21, 24, 26, 28, 30],
    'cdp.assessment': [5, 27],
}

SKIP = {}

FIX = {
    10: {
        'en': 'Match List A with List B.\n'
              'List A: A. Hull, B. McDougall, C. Freud, D. Maslow\n'
              'List B: I. Need theory, II. Instinct theory, III. Psycho-analytical theory, IV. Drive-reduction theory',
        'hi': 'सूची–A तथा सूची–B को सुमेलित कीजिए।\n'
              'सूची–A: A. हल, B. मैक्डूगल, C. फ्रॉयड, D. मैस्लो\n'
              'सूची–B: I. आवश्यकता सिद्धांत, II. मूल प्रवृत्ति सिद्धांत, III. मनो–विश्लेषण सिद्धांत, IV. प्रणोद–अवकलन सिद्धांत',
        'match': ['I II III IV', 'IV II III I', 'IV II I III', 'IV I II III'],
    },
    19: {'options': {'d': (None, 'संवेदी–गामक अवस्था')}},
}

EXPLAIN = {
    1: ('Insight (sudden understanding of the solution) helps problem solving. Frustration, anxiety and a negative '
        'mental set are obstacles.',
        'सूझ (हल का अचानक समझ में आना) समस्या समाधान में सहायक है। भग्नाशा, चिन्ता और नकारात्मक मानसिक वृत्ति बाधक हैं।'),
    2: ('Amusement is a feeling, and so an emotion. Stimulus, memory and attention are not emotions.',
        'आमोद (मनोरंजन का भाव) एक भावना अर्थात् संवेग है। उद्दीपक, स्मृति और ध्यान संवेग नहीं हैं।'),
    3: ('FIACS (Flanders\' Interaction Analysis Category System) was developed by Ned A. Flanders to record and analyse '
        'teacher–student talk in the classroom in 10 categories.',
        'एफ.आई.ए.सी.एस. (फ्लैण्डर्स अंतःक्रिया विश्लेषण वर्ग प्रणाली) नेड ए. फ्लैण्डर्स ने विकसित की। इसमें कक्षा में शिक्षक–छात्र '
        'वार्ता को 10 वर्गों में दर्ज कर विश्लेषण किया जाता है।'),
    4: ('Good questioning encourages pupils and asks thought-provoking questions. Increasing the number of yes/no '
        'questions does the opposite, so that statement is not correct.',
        'अच्छे प्रश्न कौशल में छात्रों को प्रोत्साहित किया जाता है और विचारोत्तेजक प्रश्न पूछे जाते हैं। केवल हाँ/न उत्तर वाले प्रश्न बढ़ाना '
        'इसके विपरीत है, इसलिए यह कथन सही नहीं है।'),
    5: ('Projective tests present ambiguous material on which the person projects inner feelings. The Thematic '
        'Apperception Test (TAT) is one; interview, rating scale and observation are not projective.',
        'प्रक्षेपी परीक्षणों में अस्पष्ट सामग्री दी जाती है, जिस पर व्यक्ति अपने आंतरिक भाव प्रक्षेपित करता है। प्रासंगिक अन्तर्बोध '
        'परीक्षण (TAT) ऐसा ही परीक्षण है; साक्षात्कार, निर्धारण मापनी और अवलोकन प्रक्षेपी नहीं हैं।'),
    6: ('In Wallas\' stages of creative thinking (preparation, incubation, illumination, verification), incubation is '
        'the stage in which the person stops working on the problem consciously and leaves irrelevant details aside.',
        'वालास की सृजनात्मक चिंतन की अवस्थाओं (आयोजन, उद्भवन, प्रबोधन, सत्यापन) में उद्भवन वह अवस्था है जिसमें व्यक्ति समस्या '
        'पर सचेत रूप से काम करना छोड़ देता है और असंगत बातों को अलग रख देता है।'),
    7: ('The phoneme is the smallest unit of sound in spoken language. The morpheme is the smallest unit of meaning.',
        'ध्वनिग्राम (फोनीम) बोली जाने वाली भाषा की सबसे छोटी ध्वनि इकाई है। रूपग्राम (मॉर्फीम) अर्थ की सबसे छोटी इकाई है।'),
    8: ('Creative thinking is divergent: it looks for many possible answers. Asking in how many different ways a problem '
        'can be solved invites divergent thinking; the other questions have one fixed answer.',
        'सृजनात्मक चिन्तन अपसारी होता है, यानी अनेक सम्भावित उत्तर खोजता है। "इसे कितने भिन्न तरीकों से हल किया जा सकता है?" '
        'जैसा प्रश्न अपसारी चिंतन को बढ़ाता है; बाकी प्रश्नों का एक ही निश्चित उत्तर है।'),
    9: ('Micro-teaching is scaled-down teaching: fewer pupils (5–10), a shorter lesson (5–10 minutes) and one teaching '
        'skill at a time.',
        'सूक्ष्म शिक्षण अवश्रेणीयन (छोटे पैमाने का) शिक्षण है: कम छात्र (5–10), छोटा पाठ (5–10 मिनट) और एक समय में एक शिक्षण कौशल।'),
    10: ('Hull gave the drive-reduction theory, McDougall the instinct theory, Freud the psycho-analytical theory and '
         'Maslow the need (hierarchy) theory. So A–IV, B–II, C–III, D–I.',
         'हल ने प्रणोद-अवकलन सिद्धांत, मैक्डूगल ने मूल प्रवृत्ति सिद्धांत, फ्रॉयड ने मनोविश्लेषण सिद्धांत और मैस्लो ने आवश्यकता '
         '(पदानुक्रम) सिद्धांत दिया। अतः A–IV, B–II, C–III, D–I।'),
    11: ('Skinner\'s programmed instruction rests on small steps, active responding, immediate reinforcement '
         '(confirmation), self-pacing and evaluation. "Practice" is not listed among its principles.',
         'स्किनर का अभिक्रमित अनुदेशन छोटे पदों, सक्रिय अनुक्रिया, तत्काल पुनर्बलन (पुष्टि), स्वगति और मूल्यांकन के सिद्धांतों पर आधारित '
         'है। "अभ्यास" इसके सिद्धांतों में नहीं गिना जाता।'),
    12: ('Thorndike\'s S–R learning involves a drive, a motive and a stimulus that leads to a response. Operant '
         'behaviour is Skinner\'s concept, not Thorndike\'s.',
         'थॉर्नडाइक के उद्दीपक–अनुक्रिया सिद्धांत में अन्तर्नोद, अभिप्रेरक और उद्दीपक महत्त्वपूर्ण हैं। क्रिया-प्रसूत व्यवहार स्किनर की '
         'संकल्पना है, थॉर्नडाइक की नहीं।'),
    13: ('Gagne\'s hierarchy runs from signal learning (lowest) through stimulus–response, chaining, verbal association, '
         'discrimination, concept and rule learning up to problem solving (highest).',
         'गेने की अधिगम सोपानिकी संकेत अधिगम (सबसे निम्न) से शुरू होकर उद्दीपक-अनुक्रिया, शृंखला, शाब्दिक साहचर्य, विभेदन, प्रत्यय और '
         'नियम अधिगम से होते हुए समस्या समाधान (सबसे उच्च) तक जाती है।'),
    14: ('Changing the voice, gestures and movement to hold pupils\' attention is part of the skill of stimulus '
         'variation.',
         'छात्रों का ध्यान बनाए रखने के लिए आवाज, हाव-भाव और गतिविधि में बदलाव करना उद्दीपन-परिवर्तन कौशल का भाग है।'),
    15: ('Communication involves a sender, a message, a medium, a receiver, interaction and feedback. Reinforcement is '
         'a learning concept, not an element of communication.',
         'सम्प्रेषण में प्रेषक, संदेश, माध्यम, प्राप्तकर्ता, अंतःक्रिया और प्रतिपुष्टि होते हैं। पुनर्बलन अधिगम की संकल्पना है, सम्प्रेषण '
         'का तत्व नहीं।'),
    16: ('Children with intellectual disability need individualised instruction matched to their pace and needs. '
         'Acceleration, enrichment and a high-level curriculum suit gifted children.',
         'मन्दितमना बालकों को उनकी गति और आवश्यकता के अनुसार वैयक्तिक अनुदेशन चाहिए। त्वरण, संवर्धन और उच्चस्तरीय पाठ्यचर्या '
         'प्रतिभाशाली बालकों के लिए उपयुक्त हैं।'),
    17: ('Development is a qualitative (as well as quantitative) process; growth is the quantitative change. So '
         '"development is a quantitative process" is not correct.',
         'विकास गुणात्मक (और मात्रात्मक भी) प्रक्रिया है; मात्रात्मक परिवर्तन वृद्धि है। इसलिए "विकास एक मात्रात्मक प्रक्रिया है" '
         'कथन सत्य नहीं है।'),
    18: ('Aptitude is a person\'s special ability or potential to succeed in a particular field with training.',
         'अभिक्षमता किसी विशेष क्षेत्र में प्रशिक्षण मिलने पर सफल होने की व्यक्ति की विशिष्ट योग्यता या क्षमता है।'),
    19: ('Bruner\'s iconic stage, in which the child thinks in images, is similar to Piaget\'s pre-operational stage '
         '(about 2–7 years).',
         'ब्रूनर की प्रतिबिम्बात्मक अवस्था, जिसमें बच्चा चित्रों/प्रतिमाओं में सोचता है, पियाजे की पूर्व-संक्रियात्मक अवस्था (लगभग '
         '2–7 वर्ष) से मिलती है।'),
    20: ('Allport, Cattell and Eysenck are trait theorists. Freud gave the psycho-analytic theory of personality.',
         'आलपोर्ट, कैटल और आइसेंक गुण (शील-गुण) सिद्धांत से जुड़े हैं। फ्रॉयड ने व्यक्तित्व का मनोविश्लेषणात्मक सिद्धांत दिया।'),
    21: ('Guilford and Torrance describe creativity through fluency, flexibility, originality and elaboration.',
         'गिलफोर्ड और टॉरेन्स के अनुसार सृजनात्मकता के तत्त्व प्रवाह, विविधता (लचीलापन), मौलिकता और विस्तारण हैं।'),
    22: ('Freud called a boy\'s strong attachment to his mother and rivalry with his father, in the phallic stage '
         '(about 3–6 years), the Oedipus complex. The girl\'s attachment to her father is the Electra complex.',
         'फ्रॉयड ने लिंग प्रधान अवस्था (लगभग 3–6 वर्ष) में बालक के माता के प्रति तीव्र लगाव और पिता से प्रतिद्वंद्विता को ओडिपस '
         'कॉम्पलेक्स कहा। बालिका का पिता के प्रति लगाव इलेक्ट्रा कॉम्पलेक्स है।'),
    23: ('Thorndike\'s secondary laws are multiple response, set or attitude, partial activity, analogy (assimilation) '
         'and associative shifting. There is no "law of action-reaction".',
         'थॉर्नडाइक के गौण नियम हैं: बहु-प्रतिक्रिया, मनोवृत्ति, आंशिक क्रिया, सादृश्यता (आत्मीकरण) और साहचर्य परिवर्तन। '
         '"क्रिया-प्रतिक्रिया का नियम" इनमें नहीं है।'),
    24: ('The answer key treats this as vertical transfer: a simpler skill learnt earlier (riding a scooter) helps in '
         'learning a more complex, higher-level skill (driving a car). Because the earlier learning helps, it is also '
         'positive transfer, so option (b) is arguable, but the key accepts only (c).',
         'उत्तर कुंजी इसे ऊर्ध्व अंतरण मानती है: पहले सीखा गया सरल कौशल (स्कूटर चलाना) अधिक जटिल, उच्च स्तर के कौशल (कार चलाना) '
         'को सीखने में सहायता करता है। पूर्व अधिगम सहायक होने से यह धनात्मक अंतरण भी है, इसलिए विकल्प (b) भी तर्कसंगत लगता है, '
         'पर कुंजी केवल (c) को सही मानती है।'),
    25: ('Dysphasia is difficulty in producing or understanding spoken language, so it affects communication. '
         'Dysgraphia affects writing, dyslexia reading and dyscalculia mathematics.',
         'डिस्फेशिया बोली गई भाषा को बोलने या समझने में कठिनाई है, जिससे सम्प्रेषण प्रभावित होता है। डिस्ग्रेफिया लेखन, डिस्लेक्सिया '
         'पठन और डिस्कैल्क्युलिया गणित से सम्बन्धित है।'),
    26: ('In the lecture method the teacher talks and pupils listen, so it is teacher-centred and not democratic. '
         'Project work, participation and group discussion involve the learners.',
         'व्याख्यान विधि में शिक्षक बोलता है और छात्र केवल सुनते हैं, इसलिए यह शिक्षक-केन्द्रित है, प्रजातांत्रिक नहीं। प्रोजेक्ट, सहभागी '
         'विधि और सामूहिक परिचर्चा में छात्र सक्रिय रहते हैं।'),
    27: ('Bloom\'s affective domain has receiving, responding, valuing, organisation and characterisation. Knowledge '
         'belongs to the cognitive domain.',
         'ब्लूम के भावात्मक पक्ष में आग्रहण, अनुक्रिया, अनुमूल्यन, व्यवस्थापन और चारित्रीकरण आते हैं। ज्ञान संज्ञानात्मक पक्ष का स्तर है।'),
    28: ('The three levels of teaching are memory (Herbart), understanding (Morrison) and reflective (Hunt). There is '
         'no "motivation level".',
         'शिक्षण के तीन स्तर हैं: स्मृति स्तर (हरबर्ट), अवबोध स्तर (मॉरीसन) और परावर्ती स्तर (हण्ट)। "अभिप्रेरणा स्तर" नाम का कोई '
         'स्तर नहीं है।'),
    29: ('Connectionist (S–R) theories describe learning as forming a bond between a stimulus and a response.',
         'सम्बन्धवादी (उद्दीपक–अनुक्रिया) सिद्धांतों के अनुसार अधिगम उद्दीपन और अनुक्रिया के बीच बन्धन (संगति) बनना है।'),
    30: ('Progressive education (John Dewey) stresses learning by doing and solving real problems, which is the basis '
         'of the problem-solving method.',
         'प्रगतिवादी शिक्षा (जॉन ड्यूवी) करके सीखने और वास्तविक समस्याओं को हल करने पर बल देती है, यही समस्या समाधान विधि का आधार है।'),
}
