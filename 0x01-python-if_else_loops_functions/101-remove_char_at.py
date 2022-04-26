#!/usr/bin/python3
def remove_char_at(str, n):
    string = ''
    x = 0
    if n < 0:
        n = len(str) - (n + 1)
    for i in str:
        if x != n:
            string += i
        x += 1
    return(string)
