#!/usr/bin/python3
"""task 3"""


def say_my_name(first_name, last_name=""):
    """My name is <first name> <last name>"""
    if first_name is None or first_name == "":
        raise TypeError("first_name must be a string")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
