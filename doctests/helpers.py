# Please add some doctests to the following file! Otherwise, how will we ever
# test the results of these super complicated, higher level functions???!!!
# Try to create a few doctests for each that take in interesting data.

from doctest import testmod


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

    >>> all_even([0, 1, 2, 3, 4])
    [0, 2, 4]

    >>> all_even([-7, 0, -2, 1, 2])
    [0, -2, 2]

    """

    return [d for d in number_list if d % 2 == 0]


def unique(numbers):
    """Given a list of numbers, return a list with duplicates removed.

    >>> unique([0, 1, 2, 3, 4])
    [0, 1, 2, 3, 4]

    >>> unique([4, 1, 2, 2, 3, 4])
    [4, 1, 2, 3]

    >>> unique([4, 4, 4, -3, 0, 1])
    [4, -3, 0, 1]

    """

    uniques = []
    for n in numbers:
        if n not in uniques:
            uniques.append(n)
    return uniques


if __name__ == "__main__":
    result = testmod()
    if not result.failed:
        print "*** %s TESTS PASSED!" % result.attempted
