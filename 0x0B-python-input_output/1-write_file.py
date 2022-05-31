#!/usr/bin/python3
"""task 1"""


def write_file(filename="", text=""):
    """write in file"""
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
    return(write_data)
