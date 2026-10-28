"""UPTET 2018 Primary, Part III (Q61–90): Language II, English. English only."""

SOURCE = 'primary18'
ID_PREFIX = 'p'
PAPER_LABEL = 'Primary level paper'
RANGE = (61, 90)
SUBJECT = 'eng'

TOPICS = {
    'eng.grammar': [61, 62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 88,
                    89, 90],
    'eng.pedagogy': [68, 69],
    'eng.comprehension': [78, 79],
}

SKIP = {}

PASSAGES = {77: ('prose', [78, 79], 3)}

REPLACE = [('historical backgound', 'historical background'), ('very intellingent', 'very intelligent'),
           ('His crueltly', 'His cruelty')]

FIX = {
    90: {'options': {'d': ("One who does not love one's country is a wretched person.", None)}},
}

EXPLAIN = {
    61: ('"Mice" is the plural of "mouse". Dog, fox and goat are singular.', None),
    62: ('"Mathematics" ends in -s but is treated as singular: Mathematics is my favourite subject.', None),
    63: ('In "I requested him to come in time" the subject "I" does the action, so it is active. The others use '
         'was + past participle and are passive.', None),
    64: ('"He was assisted by a group of students" uses was + past participle with "by", so it is passive.', None),
    65: ('"The" is the definite article, used here before "man" and "police".', None),
    66: ('"Students" can be boys or girls, so it is a noun of common gender.', None),
    67: ('"Was going" (was/were + -ing) is the past continuous tense.', None),
    68: ('Language skills develop in the order listening, speaking, reading and writing, so learning starts with '
         'listening.', None),
    69: ('Poetry recitation in class is mainly meant to help children enjoy the rhythm and feel of a poem and '
         'appreciate it.', None),
    70: ('"European" begins with a "yoo" (consonant) sound, so it takes "a"; "elephant" begins with a vowel sound, so '
         'it takes "an".', None),
    71: ('"Describe" is a transitive verb and takes its object directly, without "about": Please describe the story.', None),
    72: ('We say "accused of" a crime: He was accused of murder.', None),
    73: ('"Innocent" means not guilty, so its antonym is "guilty".', None),
    74: ('"Significant" means important or meaningful.', None),
    75: ('"Ox" becomes "oxen" with the suffix -en; box, tax and max take -es.', None),
    76: ('The blank needs a possessive pronoun that stands alone, like "mine": This dress is yours and that one is mine.', None),
    77: ('Present perfect question in the passive: Has + object + been + past participle: Has this question been asked '
         'by the girls?', None),
    78: ('Gangapur is the name of a particular village, so it is a proper noun.', None),
    79: ('In "two brave children", "brave" describes the noun "children", so it is an adjective.', None),
    80: ('Gold is a substance from which things are made, so it is a material noun.', None),
    81: ('"Connection" names an idea or relation that cannot be touched, so it is an abstract noun.', None),
    82: ('"Adversity" (hardship, bad luck) is a state or condition, so it is an abstract noun.', None),
    83: ('In "He is working hard", "hard" tells us how he works, so it modifies the verb and is an adverb.', None),
    84: ('"But" joins the two clauses "She is poor" and "she is by nature hospitable", so it is a conjunction.', None),
    85: ('The present perfect uses has/have + past participle: I have finished my work.', None),
    86: ('The correct spelling is "derogatory".', None),
    87: ('In "I killed a snake", the verb "killed" has an object ("a snake"), so it is transitive.', None),
    88: ('"He does not listen to me" contains "not", so it is a negative sentence.', None),
    89: ('"What a piece of work is man" expresses strong feeling (wonder), so it is an exclamatory sentence.', None),
    90: ('The sentence has a main clause and a relative clause ("who does not love one\'s country"), so it is complex.', None),
}
