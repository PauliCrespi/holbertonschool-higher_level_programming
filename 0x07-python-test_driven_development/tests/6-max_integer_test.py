#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Testpk2(unittest.TestCase):
    """tests"""

    def test_0(self):
        """test 0"""
        t = []
        self.assertEqual(max_integer(t), None)

    def test_1(self):
        """test 1"""
        t = [1]
        self.assertEqual(max_integer(t), 1)

    def test_2(self):
        """test 2"""
        t = [12, 32, 233, 1]
        self.assertEqual(max_integer(t), 233)

    def test_3(self):
        """test 3"""
        t = [100, 1, 2, 100]
        self.assertEqual(max_integer(t), 100)

    def test_4(self):
        """test 4"""
        t = [-1, -2, 1, -2]
        self.assertEqual(max_integer(t), 1)

    def test_5(self):
        """test 5"""
        t = [-1, -2, -100]
        self.assertEqual(max_integer(t), -1)

    def test_6(self):
        """test 6"""
        self.assertRaises(TypeError, max_integer, [13, 'ba'])

    def test_7(self):
        """test 7"""
        self.assertRaises(TypeError, max_integer, [12, 12, 335, "string not accepted"])


if __name__ == '__main__':
    unittest.main()
