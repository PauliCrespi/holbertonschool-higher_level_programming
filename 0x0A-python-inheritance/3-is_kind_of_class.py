#!/usr/bin/python3
"""task 3"""


def is_kind_of_class(obj, a_class):
    return (isinstance(obj, a_class) or issubclass(type(obj), a_class))
