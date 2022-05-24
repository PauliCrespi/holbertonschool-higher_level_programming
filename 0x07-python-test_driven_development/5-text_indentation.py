#!/usr/bin/python3
"""task 5"""


def text_indentation(text):
    """text"""
    if text is None:
        raise TypeError("text must be a string")
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            print('\n')
            i += 1
            while (text[i] == ' ' and i < len(text)):
                i += 1
        else:
            print(text[i], end="")
            i += 1
