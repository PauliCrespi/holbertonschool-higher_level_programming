#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    flag = 0
    for k in a_dictionary.items():
        if k[0] == key:
            a_dictionary[key] = value
            flag = 1
    if flag == 0:
        a_dictionary.update({key: value})
    return a_dictionary
