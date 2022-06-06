#!/usr/bin/python3
"""Unittest"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test base"""


    def test_user_activation(self):
        pass

    def test_user_points_update(self):
        pass

    def test_user_level_change(self):
        pass

    def test_0(self):
        """0"""
        a = Base()
        self.assertEqual(a.id, 1)

    def test_1(self):
        """1"""
        self.assertEqual(Base().id, 2)

    def test_2(self):
        """2"""
        self.assertEqual(Base(45).id, 45)

    def test_3(self):
        """3"""
        self.assertEqual(Base().id, 3)

    def test_4(self):
        """4"""
        self.assertEqual(Base(4738294732).id, 4738294732)

    def test_5(self):
        """5"""
        neg = Base(-132)
        self.assertEqual(neg.id, -132)


if __name__ == '__main__':
    unittest.main()
