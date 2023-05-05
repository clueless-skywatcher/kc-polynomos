import unittest

import sys

sys.path.insert(0, "../../kc-polynomos")
sys.path.insert(0, "../kc-polynomos")

from polynomos.all import *
from polynomos.combinomos.all import *

class TestFerrersDiagrams(unittest.TestCase):
    def test_ferrers(self):
        self.assertRaises(ValueError, lambda: FerrersDiagram(PlainListNew(1.2, 5, 2)))
        self.assertRaises(ValueError, lambda: FerrersDiagram(PlainListNew(-1, 5, 0)))
        self.assertRaises(ValueError, lambda: FerrersDiagram(PlainListNew(4, 1, 2, 3)))
        self.assertRaises(ValueError, lambda: FerrersDiagram(PlainListNew(4, 1, 2, 3), notation = 'french'))
        self.assertRaises(ValueError, lambda: FerrersDiagram(PlainListNew(4, 3, 3, 1), character = 'ab'))
        
        self.assertEqual(FerrersDiagram(PlainListNew(4, 3, 3, 1)), '\n'.join([
            '* * * *',
            '* * *',
            '* * *',
            '*'
        ]))
        self.assertEqual(FerrersDiagram(PlainListNew(1, 3, 3, 4), notation = 'french'), '\n'.join([
            '*',
            '* * *',
            '* * *',
            '* * * *'
        ]))
        self.assertEqual(FerrersDiagram(PlainListNew(4, 3, 3, 1), character = '#'), '\n'.join([
            '# # # #',
            '# # #',
            '# # #',
            '#'
        ]))
        self.assertEqual(FerrersDiagram(PlainListNew(1, 3, 3, 4), notation = 'french', character = '#'), '\n'.join([
            '#',
            '# # #',
            '# # #',
            '# # # #'
        ]))

if __name__ == '__main__':
    unittest.main()