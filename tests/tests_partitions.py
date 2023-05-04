import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.all import *
from polynomos.lists.list_callables_0 import PlainListNew

class TestPartitions(unittest.TestCase):
    def make_plainlist(self, list_of_lists):
        return PlainListNew(
            *[PlainListNew(*x) for x in list_of_lists]
        )
    
    def test_partitions(self):
        self.assertEqual(IntegerPartitions(0), self.make_plainlist([[]]))
        self.assertEqual(IntegerPartitions(1), self.make_plainlist([[1]]))
        self.assertEqual(IntegerPartitions(-1), self.make_plainlist([[]]))
        self.assertEqual(IntegerPartitions(2), self.make_plainlist([[2], [1, 1]]))
        self.assertEqual(IntegerPartitions(5), self.make_plainlist([
            [5], 
            [4, 1],
            [3, 2],
            [3, 1, 1],
            [2, 2, 1],
            [2, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]))

if __name__ == '__main__':
    unittest.main()