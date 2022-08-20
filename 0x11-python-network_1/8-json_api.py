#!/usr/bin/python3
"""task 8"""
from sys import argv
from requests


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
