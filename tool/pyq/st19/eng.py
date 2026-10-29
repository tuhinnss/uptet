"""Super TET 2019, Q31–40: English."""

RANGE = (31, 40)
LANGUAGE = 'en'

TOPICS = {
    'eng.comprehension': [31, 32],
    'eng.grammar': [33, 34, 35, 36, 37, 38, 39, 40],
}

SKIP = {}

FIX = {
    # The underline does not survive in the text, so the word is named.
    36: {'en': 'Identify the part of speech of the underlined word (‘enough’) in the following sentence:\n'
               'He is intelligent enough to solve this sum.'},
}

EXPLAIN = {
    31: ('In the passage, oil will be “depleted”, that is, used up until none is left. The opposite is to regenerate: '
         'to grow or be produced again. To empty is a synonym, and quench and inflate are unrelated.', None),
    32: ('The author says that “in the field of economics, the tree of ideology has never bore any fruit”. In other '
         'words, ideology has barely yielded any result, and pragmatism is the only cure for poverty.', None),
    33: ('A sentence with the indefinite pronoun “one” as subject keeps “one’s” for the possessive: one should love '
         'one’s country. “His” is also heard in informal use, but the formal pattern is one … one’s.', None),
    34: ('Although English has only 5 vowel letters and 21 consonant letters, it has about 20 vowel sounds '
         '(12 pure vowels and 8 diphthongs) and 24 consonant sounds, 44 sounds in all.', None),
    35: ('In direct speech Atul speaks to his friend in his own words: the reported “he could make use of his bike '
         'while he was away” becomes “You can make use of my bike while I am away.” The pronouns change to you/my/I '
         'and the past forms could/was go back to can/am.', None),
    36: ('“Enough” here modifies the adjective “intelligent” (intelligent to what degree?), so it is an adverb. '
         'Adverbs of degree such as very, too and enough modify adjectives.', None),
    37: ('The sentence is inverted. In normal order it reads “A hermit lives on the top of the hill”, so the subject '
         'is “a hermit”. “On the top of the hill” is an adverbial phrase of place.', None),
    38: ('Hide is an irregular verb: hide – hid – hidden. The simple past is “She hid her face for shame.” '
         '“Hidden” is the past participle and “hidded” is not a word.', None),
    39: ('A sentence that expresses strong feeling and begins with “How” or “What” and ends with “!” is exclamatory.', None),
    40: ('The choice of “a” or “an” depends on the first sound, not the first letter. FIR is read “eff-eye-ar”, '
         'which begins with a vowel sound, so “an FIR” is correct. European (“yoo”), one (“wun”) and unit (“yoo”) '
         'begin with consonant sounds and take “a”.', None),
}
