"""UPTET 2021 Junior (23 Jan 2022), Part III (Q61–90): Language II, English. English only."""

SOURCE = 'junior_ss21'
ID_PREFIX = 'j'
PAPER_LABEL = 'Junior level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.grammar': [61, 62, 63, 64, 65, 71, 72, 73, 74, 75, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    'eng.comprehension': [66, 67, 68, 69, 70, 76, 77, 78, 79, 80],
}

SKIP = {}

PASSAGES = {
    65: ('prose', [66, 67, 68, 69, 70], 2),
    75: ('prose', [76, 77, 78, 79, 80], 0,
         'Helicopters are very different from airplanes. They can do three things that airplanes cannot do. First, when '
         'airplanes move upward, they must also move forward, but helicopters can move straight up without moving ahead. '
         'Second, helicopters can fly backward, which airplanes cannot do. Third, helicopters can use their rotors to hover '
         'in the air, which is impossible for planes. Because helicopters can perform actions that airplanes cannot, they '
         'are used for different tasks. Since helicopters can take off without moving forward, they do not need a runway '
         'for take off. They are used in congested areas where there is no room for airplanes or in isolated areas, which '
         'do not have airports. Because they can hover, they are used on fire fighting missions to drop water on fires. '
         'They are used in logging operations to lift trees out of forests. Helicopters are used as air ambulances to '
         'airlift patients out of situations which are difficult to reach by conventional ambulances. The police use '
         'helicopters to follow suspects on the ground or to search for cars on the ground. Of course, helicopters have '
         'military uses because of their design and capabilities.'),
}

REPLACE = [("time to spare. 'Thus", "time to spare.' Thus"), ('pillar box to the street', 'pillar box in the street'),
           ('may it this fashion', 'may in this fashion'), ('the underlined word', 'the word'), ('Meterology', 'Meteorology'),
           ('twenty-kilometeres', 'twenty-kilometre'), ('"To chew the cud\'', '\'To chew the cud\''),
           ('by the woman."', 'by the woman.'), ("to America.'", 'to America.')]

FIX = {
    65: {'en': 'Point out the part of the sentence that has an error:\nYou are learning English (A) / for the last one year (B) '
               '/ but you show (C) / no improvement at all (D).'},
    75: {'options': {'d': ('Precious', None)}},
}

EXPLAIN = {
    61: ('An apiary is a place where bees are kept.', None),
    62: ('The "green-eyed monster" is jealousy (from Shakespeare\'s Othello).', None),
    63: ('"M.A." begins with a vowel sound ("em"), so it should be "an M.A.", not "a M.A.".', None),
    64: ('A negative statement takes a positive tag: People shouldn\'t drink and drive, should they?', None),
    65: ('An action continuing from the past up to now needs the present perfect continuous: "You have been learning '
         'English for the last one year", so the error is in part A.', None),
    66: ('The passage says the elderly lady "can spend the entire day writing a postcard".', None),
    67: ('"Work expands so as to fill the time available": given more time, the work takes up all of it.', None),
    68: ('A "pillar box" is a post box shaped like a pillar, where letters are posted.', None),
    69: ('The passage contrasts a busy man with a person of leisure, who takes the whole day for a small task.', None),
    70: ('The sentence means that however much time is available for a task, all of it gets used.', None),
    71: ('A collective noun takes a singular verb when the group acts as one: "The committee was one on this point." When '
         'members differ, the plural is used: "The committee were divided."', None),
    72: ('"I wandered lonely as a cloud" compares using "as", so it is a simile.', None),
    73: ('Active voice: subject (the woman) + verb in the same tense (showed) + objects: The woman showed the visitors the '
         'new-born.', None),
    74: ('"Adverse" means unfavourable or hostile, so its antonym is "friendly".', None),
    75: ('The proverb is "Blood is thicker than water": family ties are stronger than other relationships.', None),
    76: ('"Congested" means overcrowded, with no free space; the passage uses it for places with no room for airplanes.', None),
    77: ('To "hover" is to stay in one place in the air.', None),
    78: ('In "Helicopters can perform actions", "perform" is the main verb.', None),
    79: ('The passage says helicopters airlift patients from places that are difficult to reach by ordinary ambulances.', None),
    80: ('In "very different", "very" modifies the adjective "different", so it is an adverb.', None),
    81: ('Entomology is the scientific study of insects.', None),
    82: ('The reported question "why he was looking" becomes the direct question: "Why are you looking through the '
         'keyhole?" I said.', None),
    83: ('Habits take the simple present (writes, know) and an action in progress the present continuous (is doing).', None),
    84: ('"Cantankerous" means bad-tempered and quarrelsome.', None),
    85: ('In "This kind of question", "this" points out the noun "kind", so it is a demonstrative adjective.', None),
    86: ('"To chew the cud" means to think over something slowly, to meditate.', None),
    87: ('We are ashamed "of" something: He was very much ashamed of his mischief.', None),
    88: ('"Had he stood first" is the inverted form of "If he had stood first", used in a past conditional.', None),
    89: ('"Latter" means the second of two: of the sword and the pen, the latter (the pen) is more powerful.', None),
    90: ('"Mis-" gives misbehave, misguide and misuse.', None),
}
