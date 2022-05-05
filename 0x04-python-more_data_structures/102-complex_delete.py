#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = a_dictionary.copy()
    for key in new.items():
        if key[1] == value:
            a_dictionary.pop(key[0], None)
    return(a_dictionary)
