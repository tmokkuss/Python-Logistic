import unittest
from Task_2 import *


class MyTestCase(unittest.TestCase):
    def test_sort_data(self):
        self.assertEqual(sort_data('input.txt')[0], "KP2.2-01 - Vedomost'\n")


if __name__ == '__main__':
    unittest.main()
