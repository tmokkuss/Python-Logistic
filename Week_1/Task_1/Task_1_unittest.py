import unittest

from Task_1 import *


class Task1Test(unittest.TestCase):
    def test_get_grade_and_name(self):
        self.assertEqual(get_grade_and_name("1week/Task_1_folder/data.txt")[0], 'Котов Алексей,4\n')

    def test_alphabetical_sorting(self):
        self.assertEqual(alphabetical_sorting("1week/Task_1_folder/data.txt")[0], f'Бакушкин Даниил,3\n')


if __name__ == '__main__':
    unittest.main()
