import unittest


class MyTest(unittest.TestCase):
    def test_m1(self):
        self.assertEqual(1, 2)

    def test_m2(self):
        self.assertEqual(100 % 2 == 0)
