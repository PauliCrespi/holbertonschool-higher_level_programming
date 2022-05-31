#!/usr/bin/python3
"""101"""


def add_attribute(mc, name, value):
    """add"""
    if hasattr(mc, '__dict__'):
        setattr(mc, name, value)
    else:
        raise TypeError("can't add new attribute")
