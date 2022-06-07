#!/usr/bin/python3
"""Unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquare(unittest.TestCase):
    """test square"""


    def test_user_activation(self):
        pass

    def test_user_points_update(self):
        pass

    def test_user_level_change(self):
        pass

    def test_0(self):
        """0"""
        a = Square(6)
        self.assertEqual(a.width, 6)
        self.assertEqual(a.height, 6)

    def test_1(self):
        """1"""
        b = Square(7978906, 8)
        self.assertEqual(b.width, 7978906)
        self.assertEqual(b.height, 7978906)
        self.assertEqual(b.x, 8)

    def test_2(self):
        """2"""
        c = Square(16, 28, 5)
        self.assertEqual(c.width, 16)
        self.assertEqual(c.height, 16)
        self.assertEqual(c.x, 28)
        self.assertEqual(c.y, 5)

    def test_3(self):
        """3"""
        d = Square(16, 28, 5, 21)
        self.assertEqual(d.width, 16)
        self.assertEqual(d.height, 16)
        self.assertEqual(d.x, 28)
        self.assertEqual(d.y, 5)
        self.assertEqual(d.id, 21)

    def test_4(self):
        """4"""
        with self.assertRaises(ValueError):
            Square(-6)

    def test_5(self):
        """5"""
        with self.assertRaises(TypeError):
            Square("6")

    def test_6(self):
        """6"""
        with self.assertRaises(TypeError):
            Square("two")

    def test_7(self):
        """7"""
        with self.assertRaises(TypeError):
            Square('4')
