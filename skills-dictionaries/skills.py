# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    # turn input string into a list so I can iterate by words
    input_list = input_string.split()
    distinct_words = {}

    # add each word to the dictionary with default value of zero.
    # if word is already in the dictionary, add 1
    for word in input_list:
        distinct_words[word] = distinct_words.get(word, 0) + 1

    return distinct_words


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    common_items = []

    # iterate through every item in first list
    for item in list1:
        # during each iteration of first list, also iterate through second list
        # this is terribly inefficient!
        for second_item in list2:
            if item == second_item:
                common_items.append(item)

    return common_items


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    # convert each list to set; will remove duplicates
    set1 = set(list1)
    set2 = set(list2)

    # use & operator to find common values between set1 and set2
    unique_set = set1 & set2

    return unique_set


def get_sum_zero_pairs(input_list):
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    all_zero_pairs = {}

    # there has to be a more efficient way to do this...
    for item in input_list:
        # iterating over list a second time
        for other_item in input_list:
            # if they're a zero pair, add to dictionary
            if item + other_item == 0:
                zero_pair = (item, other_item)
                zero_alt = (other_item, item)
                if zero_pair not in all_zero_pairs and zero_alt not in all_zero_pairs:
                    all_zero_pairs[zero_pair] = None

    zero_pairs = all_zero_pairs.keys()

    return zero_pairs


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    no_duplicates = {}

    # adding all words to a dictionary, since dictionaries cannot contain duplicate keys.
    for word in words:
        no_duplicates[word] = None

    return no_duplicates.keys()


def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    encode_dict = {
        'e': 'p',
        'a': 'd',
        't': 'o',
        'i': 'u'
    }

    new_phrase = ""

    # iterate through letters and replace with desired letter.
    for letter in phrase:
        if letter in encode_dict:
            letter = encode_dict[letter]
        new_phrase += letter

    return new_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    word_lengths = {}

    # iterate through list of words
    for word in words:
        # append word lengths to dictionary, set value to word & store in a list
        if len(word) not in word_lengths:
            word_lengths[len(word)] = [word]
        else:
            # if word length is already in dictionary, append value
            word_lengths[len(word)].append(word)

    return word_lengths.items()


def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_dict = {"    sir": "matey",
        "hotel" : "fleabag inn",
        "student" : "swabbie",
        "boy" : "matey",
        "madam" : "proud beauty",
        "professor" : "foul blaggart",
        "restaurant" : "galley",
        "your" : "yer",
        "excuse" : "arr",
        "students" : "swabbies",
        "are": "be",
        "lawyer" : "foul blaggart",
        "the": "th\'",
        "restroom" : "head",
        "my": "me",
        "hello" : "avast",
        "is": "be",
        "man": "matey"}

    # split string into list so I can iterate by words.
    phrase_list = phrase.split()

    pirate_words = []

    for word in phrase_list:
        # if the word is in pirate dictioary, replace word with its corresponding key.
        if word in pirate_dict:
            word = pirate_dict[word]
        # all all words to the new, 'translated', list.
        pirate_words.append(word)

    pirate_words = " ".join(pirate_words)

    return pirate_words

# # End of skills. See below for advanced problems.
# # To work on them, set ADVANCED=True at the top of this file.
# ############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

    # initialize empty dictionary.
    letter_freq = {}

    # for each letter in string, add to empty dictionary.
    for letter in input_string.lower():
        if letter == " " or letter in ".,!?#$":
            pass
        else:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

    # turn dictionary into tuples
    freq_first = []

    for letter, freq in letter_freq.items():
        freq_first.append((freq, letter))

    print sorted(freq_first)

    # at this point, I have a list of tuples sorted by letter frequency, but not sure what to do.

    return ''

# def adv_alpha_sort_by_word_length(words):
#     """
#     Given a list of words, return a list of tuples, ordered by word-length.
#     Each tuple should have two items--a number that is a word-length,
#     and the list of words of that word length. In addition to ordering
#     the list by word length, order each sub-list of words alphabetically.
#     Now try doing it with only one call to .sort() or sorted(). What does the
#     optional "key" argument for .sort() and sorted() do?
#
#     For example:
#
#         >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
#
#     """
#
#     return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
