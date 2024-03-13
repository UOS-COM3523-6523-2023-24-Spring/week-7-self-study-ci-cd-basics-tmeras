import unittest
from main import simple_count, complex_function


class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(5, simple_count('hello'))

    # def test_complex_function(self):
    #     self.assertEqual('behaviour 1', complex_function())
