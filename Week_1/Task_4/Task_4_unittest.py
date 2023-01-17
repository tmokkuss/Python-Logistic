import unittest
from Task_4 import *


class MyTestCase(unittest.TestCase):
    def test_find_count_symbols(self):
        self.assertDictEqual(find_count_symbols('input.txt'),  {'I': 3,
                                                                'a': 8,
                                                                'c': 4,
                                                                'd': 8,
                                                                'e': 17,
                                                                'f': 2,
                                                                'g': 1,
                                                                'h': 7,
                                                                'i': 9,
                                                                'l': 1,
                                                                'm': 5,
                                                                'n': 9,
                                                                'o': 9,
                                                                'r': 5,
                                                                's': 6,
                                                                't': 8,
                                                                'u': 4,
                                                                'v': 2,
                                                                'w': 4,
                                                                'y': 2})

    def test_sorted_top(self):
        self.assertListEqual(sorted_top('input.txt'),   [('e', 17),
                                                         ('i', 9),
                                                         ('n', 9),
                                                         ('o', 9),
                                                         ('a', 8),
                                                         ('t', 8),
                                                         ('d', 8),
                                                         ('h', 7),
                                                         ('s', 6),
                                                         ('r', 5),
                                                         ('m', 5),
                                                         ('c', 4),
                                                         ('u', 4),
                                                         ('w', 4),
                                                         ('I', 3),
                                                         ('y', 2),
                                                         ('f', 2),
                                                         ('v', 2),
                                                         ('g', 1),
                                                         ('l', 1)])

    def test_add_enters(self):
        self.assertEqual(add_enters('input.txt'), ['e, ', '17\n',
                                                   'i, ', '9\n',
                                                   'n, ', '9\n',
                                                   'o, ', '9\n',
                                                   'a, ', '8\n',
                                                   't, ', '8\n',
                                                   'd, ', '8\n',
                                                   'h, ', '7\n',
                                                   's, ', '6\n',
                                                   'r, ', '5\n'])


if __name__ == '__main__':
    unittest.main()
