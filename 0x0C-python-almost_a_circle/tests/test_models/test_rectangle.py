#!/usr/bin/python3
"""Unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """test base"""


    def test_user_activation(self):
        pass

    def test_user_points_update(self):
        pass

    def test_user_level_change(self):
        pass

    def test_0(self):
        """0"""
        a = Rectangle(6, 7)
        self.assertEqual(a.width, 6)
        self.assertEqual(a.height, 7)

    def test_1(self):
        """1"""
        b = Rectangle(61111, 67967, 8)
        self.assertEqual(b.width, 61111)
        self.assertEqual(b.height, 67967)
        self.assertEqual(b.x, 8)

    def test_2(self):
        """2"""
        c = Rectangle(61111, 67967, 8, 90)
        self.assertEqual(c.width, 61111)
        self.assertEqual(c.height, 67967)
        self.assertEqual(c.x, 8)
        self.assertEqual(c.y, 90)

    def test_7(self):
        """7"""
        with self.assertRaises(ValueError):
            Rectangle(-6, 5)

    def test_8(self):
        """8"""
        with self.assertRaises(ValueError):
            Rectangle(16, -5)

    def test_9(self):
        """9"""
        with self.assertRaises(TypeError):
            Rectangle("16", 4)

    def test_10(self):
        """10"""
        with self.assertRaises(TypeError):
            Rectangle(8, '4')

    def test_11(self):
        """11"""
        with self.assertRaises(TypeError):
            Rectangle(8, "two")
