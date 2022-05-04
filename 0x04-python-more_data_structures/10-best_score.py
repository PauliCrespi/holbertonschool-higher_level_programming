#!/usr/bin/python3
def best_score(a_dictionary):
    keymax = ""
    if a_dictionary:
        keymax = max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
        return keymax
    else:
        return None
