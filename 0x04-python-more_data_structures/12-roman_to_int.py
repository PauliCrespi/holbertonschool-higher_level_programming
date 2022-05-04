#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    n = [d[i] for i in roman_string.upper() if i in d]
    r = sum([i if i >= n[min(j + 1, len(n) - 1)]
            else -i for j, i in enumerate(n)])
    return r
