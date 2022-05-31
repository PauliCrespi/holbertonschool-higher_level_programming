#!/usr/bin/python3
"""task 100"""


class MyInt(int):
    """rebel"""

    def __eq__(self, other):
        """false"""
        return False

    def __ne__(self, other):
        """true"""
        return True
