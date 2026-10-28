"""UPTET 2021 Primary (cancelled exam of 28 Nov 2021), Part III (Q61–90): Language II, English. English only."""

SOURCE = 'primary21'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.grammar': [61, 62, 63, 67, 68, 70, 71, 72, 74, 75, 76, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    'eng.comprehension': [64, 65, 77, 78],
    'eng.pedagogy': [66, 69],
}

SKIP = {73: 'none of the printed options is a plural noun'}

PASSAGES = {63: ('verse', [64, 65], 2), 76: ('prose', [77, 78], 2)}

REPLACE = [('promises to Keep', 'promises to keep'), ('The Ganga especially is river of India', 'The Ganga especially is the river of India')]

FIX = {
    64: {'options': {'c': ('Both A and B are correct', None)}},
    75: {'en': 'Fill in the blank with the correct word: Neither he is sorry............... his father.'},
    76: {'options': {o: (v, None) for o, v in zip('abcd', ['-en', '-s', '-ies', '-es'])}},
    87: {'options': {o: (v, None) for o, v in zip('abcd', ['-ies', '-ys', '-es', '-en'])}},
}

EXPLAIN = {
    61: ('"Strike the iron while it is hot" is a proverb: act while the chance lasts. "While" means "during the time that".', None),
    62: ('Polite requests become passive with "You are requested to...": You are requested to sit down.', None),
    63: ('"Bread and milk" is thought of as one dish, so it takes a singular verb: Bread and milk is a wholesome food.', None),
    64: ('In the poem, "flake" means a small, thin piece, here a snowflake.', None),
    65: ('"Deep" and "keep" end with the same sound, so they are rhyming words.', None),
    66: ('Using technology to improve teaching and learning is called ICT (Information and Communication Technology) '
         'in education.', None),
    67: ('"Will be leaving" (will + be + -ing) is the future continuous tense.', None),
    68: ('"He reads what he likes" has a main clause and a noun clause ("what he likes"), so it is complex.', None),
    69: ('The answer key gives the structural method, which teaches English through graded sentence patterns. Many '
         'English-medium teachers also use the direct method, so this question is open to debate.', None),
    70: ('The subject is the whole noun phrase "The beautiful rainbow"; "soon faded away" is the predicate.', None),
    71: ('"One-eyed" begins with a "w" sound, so it takes "a": a one-eyed man.', None),
    72: ('"Cattle" is always plural: The cattle are grazing.', None),
    74: ('"A letter was written by him" uses was + past participle with "by", so it is passive.', None),
    75: ('"Neither" pairs with "nor": Neither he is sorry nor his father.', None),
    76: ('Nouns ending in consonant + y change y to i and add -es: dictionary → dictionaries.', None),
    77: ('The passage says the Ganga "has been a symbol of India\'s age-long culture and civilization".', None),
    78: ('The author says the Ganga reminds him of the snow-covered peaks and deep valleys of the Himalayas and of the '
         'rich and vast plains below.', None),
    79: ('We congratulate someone "on" something: I must congratulate you on your exam results.', None),
    80: ('"European" begins with a "yoo" sound, so it takes "a".', None),
    81: ('Names of rivers take "the" (The Ganga), and "sacred river" here is one of many, so "a".', None),
    82: ('"Else" means "otherwise": Walk quickly, else you will not overtake him.', None),
    83: ('Names of trains take "the", and the superlative "fastest" also takes "the".', None),
    84: ('"Im-" gives improper, impolite, immortal and immovable.', None),
    85: ('"Humanity" names a quality, so it is an abstract noun. Gold and tea are material nouns; crowd is collective.', None),
    86: ('The plural of "maximum" is "maxima" (also "maximums").', None),
    87: ('"Memento" takes -es (mementoes); "mementos" is also used.', None),
    88: ('"Czarina" (tsarina) is the wife of a czar or a female ruler, so it is feminine.', None),
    89: ('We carry something "on" the head.', None),
    90: ('"Alumni" is the plural of "alumnus". Oasis, radius and stadium are singular.', None),
}
