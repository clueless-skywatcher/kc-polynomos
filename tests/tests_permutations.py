import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.all import *
from polynomos.combinomos.all import *

class TestPermutations(unittest.TestCase):
    def test_perms(self):
        self.assertEqual(
            Permutations(PlainListNew(1, 2, 3)), 
            PlainListNew(
                PlainListNew(1, 2, 3),
                PlainListNew(1, 3, 2),
                PlainListNew(2, 1, 3),
                PlainListNew(2, 3, 1),
                PlainListNew(3, 1, 2),
                PlainListNew(3, 2, 1)
            ))
        self.assertEqual(Permutations(PlainListNew()), PlainListNew(PlainListNew()))
        self.assertEqual(Permutations(PlainListNew(1)), PlainListNew(PlainListNew(1)))
        self.assertEqual(Permutations('abc'), PlainListNew(
            'abc',
            'acb',
            'bac',
            'bca',
            'cab',
            'cba'
        ))
        self.assertEqual(Permutations(PlainListNew(1, 2, 3)), Permutations(PlainListNew(1, 3, 2)))
        self.assertNotEqual(Permutations(PlainListNew(1, 2, 3)), Permutations(PlainListNew(1, 2, 4)))
        self.assertEqual(ListLength(Permutations(PlainListNew(1, 2, 3))), 6)
        self.assertEqual(ListLength(Permutations(PlainListNew(1))), 1)

class TestCombinations(unittest.TestCase):
    def test_combs(self):
        self.assertEqual(
            Combinations(PlainListNew(1, 2, 3, 4), 2), 
            PlainListNew(
                PlainListNew(1, 2),
                PlainListNew(1, 3),
                PlainListNew(1, 4),
                PlainListNew(2, 3),
                PlainListNew(2, 4),
                PlainListNew(3, 4)
            ))
        self.assertEqual(
            Combinations(PlainListNew(1, 3, 2, 4), 2), 
            PlainListNew(
                PlainListNew(1, 3),
                PlainListNew(1, 2),
                PlainListNew(1, 4),
                PlainListNew(3, 2),
                PlainListNew(3, 4),
                PlainListNew(2, 4)
            ))
        self.assertEqual(Combinations(PlainListNew(), 1), PlainListNew())
        self.assertEqual(Combinations(PlainListNew(1), 1), PlainListNew(PlainListNew(1)))
        self.assertEqual(Combinations('abcd', 2), PlainListNew(
            'ab',
            'ac',
            'ad',
            'bc',
            'bd',
            'cd'
        ))
        self.assertNotEqual(Combinations(PlainListNew(1, 2, 3), 2), Combinations(PlainListNew(1, 3, 2), 2))
        self.assertNotEqual(Combinations(PlainListNew(1, 2, 3), 2), Combinations(PlainListNew(1, 2, 4), 2))
        self.assertEqual(ListLength(Combinations(PlainListNew(1, 2, 3, 4), 2)), 6)
        self.assertEqual(ListLength(Combinations(PlainListNew(1), 1)), 1)

if __name__ == '__main__':
    unittest.main()