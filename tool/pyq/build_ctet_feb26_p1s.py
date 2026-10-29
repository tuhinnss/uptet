"""Turn the extracted CTET Feb 2026 Paper I Set S questions
(Q1-90) into content-pack entries and merge them into content_pack.json.

usage: python -I build_ctet_feb26_p1s.py q1_90.json content_pack.json
"""
import json
import re
import sys

extracted_path, pack_path = sys.argv[1:3]
extracted = {q["qno"]: q for q in json.load(open(extracted_path, encoding="utf-8"))}

PAPER_ID = "ctet-feb26-p1-07feb-s"
SKIP = {16: "final key accepts option 1 or 4"}


def qid(n):
    return f"q-ctet-feb26-p1-s-{n:03d}"


# ---- Repairs: text lost or garbled by PDF extraction, checked against the booklet text/glyph codes.
STEMS = {
    32: "If 101 × 210 − 120 × 102 = 99 × 104 − □, then what is the number at □?",
    35: "Kanta has five dozen chocolates. She gives 1/6 of these to Aruna and 1/5 of the remaining "
        "chocolates to Radha. She then gives 1/8 of the remaining chocolates to each of her other three "
        "friends. How many chocolates does Kanta have now?",
    36: "(LCM of 96, 120 and 160) ÷ (HCF of 72 and 168) is equal to",
    37: "The cost of 8 Samosas is ₹ 156 and that of 4 Idlis is ₹ 98. Sunita has a ₹ 200 note only and "
        "buys 3 Samosas and 3 Idlis. How much money is left with her now?",
    44: "The following table shows the number of visitors to a library in the first six days of a week:\n"
        "Days — Number of visitors\nMonday — 86\nTuesday — 114\nWednesday — 141\nThursday — 95\n"
        "Friday — 124\nSaturday — 151\n"
        "On which day, the number of visitors to the library was 29 more than its previous day?",
    76: "Match Column–A with Column–B:\n"
        "Column–A: (a) Peer assessment  (b) Rubric-based rating scale  (c) Assessment as learning  "
        "(d) Paper-pencil test\n"
        "Column–B: (i) Tool of assessment  (ii) Self-learning  (iii) Summative assessment  "
        "(iv) Technique of assessment\n"
        "Choose the correct option.",
}
OPTIONS = {
    9: ["A teacher gave half-solved problems to her students who were finding it difficult to solve them otherwise.",
        "A teacher has strictly prohibited students to have any kind of collaborations and communication with their peers.",
        "A teacher has written answers on the blackboard and has asked the students to copy the answers passively in their notebooks.",
        "A teacher has made it mandatory for her students to solve problems on their own in a set time period."],
    37: ["₹ 65", "₹ 66", "₹ 68", "₹ 72"],
    43: ["five faces and five vertices", "six faces and six edges",
         "six vertices and five faces", "six vertices and six faces"],
    53: ["Is 15 × 4 equal to 4 × 15?", "Solve 1/2 ÷ 1/3.",
         "Extend the sequence A, DE, HIJ, _____ .",
         "There are 12 balls in a box. How many balls will be there in 5 such boxes?"],
    76: ["(a)–(iii), (b)–(iv), (c)–(i), (d)–(ii)", "(a)–(i), (b)–(iv), (c)–(iii), (d)–(ii)",
         "(a)–(iv), (b)–(i), (c)–(ii), (d)–(iii)", "(a)–(iii), (b)–(iv), (c)–(ii), (d)–(i)"],
    79: ["Facts, principles and laws of EVS", "How children learn EVS?",
         "How to teach EVS?", "Concepts and curriculum of EVS"],
    86: ["Both A and B are true.", "Both A and B are false.",
         "A is true but B is false.", "A is false but B is true."],
}
OPTIONS[88] = OPTIONS[86]
OPTION_FIXES = {  # (question, option number) -> full text where the option wrapped onto a second line
    (19, 1): "Children with Autism Spectrum Disorder have excellent communication skills but very poor memory.",
    (23, 3): "supportive only for students with learning disabilities because they have difficulty in auditory processing.",
    (46, 2): "Provide few practical examples to the child to understand the position of digits in a number.",
    (51, 4): "They might be derived from recent experiences in the classroom like a field trip, a discussion in art, "
             "science, or social studies classrooms.",
    (57, 3): "A child can informally deduce general properties of a given geometrical shape and is able to see the "
             "linkages among these properties.",
    (58, 4): "Including examples of different methods of calculation used by the people from various occupations "
             "and communities",
    (65, 2): "Some old houses have special type of windows which come out of the wall. These are called ‘dab’.",
    (74, 2): "These paintings are done on the floor using brush and indigo in the Mithila region of Bihar.",
    (74, 4): "It has its roots in the Mithila region of Bihar and these are made out of paste of powdered rice in "
             "which colours are mixed.",
    (81, 2): "Ask her to relate laying of eggs/giving birth to their visible ears and whose ears cannot be seen.",
}

# ---- Topics
TOPICS = {}
for n in (1, 2, 3, 4, 8, 14):
    TOPICS[n] = "cdp.development"
for n in (5, 6, 7, 9, 11, 12, 13, 23, 26):
    TOPICS[n] = "cdp.theories"
for n in (10, 21, 22, 24, 25, 27, 28, 29, 30):
    TOPICS[n] = "cdp.learning"
TOPICS[15] = "cdp.assessment"
for n in (17, 18, 19, 20):
    TOPICS[n] = "cdp.inclusive"
for n in (31, 32, 33, 34, 35, 36, 45):
    TOPICS[n] = "math.numbers"
for n in (37, 38, 40, 44):
    TOPICS[n] = "math.measurement"
for n in (39, 41, 42, 43):
    TOPICS[n] = "math.geometry"
for n in range(46, 61):
    TOPICS[n] = "math.pedagogy"
for n in (64, 66, 67):
    TOPICS[n] = "evs.living"
for n in (61, 62, 63, 65, 68, 69, 70, 71, 72, 73, 74, 75):
    TOPICS[n] = "evs.society"
for n in range(76, 91):
    TOPICS[n] = "evs.pedagogy"

NEW_TOPICS = {  # subject -> topics to add (id, en, hi)
    "cdp": [("cdp.development", "Development: principles and influences", "विकास: सिद्धांत एवं प्रभाव"),
            ("cdp.learning", "Learning, motivation and classroom practice", "अधिगम, अभिप्रेरणा एवं कक्षा-अभ्यास")],
    "math": [("math.measurement", "Measurement, money and data", "मापन, धन एवं आँकड़े"),
             ("math.pedagogy", "Pedagogy of mathematics", "गणित का शिक्षाशास्त्र")],
    "evs": [("evs.society", "Family, shelter, travel and culture", "परिवार, आवास, यात्रा एवं संस्कृति"),
            ("evs.pedagogy", "Pedagogy of EVS", "पर्यावरण अध्ययन का शिक्षाशास्त्र")],
}

# ---- Explanations (UPTET Saathi's own; they explain the official answer, they are not CBSE text)
EXPLAIN = {
    1: "Children inherit genes from both parents and also grow up in their own environments. Because each trait comes from a complex mix of heredity (nature) and environment (nurture), some children closely resemble their parents while others differ markedly. So R is the correct explanation of A.",
    2: "Development takes place in many domains at once — physical, cognitive, social and emotional (multidimensional) — and some abilities grow while others decline (multidirectional). It is not a simple single process, it cannot be predicted very accurately, and it cannot always be measured precisely.",
    3: "Development in one domain is linked to the others. Understanding and producing speech depends on the maturing of the brain and speech organs, and emotional development is likewise tied to physical growth. The official key treats R as explaining A because both describe how physical growth underlies other areas of development.",
    4: "Speech develops quickly in the early years: around one year children say single words, and by about three years most can speak in short, connected sentences. Five-to-six sentence coherent speech is typical of this age, not a later one.",
    5: "Vygotsky held that speech begins as social (external) speech, then becomes private speech — children 'think out loud' to guide themselves — and finally turns into silent inner speech, which works as thought.",
    6: "Piaget described four qualitatively different stages: sensorimotor, pre-operational, concrete operational and formal operational. Option 3 describes Erikson's eight psychosocial stages, and option 4 describes a continuous (non-stage) view of development.",
    7: "Linking two unrelated events — being mean to her brother and his falling sick — shows the faulty, magical cause-and-effect reasoning and egocentrism that Piaget described in the pre-operational stage (about 2 to 7 years).",
    8: "Gender typing is the process through which children learn the roles, behaviours and attitudes their society considers appropriate for their gender. Equality, relatedness and homogeneity are not names of this process.",
    9: "Scaffolding is temporary support matched to what a learner can do with help (the zone of proximal development), withdrawn as the learner gains skill. Giving half-solved problems to students who could not solve them alone is such support; banning collaboration, copying answers or forcing solo timed work is not.",
    10: "Progressive education, associated with John Dewey, puts the learner at the centre and emphasises learning through experience, activity and participation, rather than rote memorisation, testing or competition.",
    11: "A is true: in Kohlberg's theory children move from judging actions by their consequences to understanding that rules are social agreements that can change. R is false: Kohlberg described moral development as a sequence of distinct stages, which is a discontinuous view.",
    12: "For Vygotsky, language is the main tool of thought. Private speech — children talking to themselves — guides and regulates their thinking. Assimilation and accommodation are Piaget's ideas, and reinforcement belongs to behaviourism.",
    13: "In Gardner's theory, interpersonal intelligence is the ability to understand other people's moods, feelings, intentions and motivations and to respond to them well. The other options are different intelligences.",
    14: "The family is the first and most important agent of socialisation. Children's earliest ideas of what it means to be a 'girl' or a 'boy' come from how their family treats them and what it expects of them; media, relatives and neighbours influence them later.",
    15: "Formative assessment is assessment for learning: it is ongoing, gives feedback, and makes the criteria for good work clear to learners so they can improve. Ranking learners, year-end exams and a purely quantitative focus belong to summative assessment.",
    17: "Gifted children have cognitive needs (challenge and enrichment) but also social and emotional needs, such as finding peers they relate to and managing perfectionism or sensitivity. Teachers should cater to all three.",
    18: "Children with learning disabilities benefit from multisensory teaching, flexible and step-by-step instructions, and tasks broken into smaller parts. Standardised, identical learning goals for everyone do not meet their individual needs.",
    19: "Many children with Autism Spectrum Disorder process sensory input differently, so sensory integration and regulation strategies help them. ASD mainly affects social communication and interaction (not hearing), and children with ASD usually prefer routine and sameness rather than new stimuli.",
    20: "Inclusive teaching asks teachers to keep examining their own hidden biases and assumptions about learners. Diversity should be seen as a resource, children with special needs should not be viewed as helpless, and teaching should be adapted to different learners rather than uniform.",
    21: "A print-rich classroom with varied children's literature gives children constant, meaningful contact with reading and writing. Because classrooms rich in literacy materials and experiences are central to effective learning, R is the correct explanation of A.",
    22: "A progressive classroom values inquiry, discussion and reflection. Encouraging reflective thinking helps students examine their own ideas and learn from experience; conditioning, passive copying and obedient listening do not.",
    23: "Speaking one's thoughts aloud is private speech, which Vygotsky saw as a tool that organises and guides thinking. So verbalising his steps is likely to help Raman solve the problem.",
    24: "A constructivist teacher respects how each child builds knowledge and does not judge students on the basis of their socio-cultural background. Such a teacher connects content to the real world, limits lecturing and avoids rigid ability grouping.",
    25: "Active engagement means learners take part in building their own knowledge — they inquire, explore and ask questions — rather than memorising facts, chasing marks or relying only on the textbook.",
    26: "Radha compares the sun and the shade and links a cause (the sun's heat) to an effect (clothes drying faster). This is an understanding of cause and effect.",
    27: "Intrinsic motivation comes from within — doing something because it is enjoyable or satisfying in itself. Studying for grades, playing for prize money and avoiding scolding are driven by external rewards or punishments (extrinsic motivation).",
    28: "A is true: constructivist teachers give children many materials to explore and build understanding. R is false: young children learn meaningfully through concrete, hands-on experience, not only through verbal instructions and lectures.",
    29: "Performance-avoidance goals are about avoiding looking incompetent in front of others. Mastery and task-involved goals focus on learning itself, and performance-approach goals focus on appearing more able than others.",
    30: "Critical thinking grows when students think independently, ask questions and examine assumptions. Rote memorisation, discouraging questions and fixed answers work against it.",
    31: "The primes between 12 and 49 are 13, 17, 19, 23, 29, 31, 37, 41, 43 and 47. Their sum is 300.",
    32: "101 × 210 = 21210 and 120 × 102 = 12240, so the left side is 21210 − 12240 = 8970. Also 99 × 104 = 10296, so 10296 − □ = 8970, which gives □ = 1326.",
    33: "The common factors of 36 and 48 are 1, 2, 3, 4, 6 and 12. Leaving out 1: 2 + 3 + 4 + 6 + 12 = 27.",
    34: "The greatest number using 1, 5, 0 and 7 once is 7510. The least 4-digit number cannot start with 0, so it is 1057. Difference: 7510 − 1057 = 6453.",
    35: "Five dozen = 60. Aruna gets 1/6 of 60 = 10, leaving 50. Radha gets 1/5 of 50 = 10, leaving 40. Each of three friends gets 1/8 of 40 = 5, so 15 more are given away. Kanta has 40 − 15 = 25.",
    36: "LCM of 96 (2⁵ × 3), 120 (2³ × 3 × 5) and 160 (2⁵ × 5) is 2⁵ × 3 × 5 = 480. HCF of 72 (2³ × 3²) and 168 (2³ × 3 × 7) is 2³ × 3 = 24. 480 ÷ 24 = 20.",
    37: "One samosa costs 156 ÷ 8 = ₹ 19.50 and one idli costs 98 ÷ 4 = ₹ 24.50. Three of each cost 3 × (19.50 + 24.50) = ₹ 132. Money left = 200 − 132 = ₹ 68.",
    38: "24 L 650 mL = 24650 mL, so each bottle holds 24650 ÷ 29 = 850 mL. Fifteen bottles hold 15 × 850 = 12750 mL = 12 L 750 mL.",
    39: "The cuboidal box holds 12 × 10 × 8 = 960 dice and the cubical box holds 9 × 9 × 9 = 729 dice, 1689 in all. Dice left unpacked = 1800 − 1689 = 111.",
    40: "Weight of lemons = 46160 g − 17115 g − 15325 g − 120 g = 13600 g = 13.6 kg. Since 30 lemons weigh 1 kg, there are 13.6 × 30 = 408 lemons.",
    41: "A rectangle (not a square) and a rhombus (not a square) each have exactly two lines of symmetry. An equilateral triangle has three and an isosceles triangle has one, so the answer is B and C.",
    42: "The letter Z looks the same after a half turn (rotational symmetry of order 2), but no line divides it into mirror halves. X and O have both kinds of symmetry, and M has a vertical line of symmetry but no rotational symmetry.",
    43: "A pentagonal pyramid has a pentagonal base and five triangular faces (6 faces), five base corners plus the apex (6 vertices), and 10 edges. So it has six vertices and six faces.",
    44: "Day-to-day increases: Tuesday +28, Wednesday +27, Thursday −46, Friday +29 (124 − 95), Saturday +27. Friday had 29 more visitors than the previous day.",
    45: "Each term is 3 times the previous term plus 1, 2, 3, … in turn: 3 × 3 + 1 = 10, 10 × 3 + 2 = 32, 32 × 3 + 3 = 99. Next: 99 × 3 + 4 = 301 and 301 × 3 + 5 = 908. Their sum is 1209.",
    46: "Reading 308 as 'thirty-eight' shows the child has not understood place value — that the 3 stands for 3 hundreds and the 0 holds the tens place. Concrete examples (such as bundles of sticks or place-value cards) build this understanding; repeating after the teacher or counting does not address the gap.",
    47: "The problem starts with a quantity (4 mangoes) and increases it by adding more (6 mangoes). This 'change-increase' structure is called augmentation. Aggregation would combine two separate groups into one.",
    48: "Pre-number concepts such as classification (sorting by attributes), ordering or seriation, matching and one-to-one correspondence lay the foundation for number sense at the foundational stage. Operations and place value come after these.",
    49: "Mechanically solving algorithm-based workbook questions does little to build understanding. Intuitive ideas, links to real life and open discussion on problem solving are all desirable in a primary mathematics classroom.",
    50: "A social perspective on assessment values the mathematics children meet outside school, including folk algorithms from different cultures. Standardised tests do not take this perspective, so the answer is A and C.",
    51: "Contextual problems are linked to children's lives, help develop mathematical modelling and can come from classroom experiences. Their purpose is to shift attention to understanding the situation, not just getting a correct answer — so statement 3 is the least appropriate.",
    52: "Data representation and analysis should begin at the primary stage and be strengthened at the upper primary stage. The reason given is the correct one: working with data shows children that information can be uncertain and variable, unlike the fixed facts they mostly study.",
    53: "Commutativity of multiplication, extending letter patterns and simple multiplication word problems are expected at class III. Dividing fractions, such as 1/2 ÷ 1/3, belongs to much later classes, so it is not a class III learning outcome.",
    54: "Zero is the additive identity for whole numbers because a + 0 = a. One (not zero) is the multiplicative identity, division is not commutative, and mathematics rests on logical reasoning, not only on observation and experiment.",
    55: "Primary mathematics should nurture children's curiosity and enjoyment of mathematics, building understanding through exploration rather than rote learning, written algorithms or textbook drill.",
    56: "Writing 'five hundred three' as 5003 shows the child writes 500 and then 3 instead of using place value to show 5 hundreds, 0 tens and 3 ones. The difficulty is with the concept of place value.",
    57: "Van Hiele's levels are visualisation, analysis, informal deduction (relationships), formal deduction and rigour. At the relationships level, a child can informally deduce properties of shapes and see the links between them. Option 4 describes a later level and options 1 and 2 earlier ones.",
    58: "Bringing in the calculation methods used by people of different occupations and communities connects mathematics to children's own cultures and lives. Pictures alone, only traditional methods or remedial teaching do not draw on local knowledge in this way.",
    59: "NEP 2020 makes foundational literacy and numeracy the highest priority, to be achieved by all students by grade 3.",
    60: "Pouring the same water from a tall, thin jar into a short, broad jar shows that the amount stays the same even though it looks different. This activity teaches volume and its conservation.",
    61: "Average speed = 756 km ÷ 14 h = 54 km/h. Converting: 54 × 1000 m ÷ 3600 s = 15 m/s.",
    62: "Ladakh is a cold desert, so houses have thick walls of stone, mud and lime to keep warm, wooden floors and flat wooden ceilings (flat roofs suit the little rain there), and a ground floor without windows for animals and storage. Raised houses with slanting roofs suit places with heavy rain, not Ladakh.",
    63: "This question is based on the NCERT Class V EVS textbook chapter 'Whose Forests?'. Suryamani, from Jharkhand, explains that her organisation is named 'Torang', which means jungle.",
    64: "The pitcher plant has pitcher-shaped leaves with a lid-like cover, attracts insects with its smell, and traps and digests small animals such as insects and even frogs. It grows in warm, humid places, not in cold deserts, so statement C is wrong.",
    65: "In Srinagar, 'Dongas' are boats on which many families live on the lake, not houses built in hilly areas. The other statements — stone, brick and wood houses, 'dab' windows and the Dal Lake houseboats — are true.",
    66: "The CBSE final answer key gives option 4 (A and D). A is correct: a hive has one queen who lays eggs. D is correct: worker bees search for nectar and dance to show other bees where the flowers are. B is wrong, because the hive is built by the worker bees, not by the males. Note: statement C (worker bees are females, far outnumber the males and look after the young) is also generally true of honeybees, so this answer may be disputed; it is shown here exactly as CBSE published it.",
    67: "Elephants live in herds, and the oldest female leads the herd and takes its decisions. Statements B and C give the herd size and the age at which males leave the herd incorrectly, so the answer is A and D.",
    68: "Al-Biruni, who visited India about a thousand years ago, wrote that its people were very skilled at building ponds and tanks, and described tanks with separate steps for going up and coming down. This appears in the NCERT Class V EVS chapter 'Every Drop Counts'.",
    69: "This question follows the NCERT Class V EVS chapter 'Whose Forests?', which states that under the Right to Forest Act passed in 2007, people who have lived in a forest for at least 25 years have a right over the forest land and what grows on it.",
    70: "Both statements are true: domestication happened slowly in many parts of the world, and sheep and goats were among the earliest domesticated animals. But R only names early domesticated animals; it does not explain why domestication was gradual.",
    71: "Harappans reared sheep, goats, cattle and buffalo. There is no clear evidence that they reared horses.",
    72: "Chhattisgarh became a state in 2000, Telangana in 2014 and Ladakh a Union Territory in 2019. Puducherry, Goa, Sikkim, Madhya Pradesh, Jammu and Kashmir and Arunachal Pradesh were formed earlier.",
    73: "Karnam Malleswari is a weightlifter. She won a bronze medal at the 2000 Sydney Olympics, becoming the first Indian woman to win an Olympic medal.",
    74: "Madhubani (Mithila) painting comes from the Mithila region of Bihar. It was traditionally made with a paste of powdered rice mixed with colours. It is not from Rajasthan, not based on Mughal art, and not floor painting with brush and indigo.",
    75: "Floors are coated with a mixture of cow dung and mud because cow dung helps keep the inside of the house cool and keeps insects away. So R is the correct explanation of A.",
    76: "Peer assessment is a technique of assessment; a rubric-based rating scale is a tool of assessment; assessment as learning means learners reflect on and direct their own learning (self-learning); and a paper-pencil test is typically used for summative assessment. This matches option 3.",
    77: "Children are naturally curious and learn well in collaborative groups. They are active learners rather than passive recipients, and they also learn outside the teacher's presence, so A and D are correct.",
    78: "EVS is about observing, asking questions and experimenting to understand one's surroundings. Merely accumulating facts is not its purpose, so B, C and D best describe it.",
    79: "Knowing how children learn EVS — their ideas, experiences and ways of making sense of the world — is the most important knowledge for an EVS teacher, because it shapes how content and teaching methods are chosen.",
    80: "Letting Harleen observe animals eating plants with and without thorns allows her to find the answer through her own observation and inquiry, which is the aim of EVS pedagogy. Simply telling her the answer ends her curiosity.",
    81: "Guiding Isha to notice a pattern herself — animals with visible ears, like cows, usually give birth, while animals whose ears cannot be seen, like birds, usually lay eggs — builds observation and reasoning instead of just handing her an answer.",
    82: "Contextual stories, folk stories and stories written by students connect EVS to children's lives and cultures. Stories mainly meant to teach morals are less suited to building EVS concepts, so the answer is A, B and C.",
    83: "The teacher should respect Poonam's imagination and understand her thinking by asking why she combined parts of different animals and what she calls it. Scolding her or saying such an animal doesn't exist would discourage her creativity.",
    84: "Identifying plants by the smell of crushed leaves and making pictures from collected leaves are hands-on activities that let children experience the variety of plants directly. So C and D are the most suitable.",
    85: "EVS is learnt by observing and experimenting with one's surroundings. Established facts, mere information and scientific terminology are not its essence, so the answer is C and E.",
    86: "NCF 2005 recommends moving away from rote learning and softening the sharp boundaries between subjects so that knowledge is connected. Both statements are true.",
    87: "A working model, such as a globe turned in front of a lamp, lets Chinu see how the Earth's rotation causes day and night. It makes the idea concrete in a way diagrams or stories cannot.",
    88: "EVS classrooms bring together children of many cultures, and respecting this diversity is a challenge teachers must meet. Every child should feel that their community, culture and way of life matter. Both statements are true.",
    89: "Discussion builds social interaction, supports authentic and meaningful learning, and helps children construct knowledge by sharing ideas. It suits all children, not only emotionally balanced ones, so the answer is A, B and C.",
    90: "Collecting different types of leaves requires children to observe their features and sort them into groups, so the activity develops observation and classification.",
}


def tidy(text):
    text = text.replace("``", "“").replace("''", "”").replace("--", "—").replace("�", "–")
    text = re.sub(r"`\s*([^`'’]*)'", r"‘\1’", text)
    return re.sub(r"[ \t]{2,}", " ", text).strip()


BREAK_BEFORE = re.compile(r"^(Assertion|Reason|Choose|[A-E]\.\s|[AB] :|\((i|ii|iii|iv)\)\s|The correct statements|"
                          r"The characteristics|This type|On which|Which of the following process)")


def stem_text(n, raw):
    if n in STEMS:
        return STEMS[n]
    out = []
    for line in raw.split(" / "):
        # Two statements printed side by side ("A. ...   B. ...") go on separate lines.
        for part in re.split(r"\s{3,}(?=[A-E]\.\s)", line):
            part = tidy(part)
            if out and not BREAK_BEFORE.match(part):
                out[-1] += " " + part
            else:
                out.append(part)
    return "\n".join(out)


questions, ids = [], []
for n in range(1, 91):
    if n in SKIP:
        continue
    q = extracted[n]
    options = OPTIONS.get(n) or [OPTION_FIXES.get((n, i + 1), o) for i, o in enumerate(q["options"])]
    options = [tidy(o) for o in options]
    stem = stem_text(n, q["stem"])
    assert q["key"] in "1234", (n, q["key"])
    assert all(options) and "–" not in stem or n in (57, 67, 76), (n, stem)
    assert "�" not in stem + "".join(options), n
    questions.append({
        "id": qid(n),
        "subject_id": TOPICS[n].split(".")[0],
        "topic_id": TOPICS[n],
        "text": {"en": stem},
        "options": [{"id": str(i + 1), "text": {"en": o}} for i, o in enumerate(options)],
        "correct_option_id": q["key"],
        "explanation": {"en": EXPLAIN[n]},
        "source": f"CBSE, CTET February 2026, Paper I, Set S (7 Feb 2026), question {n}. Answer from the CBSE final "
                  f"answer key. Explanation written by UPTET Saathi.",
        "verification_status": "verified",
    })
    ids.append(qid(n))

paper = {
    "id": PAPER_ID,
    "title": {"en": "CTET February 2026 · Paper I (7 Feb, Set S) · CDP, Maths, EVS",
              "hi": "सीटीईटी फ़रवरी 2026 · प्रश्नपत्र I (7 फ़रवरी, सेट S) · बाल विकास, गणित, पर्यावरण अध्ययन"},
    "year": 2026,
    "paper_code": "CTET-P1-070226-S",
    "is_official_pyq": True,
    "distribution_cleared": True,
    "duration_minutes": 90,
    "marking": {"correct": 1, "incorrect": 0, "unanswered": 0},
    "pdf_asset": "assets/pdfs/ctet-feb26-p1-07feb-s.pdf",
    "source": "Central Board of Secondary Education (CBSE): CTET February 2026 Paper I question booklet, Set S "
              "(exam on 7 February 2026), and the CBSE final answer key, published at ctet.nic.in. Parts I–III "
              "(questions 1–90); question 16 is left out because the final key accepts two answers. "
              "Explanations are by UPTET Saathi, not CBSE.",
    "question_count": len(ids),
    "question_ids": ids,
}

pack = json.load(open(pack_path, encoding="utf-8"))
assert not any(p["id"] == PAPER_ID for p in pack["papers"]), "paper already imported"
for subject in pack["subjects"]:
    existing = {t["id"] for t in subject["topics"]}
    for tid, en, hi in NEW_TOPICS.get(subject["id"], []):
        if tid not in existing:
            subject["topics"].append({"id": tid, "name": {"en": en, "hi": hi}})
for p in pack["papers"]:
    p.setdefault("distribution_cleared", True)  # existing papers are original content
    # keep key order readable: put distribution_cleared after is_official_pyq
    items = list(p.items())
    p.clear()
    for k, v in items:
        if k != "distribution_cleared":
            p[k] = v
        if k == "is_official_pyq":
            p["distribution_cleared"] = True
pack["papers"].insert(0, paper)
pack["questions"].extend(questions)
pack["content_version"] = "2026.10.28-sample.2"


# ---- Serialise in the file's existing style: small objects and options/topics on one line.
def inline(o):
    if isinstance(o, dict):
        return "{ " + ", ".join(f"{json.dumps(k)}: {inline(v)}" for k, v in o.items()) + " }"
    if isinstance(o, list):
        return "[" + ", ".join(inline(v) for v in o) + "]"
    return json.dumps(o, ensure_ascii=False)


def dump(o, ind=0, key=None):
    pad, inner = "  " * ind, "  " * (ind + 1)
    if isinstance(o, dict):
        if key in ("name", "marking") or len(inline(o)) <= 110:
            return inline(o)
        body = ",\n".join(f"{inner}{json.dumps(k)}: {dump(v, ind + 1, k)}" for k, v in o.items())
        return "{\n" + body + "\n" + pad + "}"
    if isinstance(o, list):
        if key == "question_ids":
            rows = [", ".join(json.dumps(v) for v in o[i:i + 5]) for i in range(0, len(o), 5)]
            return "[\n" + ",\n".join(inner + r for r in rows) + "\n" + pad + "]"
        if key in ("options", "topics"):
            return "[\n" + ",\n".join(inner + inline(v) for v in o) + "\n" + pad + "]"
        return "[\n" + ",\n".join(inner + dump(v, ind + 1) for v in o) + "\n" + pad + "]"
    return json.dumps(o, ensure_ascii=False)


open(pack_path, "w", encoding="utf-8", newline="\n").write(dump(pack) + "\n")
print(f"added paper {PAPER_ID} with {len(ids)} questions; skipped {SKIP}")
