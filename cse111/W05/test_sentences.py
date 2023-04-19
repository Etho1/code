from sentences import es_get_determiner, es_get_noun, es_get_verb, es_get_preposition, es_get_prepositional_phrase
import random
import pytest


def test_es_get_determiner():
    # 1. Test the single determiners.

    es_single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the es_get_determiner function which
        # should return a single determiner.
        es_word = es_get_determiner(1)

        # Verify that the es_word returned from es_get_determiner
        # is one of the words in the single_determiners list.
        assert es_word in es_single_determiners

    # 2. Test the plural determiners.

    es_plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the es_get_determiner function which
        # should return a plural determiner.
        es_word = es_get_determiner(2)

        # Verify that the es_word returned from es_get_determiner
        # is one of the words in the plural_determiners list.
        assert es_word in es_plural_determiners

def test_es_get_noun():
    # 1. Test the single determiners.

    es_single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the es_get_determiner function which
        # should return a single determiner.
        es_word = es_get_noun(1)

        # Verify that the es_word returned from es_get_determiner
        # is one of the words in the single_determiners list.
        assert es_word in es_single_nouns

    # 2. Test the plural determiners.

    es_plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the es_get_determiner function which
        # should return a plural determiner.
        es_word = es_get_noun(2)

        # Verify that the es_word returned from es_get_determiner
        # is one of the words in the plural_determiners list.
        assert es_word in es_plural_nouns

def test_es_get_verb():
    # 1. Test the single determiners.

    es_past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the es_get_determiner function which
        # should return a single determiner.
        es_word = es_get_verb(1,1)

        # Verify that the es_word returned from es_get_determiner
        # is one of the words in the single_determiners list.
        assert es_word in es_past_verbs

    # 2. Test the plural determiners.

    es_present_single_verb = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]


    for _ in range(4):
        es_word = es_get_verb(1,2)
        assert es_word in es_present_single_verb

    present_plural_verb = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]


    for _ in range(4):
        es_word = es_get_verb(2,2)
        assert es_word in present_plural_verb
    
    future_verb = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    for _ in range(4):
        es_word = es_get_verb(2,3)
        assert es_word in future_verb

def test_es_get_preposition():
    es_prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the es_get_determiner function which
        # should return a plural determiner.
        es_word = es_get_preposition()

        # Verify that the es_word returned from es_get_determiner
        # is one of the words in the plural_determiners list.
        assert es_word in es_prepositions
    
def test_es_get_prepositional_phrase():
    es_prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    es_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    es_determiners = ["a", "one", "the", "some", "many", "the"]
    for _ in range(4):
        phrase = es_get_prepositional_phrase(1 or 2)
        words = phrase.split()

        for i, es_word in enumerate(words):
            if i == 0:
                assert es_word in es_prepositions
            elif i == 1:
                assert es_word in es_determiners
            elif i == 2:
                assert es_word in es_nouns






pytest.main(["-v", "--tb=line", "-rN", __file__])