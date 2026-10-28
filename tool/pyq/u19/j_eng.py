"""UPTET 2019 Junior, Part III (Q61–90): Language II, English. English only; shared by both junior papers."""

SOURCE = 'junior_ms'
ID_PREFIX = 'j'
PAPER_LABEL = 'Junior level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.grammar': list(range(61, 81)) + list(range(85, 91)),
    'eng.comprehension': [81, 82, 83, 84],
}

SKIP = {84: 'the two published keys give different answers'}

PASSAGES = {80: ('verse', [81, 82], 3), 82: ('prose', [83, 84], 3)}

REPLACE = [('Both (c) and (d)', 'Both C and D'), ('on thy cold gray stones', 'On thy cold gray stones')]

FIX = {
    73: {'en': "Which of the following sentences has a 'modal verb'?"},
    90: {'options': {'d': ('I bought a chain and it was beautiful', None)}},
}

EXPLAIN = {
    61: ('The sentence is in the past tense, so it needs the past form "led" (from "lead").', None),
    62: ('A drake is a male duck. Roe (female deer), countess and peahen are feminine.', None),
    63: ('"Could I borrow some money from you, please?" is a polite request. The others are an exclamation, a wish and '
         'a statement.', None),
    64: ('Every letter in "cattle" is sounded. Psychology has a silent p, doubt a silent b and knowledge a silent k.', None),
    65: ('"Unless" means "if not": You will not succeed unless you work harder.', None),
    66: ('Reported words go inside quotation marks after a comma, with commas separating the items in the list.', None),
    67: ('The sentence already has "not", so it needs "anybody"; "nobody" would make a double negative.', None),
    68: ('The opposite of "justice" is formed with the prefix in-: injustice.', None),
    69: ('"Adroit" means skilful or clever with the hands or mind; the key gives "skilled".', None),
    70: ('In reported speech the question becomes a statement, "said to" becomes "asked" and "you" becomes "I": He asked '
         'me when I would come (here, "go") back. Option (b) is the only one with the right pronoun and word order.', None),
    71: ('Active voice: subject (a cruel boy) + verb in the same tense (killed) + object (the bird).', None),
    72: ('"He kept me waiting" becomes "I was kept waiting by him": the object "me" becomes the subject "I".', None),
    73: ('"Must" is a modal verb. Modals (can, could, may, must, should, will...) express ability, permission or '
         'necessity.', None),
    74: ('After "with" we need a noun: "with ease".', None),
    75: ('"Rama and I" is the subject of "were", so the subject pronoun "I" is used, not "me".', None),
    76: ('"Ingenious" (clever and inventive) describes a noun, so it is an adjective.', None),
    77: ('The feminine of "bachelor" is "spinster".', None),
    78: ('In the simple present, the negative uses "does not" + the base verb: This boy does not play football.', None),
    79: ('A question in the simple present uses "Does" + subject + base verb: Does Madhusudan know how to cheat?', None),
    80: ('Most nouns, including "taxi", form the plural with -s: taxis.', None),
    81: ('In "my tongue could utter the thoughts", "utter" means to speak or express in words.', None),
    82: ('In Tennyson\'s "Break, Break, Break" the poet grieves for a lost friend; the mood is sad and pessimistic.', None),
    83: ('A "frustrater" blocks or defeats something; the passage contrasts it with a city that enhances life. The '
         'opposite is "promoter".', None),
    85: ('We say "a genius for" an activity and "a genius in" a subject: genius for military tactics, genius in '
         'Mathematics.', None),
    86: ('"Cut out for" means naturally suited to: Priya is not cut out for this kind of job.', None),
    87: ('Iron is a substance from which things are made, so it is a material noun.', None),
    88: ('When a number is used as an adjective before a noun, the noun stays singular: a five-rupee note, four five '
         'rupee notes.', None),
    89: ('The key takes the whole phrase "Every boy along with his parents" as the subject. The verb "is" agrees with '
         '"every boy", because "along with his parents" does not change the number.', None),
    90: ('"Which was beautiful" describes the noun "chain", so it is an adjective clause. In (c) "because..." is an '
         'adverb clause.', None),
}
