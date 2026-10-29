"""UPTET 2017 Junior (Social Studies), Part III (Q61–90): Language II, English. English only."""

SOURCE = 'junior_ss17'
ID_PREFIX = 'j'
PAPER_LABEL = 'Junior level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.comprehension': [61, 62, 64, 86, 87, 88, 89, 90],
    'eng.grammar': [63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85],
}

SKIP = {}

PASSAGES = {60: ('prose', [61, 62, 63, 64, 65], 3), 85: ('prose', [86, 87, 88, 89, 90], 3)}

REPLACE = [('It corosses all', 'It crosses all'), ('half a hour', 'half an hour'),
           ('Helicopters can perform actions that airplanes cannot, they', 'Because helicopters can perform actions that '
                                                                           'airplanes cannot, they')]

FIX = {
    67: {'en': 'Complete the sentence with the most appropriate choice: He was very much ashamed ……… his mischief.'},
    68: {'en': 'Complete the sentence with the most appropriate choice: ……… he stood first, he would have gone to America.'},
    69: {'en': 'Complete the sentence with the most appropriate choice: Of the sword and pen, the ……… is more powerful.'},
    90: {'options': {'d': ('If you have some important work to do, you should always have some additional time.', None)}},
}

EXPLAIN = {
    61: ('"Congested" means overcrowded, with no room to spare. The passage contrasts congested areas with places that '
         'have room for airplanes.', None),
    62: ('To hover is to stay in one place in the air, as the passage explains with the rotors.', None),
    63: ('"Perform" is an action word in "Helicopters can perform actions", so it is a verb.', None),
    64: ('The passage says helicopters airlift patients from places that conventional ambulances find difficult to reach.',
         None),
    65: ('"Very" modifies the adjective "different" in "very different", so it is an adverb.', None),
    66: ('"To chew the cud" means to think something over slowly, to meditate.', None),
    67: ('We are ashamed of something we have done.', None),
    68: ('"Had he stood first" is the inverted form of "If he had stood first", which goes with "would have gone".', None),
    69: ('"The latter" refers to the second of two things named, here the pen.', None),
    70: ('"Mis-" gives misbehave, misguide and misuse.', None),
    71: ('A collective noun takes a singular verb when the group acts as one: "The committee was one on this point." When '
         'members differ, the plural is used ("The committee were divided"), so (c) is not the best answer.', None),
    72: ('"Lonely as a cloud" compares using "as", so it is a simile. "Life is a dream" is a metaphor.', None),
    73: ('Active voice: subject "the woman", verb "showed", objects "the visitors" and "the newborn".', None),
    74: ('"Adverse" means harmful or hostile; its opposite is "friendly".', None),
    75: ('The proverb is "Blood is thicker than water": family ties are the strongest.', None),
    76: ('An apiary is a place where bees are kept.', None),
    77: ('"The green-eyed monster" is jealousy, a phrase from Shakespeare\'s Othello.', None),
    78: ('"MA" begins with a vowel sound (em-ay), so it takes "an": He is an MA.', None),
    79: ('A negative statement takes a positive tag with the same auxiliary: "shouldn\'t ... should they?"', None),
    80: ('An action continuing up to now needs the present perfect continuous: "You have been learning English for the '
         'last one year".', None),
    81: ('Entomology is the scientific study of insects. Mycology is the study of fungi.', None),
    82: ('The reported question becomes "Why are you looking through the keyhole?" in direct speech.', None),
    83: ('Habits take the simple present ("writes", "know") and an action going on now takes the present continuous ("is '
         'doing").', None),
    84: ('"Cantankerous" means bad-tempered and quarrelsome.', None),
    85: ('"This" in "This kind of question" points to a noun, so it is a demonstrative adjective.', None),
    86: ('The passage says the elderly lady at leisure can spend the entire day writing a postcard.', None),
    87: ('"Work expands so as to fill the time available": when more time is given, the work takes up all of it.', None),
    88: ('A pillar-box is a pillar-shaped postbox in the street.', None),
    89: ('The passage shows that a person at leisure takes far longer than a busy one to do the same work.', None),
    90: ('The sentence means that whatever time is available for a piece of work, all of it gets used.', None),
}
