"""Super TET 2019, Q51–70: Pedagogy & Child Development."""

RANGE = (51, 70)
LANGUAGE = None

TOPICS = {
    'cdp.policy': [51, 52, 55, 56, 58, 59, 60],
    'cdp.theories': [53, 65],
    'cdp.inclusive': [54, 61, 64, 70],
    'cdp.assessment': [57],
    'cdp.development': [62, 63, 66, 67],
    'cdp.learning': [68, 69],
}

SKIP = {}

FIX = {}

EXPLAIN = {
    51: ('Teaching is interactive, tripolar (teacher, learner and curriculum or social setting) and directed at '
         'bringing about desired effects in learners. It is not confined to the classroom: it also happens '
         'through activities, field visits, guidance and the wider school life.',
         'शिक्षण अन्तःक्रियात्मक है, त्रिमुखी (शिक्षक, छात्र और पाठ्यक्रम/सामाजिक परिवेश) है और छात्रों में वांछित प्रभाव लाने '
         'की दिशा में चलता है। यह केवल कक्षा तक सीमित नहीं है; गतिविधियों, भ्रमण, निर्देशन और पूरे विद्यालयी जीवन में भी होता है।'),
    52: ('The Mid-Day Meal scheme (1995, now PM POSHAN) gives cooked meals in government schools mainly to raise '
         'enrolment and attendance and to keep children in school, while also improving nutrition.',
         'मध्याह्न भोजन योजना (1995, अब पीएम पोषण) का मुख्य उद्देश्य सरकारी विद्यालयों में नामांकन और उपस्थिति बढ़ाना तथा बच्चों '
         'को विद्यालय में रोके रखना है; साथ ही इससे पोषण भी सुधरता है।'),
    53: ('E. L. Thorndike propounded the stimulus–response (S–R) bond theory, also called connectionism or trial '
         'and error learning, with his laws of readiness, exercise and effect.',
         'उद्दीपन–अनुक्रिया (S–R) बंध सिद्धांत, जिसे संबंधवाद या प्रयास एवं त्रुटि सिद्धांत भी कहते हैं, ई० एल० थॉर्नडाइक ने दिया। '
         'उन्होंने तत्परता, अभ्यास और प्रभाव के नियम भी दिए।'),
    54: ('Dyslexia is a learning disability in reading, and it often affects spelling and writing too. Dysgraphia '
         'is specific to writing, dyspraxia affects coordination of movement and apraxia affects planned movements '
         'such as speech.',
         'डिस्लेक्सिया पढ़ने की अक्षमता है, जिसका असर प्रायः वर्तनी और लेखन पर भी पड़ता है। डिस्ग्राफ़िया लिखने की, डिस्प्रेक्सिया '
         'गति-समन्वय की और एप्रेक्सिया नियोजित गतियों (जैसे बोलने) की अक्षमता है।'),
    55: ('Everett M. Rogers, in “Diffusion of Innovations” (1962), defined an innovation as an idea, practice or '
         'object perceived as new by an individual or other unit of adoption.',
         'एवरेट एम० रोजर्स ने ‘डिफ्यूज़न ऑफ़ इनोवेशन्स’ (1962) में नवाचार को ऐसा विचार, व्यवहार या वस्तु बताया जिसे व्यक्ति '
         'या अपनाने वाली इकाई नया अनुभव करे।'),
    56: ('The Hartog Committee (1929) was the first to point out wastage (pupils leaving school early) and '
         'stagnation (pupils failing and repeating classes) in primary education in India.',
         'हार्टोग समिति (1929) ने सबसे पहले भारत की प्राथमिक शिक्षा में अपव्यय (बीच में पढ़ाई छोड़ना) और अवरोधन (अनुत्तीर्ण होकर '
         'उसी कक्षा में रुकना) की समस्या उठाई।'),
    57: ('Only a ratio scale has a true (absolute) zero, which means none of the quantity, as in height, weight or '
         'marks. That is why ratios like “twice as much” make sense on it. Nominal, ordinal and interval scales have '
         'no true zero.',
         'केवल आनुपातिक स्केल में वास्तविक (परम) शून्य होता है, जिसका अर्थ है गुण का पूर्ण अभाव, जैसे लम्बाई, भार या अंक। इसी से '
         '‘दोगुना’ जैसे अनुपात सार्थक होते हैं। नामित, क्रमित और अंतरित स्केल में परम शून्य नहीं होता।'),
    58: ('The skill of introducing a lesson links the new lesson to what pupils already know. Using their previous '
         'knowledge through questions, examples or activities is its main component.',
         'पाठ प्रस्तावना कौशल में नए पाठ को छात्रों के पूर्वज्ञान से जोड़ा जाता है। प्रश्नों, उदाहरणों या गतिविधियों से पूर्वज्ञान का '
         'उपयोग इसका मुख्य संघटक है।'),
    59: ('NCERT brought out the National Curriculum Framework in 2005 (NCF 2005). It stresses linking knowledge to '
         'life outside school, moving away from rote learning and making examinations more flexible.',
         'एन० सी० ई० आर० टी० ने राष्ट्रीय पाठ्यचर्या की रूपरेखा 2005 (NCF 2005) प्रस्तुत की। इसमें ज्ञान को स्कूल के बाहर के '
         'जीवन से जोड़ने, रटने से दूर रहने और परीक्षा को लचीला बनाने पर बल दिया गया।'),
    60: ('This is Sir Graham Balfour’s well-known definition: educational administration enables the right pupils '
         'to receive the right education from the right teachers, within the means available. The booklet prints '
         'his name as “Welfare Grahya”.',
         'यह सर ग्राहम बालफ़ोर की प्रसिद्ध परिभाषा है: शैक्षिक प्रशासन उपयुक्त छात्रों को उपयुक्त शिक्षकों द्वारा उपलब्ध साधनों के '
         'भीतर उपयुक्त शिक्षा दिलाता है। प्रश्न-पुस्तिका में नाम ‘वेलफेयर ग्राह्य’ छपा है।'),
    61: ('The Rehabilitation Council of India (RCI), a statutory body since 1992, regulates and standardises the '
         'training of professionals who educate and rehabilitate persons with disabilities.',
         'भारतीय पुनर्वास परिषद् (RCI), जो 1992 से सांविधिक निकाय है, दिव्यांगजन की शिक्षा और पुनर्वास से जुड़े पेशेवरों के '
         'प्रशिक्षण का नियमन और मानकीकरण करती है।'),
    62: ('Development follows two directions: cephalocaudal (from head to feet) and proximodistal (from the centre '
         'of the body outwards). The law of developmental direction includes both.',
         'विकास दो दिशाओं में होता है: मस्तकाधोमुखी (सिर से पैर की ओर) और निकट से दूर (शरीर के केन्द्र से बाहर की ओर)। '
         'विकास की दिशा का नियम दोनों को सम्मिलित करता है।'),
    63: ('Margaret Mead’s studies of tribes in Samoa and New Guinea showed that much of the difference in '
         'behaviour and personality comes from culture, so she held cultural factors to be the most important.',
         'मार्गरेट मीड ने समोआ और न्यू गिनी की जनजातियों के अध्ययन से दिखाया कि व्यवहार और व्यक्तित्व के अधिकांश अंतर संस्कृति '
         'से आते हैं, इसलिए उन्होंने सांस्कृतिक कारक को सबसे महत्त्वपूर्ण माना।'),
    64: ('Louis Braille of France, blind from childhood, developed the six-dot raised script in 1824, building on '
         'Charles Barbier’s “night writing”.',
         'फ्रांस के लुई ब्रेल ने, जो बचपन से दृष्टिहीन थे, चार्ल्स बारबियर की ‘नाइट राइटिंग’ के आधार पर 1824 में छह उभरे बिन्दुओं '
         'वाली लिपि बनाई।'),
    65: ('Ivan Pavlov gave the theory of classical conditioning from his experiments in which a dog learned to '
         'salivate at the sound of a bell paired with food. Skinner gave operant conditioning.',
         'प्राचीन (शास्त्रीय) अनुबंधन का सिद्धांत इवान पावलोव ने कुत्ते पर प्रयोग से दिया, जिसमें घंटी और भोजन साथ देने पर कुत्ता '
         'घंटी सुनकर ही लार टपकाने लगा। स्किनर ने क्रियाप्रसूत अनुबंधन दिया।'),
    66: ('Francis Galton wrote “Hereditary Genius” (1869), arguing from family records that ability is inherited. '
         'He also founded eugenics and pioneered the study of individual differences.',
         'फ्रांसिस गाल्टन ने ‘हेरेडिटरी जीनियस’ (1869) लिखी, जिसमें परिवारों के अध्ययन से बताया कि योग्यता वंशानुगत होती है। '
         'उन्होंने व्यक्तिगत भिन्नताओं के अध्ययन की नींव भी रखी।'),
    67: ('A child’s growth is shaped by many factors together: hormones from the endocrine glands, nutrition, '
         'and illness or injury among others. So all of the listed factors affect development.',
         'बालक का विकास अनेक कारकों से प्रभावित होता है, जैसे अंतःस्रावी ग्रंथियों के हार्मोन, पौष्टिक भोजन, और रोग तथा चोट। '
         'अतः उपर्युक्त सभी कारक विकास को प्रभावित करते हैं।'),
    68: ('Gagné arranged learning from simple to complex: signal, stimulus–response, chaining, verbal association, '
         'discrimination, concept learning, rule (principle) learning and problem solving. So concept learning '
         'comes before rule learning, which comes before problem solving.',
         'गैग्ने ने अधिगम को सरल से जटिल क्रम में रखा: संकेत, उद्दीपन–अनुक्रिया, शृंखला, शाब्दिक साहचर्य, विभेदन, सम्प्रत्यय अधिगम, '
         'नियम अधिगम और समस्या समाधान। अतः सम्प्रत्यय, फिर नियम, फिर समस्या समाधान।'),
    69: ('In Wallas’s stages of creative thinking (preparation, incubation, illumination, verification), '
         'incubation is the stage in which the person stops working on the problem consciously and the mind works '
         'on it in the background.',
         'वालास के सृजनात्मक चिंतन के चरणों (आयोजन, उद्भवन, प्रदीप्ति, सत्यापन) में उद्भवन वह अवस्था है जिसमें व्यक्ति समस्या पर '
         'सचेत रूप से ध्यान नहीं देता और मन भीतर ही भीतर उस पर काम करता है।'),
    70: ('The National Institute for the Orthopaedically Handicapped, now the National Institute for Locomotor '
         'Disabilities (Divyangjan), is in Kolkata.',
         'राष्ट्रीय अस्थि विकलांग संस्थान, जिसका नाम अब राष्ट्रीय चलन दिव्यांगजन संस्थान है, कोलकाता में है।'),
}
