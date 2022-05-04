#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key in new.items():
        new[key[0]] = key[1] * 2
    return new
