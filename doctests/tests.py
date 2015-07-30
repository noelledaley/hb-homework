import unittest
from helpers import all_even, unique

class UnitTestCase(unittest.TestCase):

    def test_all_even(self):
        assert(all_even([0, 1, 2, 3, 4]) == [0, 2, 4])

    def test_unique(self):
        assert(unique([4, 4, 4, -3, 0, 1]) == [4, -3, 0, 1])

if __name__ == "__main__":
    unittest.main()
