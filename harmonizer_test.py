import unittest
from harmonizer import getInput

class NameTestCase(unittest.TestCase):
    def test_1_1(self):
        test = input(getInput('a'))
        self.assertEqual(test, ['a'])
    def test_1_2(self):
        test = input(getInput('bbb', 'd##', 'fbb'))
        self.assertEqual(test, ['bbb', 'd##', 'fbb'])
    def test_1_3(self):
        test = input(getInput('c', 'e', 'g'))
        self.assertEqual(test, ['c', 'e', 'g'])

if __name__ == '__main__':
    unittest.main()