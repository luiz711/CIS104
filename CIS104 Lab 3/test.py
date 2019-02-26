import unittest

import calculator



class Tests (unittest.TestCase):



    def tests_Add(self):

        self.assertEqual(calculator.add(38, 6), 44)

        self.assertEqual(calculator.add(10, 2), 12)

        self.assertEqual(calculator.add(100, 50), 150)



if __name__ == '__main__':

    unittest.main()
