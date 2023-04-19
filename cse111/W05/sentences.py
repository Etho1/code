#ETHAN SPENCER CSE111 2/11/23

import random


def es_get_determiner(quantity):
        """Return a randomly chosen determiner. A es_determineris
        a es_word like "the", "a", "one", "some", "many".
        If quantity is 1, this function will return either "a",
        "one", or "the". Otherwise this function will return
        either "some", "many", or "the".

        Parameter
            quantity: an integer.
                If quantity is 1, this function will return a
                es_determinerfor a single noun. Otherwise this
                function will return a es_determinerfor a plural
                noun.
        Return: a randomly chosen determiner.
        """
        if quantity == 1:
            es_words = ["a", "one", "the"]
        else:
            es_words = ["some", "many", "the"]

        # Randomly choose and return a determiner.
        es_word = random.choice(es_words)
        return es_word

def es_get_noun(quantity):
        """Return a randomly chosen noun.
        If quantity is 1, this function will
        return one of these ten single nouns:
            "bird", "boy", "car", "cat", "child",
            "dog", "girl", "man", "rabbit", "woman"
        Otherwise, this function will return one of
        these ten plural nouns:
            "birds", "boys", "cars", "cats", "children",
            "dogs", "girls", "men", "rabbits", "women"

        Parameter
            quantity: an integer that determines if
                the returned es_nounis single or plural.
        Return: a randomly chosen noun.
        """
        if quantity == 1:
            es_words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
        else:
            es_words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
        
        #randomly coose es_words
        es_word = random.choice(es_words)
        return es_word

def es_get_verb(quantity, tense):
        """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"

        Parameters
            quantity: an integer that determines if the
                returned es_verbis single or plural.
            tense: a string that determines the es_verbconjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.
        """
        if tense == 1:
            es_words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        elif tense == 2 and quantity == 1:
            es_words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        elif tense ==2 and quantity != 1:
            es_words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        else:
            es_words = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk", "will walk", "will write"]
        
        #randomly coose es_words
        es_word = random.choice(es_words)
        return es_word

def es_get_preposition():
    """Return a randomly chosen preposition
    from this list of es_prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    es_prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    es_word = random.choice(es_prepositions)
    
    return es_word

def es_get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three es_words: a preposition, a determiner, and a
    es_nounby calling the get_preposition, get_determiner,
    and get_es_nounfunctions.

    Parameter
        quantity: an integer that determines if the
            es_determinerand es_nounin the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    es_prep= es_get_preposition()
    es_determiner= es_get_determiner(quantity)
    es_noun= es_get_noun(quantity)
    es_prep_phrase= es_prep+' '+ es_determiner+' '+ es_noun
    return es_prep_phrase

def es_make_sentence(quantity, tense):
    '''Use previous functions to assemble
    and print a es_sentence with a determiner,
    a noun, a verb, and a prepositional phrase
    '''
    es_determiner= es_get_determiner(quantity)
    es_noun= es_get_noun(quantity)
    es_verb= es_get_verb(quantity, tense)
    es_prep_phrase= es_get_prepositional_phrase(quantity)

    es_sentence = es_determiner+' '+ es_noun+' '+ es_verb+' '+ es_prep_phrase
    return es_sentence
def main():

    param_list = [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3)]

    for quantity, tense in param_list:
        es_sentence = es_make_sentence(quantity, tense)
    print (es_sentence)

if __name__ == "__main__":
    main()
    
