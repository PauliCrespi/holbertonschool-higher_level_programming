#!/usr/bin/python3
"""task 100"""


def append_after(filename="", search_string="", new_string=""):
    """write in file"""
    txt = ""
    with open(filename, 'r') as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, 'w') as f:
        f.write(txt)
