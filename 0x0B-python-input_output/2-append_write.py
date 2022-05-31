#!/usr/bin/python3
"""task 2"""


def append_write(filename="", text=""):
    """append in file"""
    with open(filename, 'a', encoding="utf-8") as f:
        write_data = f.write(text)
    return(len(text))
