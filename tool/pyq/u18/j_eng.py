"""UPTET 2018 Junior, Part III (Q61–90): Language II, English. English only."""

SOURCE = 'junior_ss18'
ID_PREFIX = 'j'
PAPER_LABEL = 'Junior level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.comprehension': [61, 62],
    'eng.pedagogy': [87, 88],
    'eng.grammar': list(range(63, 87)) + [89, 90],
}

SKIP = {}

PASSAGES = {60: ('prose', [61, 62], 3)}

FIX = {
    65: {'en': 'Complete the following sentence with the most appropriate word: Let us not confuse liberty............ license.'},
    72: {'en': 'Identify the phrasal verb in the following sentence: "Thieves broke into the bank in the middle of the night."'},
    90: {'options': {'d': ('No man', None)}},
}

EXPLAIN = {
    61: ('A "hobo" is a homeless wanderer without regular work, like Jacob, who tramped across the United States and '
         'Canada.', None),
    62: ('Scurvy is a disease caused by a lack of vitamin C; the passage says Jacob came back from Alaska suffering '
         'from it.', None),
    63: ('The plural of "sheep" is "sheep", so "sheeps" is wrong.', None),
    64: ('The answer key accepts "Please see my certificates." The other options misuse prepositions with "see" and '
         '"overlook".', None),
    65: ('We confuse one thing "with" another: Let us not confuse liberty with license.', None),
    66: ('"Though" joins two ideas that contrast: He lost the prize though he tried his best.', None),
    67: ('The predicate tells what the subject does: "play football in the park". "My friends and I" is the subject.', None),
    68: ('The feminine of "wizard" is "witch".', None),
    69: ('A vixen is a female fox, so the masculine is "fox".', None),
    70: ('Reported words go in double quotation marks after a comma, begin with a capital letter, and the full stop '
         'goes inside the closing quotes.', None),
    71: ('"Prevent" takes -ive (preventive), -able (preventable) and -ing (preventing), but not -ious.', None),
    72: ('"Broke into" (verb + preposition, meaning entered by force) is a phrasal verb.', None),
    73: ('With "didn\'t" the sentence is already negative, so it needs "anybody": I didn\'t know anybody in the party.', None),
    74: ('Homophones sound the same but differ in meaning. "Kite" and "kit" sound different, so they are not homophones.', None),
    75: ('Every letter in "orange" is sounded. Honest has a silent h, knock a silent k and debt a silent b.', None),
    76: ('"Who" stands for "those" and joins the clause, so it is a (relative) pronoun.', None),
    77: ('"So" joins two clauses and shows result, so it is a conjunction.', None),
    78: ('"Ought to" is a modal verb expressing duty or likelihood.', None),
    79: ('"Ours" is a possessive pronoun standing on its own for "our country".', None),
    80: ('"Cattle" names a group of animals and is a collective noun (always plural).', None),
    81: ('"He will be taken care of" uses will be + past participle, so it is passive.', None),
    82: ('"I know nothing about western philosophy" has the subject doing the action, so it is active voice.', None),
    83: ('"How beautiful is the morning today!" expresses strong feeling and ends with "!", so it is exclamatory.', None),
    84: ('The "l" in "calm" is silent.', None),
    85: ('Direct narration quotes the speaker\'s exact words in quotation marks: He said to me, "Do not cross the limit."', None),
    86: ('"Broad" is the antonym of "narrow".', None),
    87: ('NCF 2005 describes learning as active and social: children construct knowledge by doing and by interacting '
         'with others.', None),
    88: ('Motivation creates interest and the desire to learn, which keeps learners engaged.', None),
    89: ('We say "worthy of": Ashoka is worthy of remembrance.', None),
    90: ('"No man" is the subject; "can serve two masters" is the predicate.', None),
}
