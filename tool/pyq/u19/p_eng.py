"""UPTET 2019 Primary, Part III (Q61–90): Language II, English. English only."""

SOURCE = 'primary'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.grammar': [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 79, 80, 85, 86, 87, 88, 89, 90],
    'eng.pedagogy': [72, 73],
    'eng.comprehension': [81, 82, 83, 84],
}

SKIP = {}

PASSAGES = {80: ('prose', [81, 82], 5), 82: ('verse', [83, 84], 2)}

REPLACE = [('noblest from of revenge', 'noblest form of revenge'), ('Fair as star', 'Fair as a star')]

FIX = {
    66: {'en': 'Which of the following words is not a co-ordinating conjunction?'},
    85: {'en': 'Which of the following sentence/sentences is/are correct?\n'
               '(A) There is few hope of his recovery.\n(B) He showed few concern for his nephew.\n'
               '(C) He showed little mercy to the vanquished.'},
}

EXPLAIN = {
    61: ('"My watch was lost" uses was + past participle, so it is passive. The other sentences are active: their '
         'subjects perform the action.', None),
    62: ('The passive of an imperative sentence begins with "Let": Do it → Let it be done.', None),
    63: ('"Criteria" is the plural of "criterion". Crisis, analysis and index are singular; their plurals are crises, '
         'analyses and indices.', None),
    64: ('"Mice" is the plural of "mouse". Electronics, billiards and news end in -s but take a singular verb.', None),
    65: ('"Orphan" can refer to either a boy or a girl, so it is a noun of common gender.', None),
    66: ('But, for and and are co-ordinating conjunctions (they join equal clauses). "If" introduces a condition and is a '
         'subordinating conjunction.', None),
    67: ('We say "thirst for knowledge" and "leisure for something", so both blanks take "for".', None),
    68: ('In "a fast writer", "fast" describes the noun "writer", so it is an adjective. In "He writes fast" it would '
         'be an adverb.', None),
    69: ('"She reads what she likes" has a main clause and a noun clause ("what she likes"), so it is complex, not '
         'simple. The other sentences have only one finite verb.', None),
    70: ('"Will be playing" (will + be + -ing) is the future continuous tense, which older grammar books call the '
         'future imperfect tense.', None),
    71: ('In "All the female members have arrived" the subject is "female members", which is feminine. The other subjects '
         'are masculine.', None),
    72: ('The direct method teaches a foreign language by linking words directly with objects and actions, without '
         'translating into the mother tongue.', None),
    73: ('Comprehension of written English means understanding what has been read.', None),
    74: ('The verb "listen" takes the preposition "to": Please listen to your teacher.', None),
    75: ('"Believe" is a stative verb and is not normally used in the continuous form, so "I don\'t believe him" is '
         'correct and "I am not believing him" is wrong.', None),
    76: ('"All" with a plural noun takes "these" and the plural "men" (not "mans"): All these men are gentle.', None),
    77: ('"At" is used with exact points of time: at midnight, at noon, at 6 o\'clock.', None),
    78: ('In "I met him where he lived", "where he lived" tells us the place of the action, so it is an adverb clause. '
         'In the other sentences the "who/which" clause describes a noun and is an adjective clause.', None),
    79: ('Junior, senior, superior and inferior are followed by "to", not "than": He is junior to me.', None),
    80: ('"Either" pairs with "or": Either he is mad or he feigns madness.', None),
    81: ('"Strength" names a quality that cannot be seen or touched, so it is an abstract noun.', None),
    82: ('The passage says forgiving is a sign of strength and it "takes a strong character" to restrain the wish for '
         'revenge. So one who does not take revenge is a strong man.', None),
    83: ('"Untrodden" means not walked on, so "untrodden ways" are paths that are unexplored, far from people.', None),
    84: ('"Fair as a star" compares the maid to a star using "as", which makes it a simile.', None),
    85: ('"Few" is used with countable nouns and "little" with uncountable ones. Hope and concern are uncountable, so '
         '(A) and (B) should use "little"; only (C), "little mercy", is correct.', None),
    86: ('The past perfect uses had + past participle: "I had written my letter before he arrived".', None),
    87: ('"The" is used before ordinal numbers (the first man) and unique things (the moon).', None),
    88: ('"Hour" begins with a vowel sound because the h is silent, so it takes "an": an hour.', None),
    89: ('The plural of "ox" is "oxen", formed with the suffix -en.', None),
    90: ('Adding -th to "grow" gives the noun "growth".', None),
}
