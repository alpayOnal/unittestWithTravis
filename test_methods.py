import unittest
import methods

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(methods.add(3,5), 8)

    def test_minus(self):
        self.assertEqual(methods.minus(3,5), 2)

    def test_multiply(self):
        self.assertEqual(methods.multiply(3,5), 15)


