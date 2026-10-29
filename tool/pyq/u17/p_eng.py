"""UPTET 2017 Primary, Part III (Q61–90): Language II, English. English only."""

SOURCE = 'primary17'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.grammar': [61, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    'eng.comprehension': [81, 83, 84, 85, 86, 87, 88, 89, 90],
}

SKIP = {
    65: 'none of the options joins the sentences correctly ("not strong enough to keep us awake")',
    82: 'the solved paper drops the passage line that uses the word "desert"',
}

# The solved paper prints both passages with a line missing. The first keeps only what it prints in full; the second
# gets back the sentence about half-educated readers from the original essay (Lafcadio Hearn, "On Reading").
PASSAGES = {
    80: ('prose', [81, 83, 84, 85], 3,
         'Antarctica is an icy continent in the South Pole. It is covered by permanently frozen ground and is surrounded '
         "by water. 98% of the land is covered with a continental ice sheet; the remaining 2% of land is barren rock. "
         "Antarctica has about 87% of the world's ice. The South Pole is the coldest, windiest and driest place on "
         'Earth. The coldest temperature ever recorded on Earth was at the South Pole; it reached as low as -128.6 °F '
         'or -88.0 °C. On an average most of the Antarctica gets less than 2 inches of snow each year. Although '
         'scientific expeditions visit Antarctica, there are no permanent human residents. This is because of the '
         'extreme weather, which includes freezing temperature, strong winds and blizzards. There are about 4000 '
         "seasonal visitors to Antarctica. Antarctica hasn't always been located at the South Pole. It has drifted, "
         'like the other continents and has ranged from the Equator during the Cambrian period, about 500 million '
         'years ago to the South Pole. During the time of the dinosaurs, Antarctica was more temperate and housed '
         'dinosaurs and many other life-forms. Now there is very little indigenous life.'),
    85: ('prose', [86, 87, 88, 89, 90], 3,
         'The first thing which a scholar should bear in mind is that a book ought not to be read for mere amusement. '
         'Half-educated persons read books for amusement, and are not to be blamed for it; they are incapable of '
         'appreciating the deeper qualities that belong to a really great literature. But a young man who has passed '
         'through a course of University training should discipline himself at an early day never to read for mere '
         'amusement. And once the habit of discipline has been formed, he will find it impossible to read for mere '
         'amusement. He will then impatiently throw down any book from which he cannot obtain intellectual food, any '
         'book which does not make an appeal to the higher emotions and to his intellect. But on the other, the habit '
         'of reading for amusement becomes with thousands of people exactly the same kind of habit as wine-drinking '
         'or opium-smoking; it is like a narcotic, something that helps to pass the time, something that keeps up a '
         'perpetual condition of dreaming, something that eventually results in destroying all capacity for thought, '
         'giving exercise only to the surface parts of the mind and leaving the deeper springs of feelings and the '
         'higher faculties of perception unemployed.'),
}

REPLACE = [('“Will I know your father?', '“Will I know your father?”'), ('superlative from of adverb', 'superlative form of adverb')]

FIX = {
    90: {'options': {'d': ('unused', None)}},
}

EXPLAIN = {
    61: ('"As cheerful as a lark" is the fixed simile; larks are known for their cheerful song.', None),
    62: ('It has a main clause ("This is the house") and a dependent clause ("in which I was born"), so it is a complex '
         'sentence.', None),
    63: ('"Beyond" is a preposition (beyond the hills). "And" and "yet" are conjunctions; "now" is an adverb.', None),
    64: ('"Apace" is an adverb meaning quickly (work went on apace).', None),
    66: ('"Each other" is the reciprocal pronoun for two people who are fond of one another.', None),
    67: ('A misanthrope is a person who hates mankind.', None),
    68: ('"Let the book be given" is the passive of the command "Give the book."', None),
    69: ('In direct speech, "asked if I might know" becomes the question "May I know your father?", introduced by "I '
         'said to Sheela".', None),
    70: ('We are responsible to a person and for a thing, so ministers are responsible to the Chief Minister.', None),
    71: ('"As" gives the reason: as he had not paid his bill, his electricity was cut off.', None),
    72: ('Death is given a human action ("lays his icy hand"), so this is personification.', None),
    73: ('Demography is the study of population. Genealogy is the study of family history.', None),
    74: ('The proverb means it is better to keep what you have than to risk it for something more that you may not get.',
         None),
    75: ('A bell chimes, jingles or rings. "Dang" is not a word for the sound of a bell.', None),
    76: ('We are sorry for something we have done.', None),
    77: ('To attenuate means to make thin or weaken.', None),
    78: ('"The servant ran away and added to their troubles" joins two main clauses with "and", so it is compound.',
         None),
    79: ('The adjective "suspicious" takes the preposition "of": suspicious of someone.', None),
    80: ('"Want" is a stative verb and is not normally used in the continuous form, so "The Headmaster wants to speak to '
         'you."', None),
    81: ('"Icy" describes the noun "continent", so it is an adjective.', None),
    83: ('"Windiest" is the superlative form of the adjective "windy".', None),
    84: ('The passage says Antarctica has not always been at the South Pole; it drifted there from the Equator.', None),
    85: ('The passage says that in the time of the dinosaurs Antarctica was temperate and housed dinosaurs.', None),
    86: ('The passage says half-educated persons are incapable of appreciating the deeper qualities of really great '
         'literature.', None),
    87: ('Reading for amusement is compared to a narcotic, that is, an intoxicant that dulls the mind.', None),
    88: ('"The higher faculties of perception" are the higher mental powers needed to understand great literature.', None),
    89: ('"Eventually" means in the end, at last.', None),
    90: ('The higher faculties are left "unemployed", that is unused, because reading for amusement never exercises them.',
         None),
}
