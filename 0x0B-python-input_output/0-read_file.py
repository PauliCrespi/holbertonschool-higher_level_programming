#!/usr/bin/python3
"""task 0"""


def read_file(filename=""):
    """read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
