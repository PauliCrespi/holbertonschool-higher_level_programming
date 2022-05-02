#!/usr/bin/python3
def no_c(my_string):
    stri = ""
    for i in range(len(my_string)):
        if my_string[i] != "c" and my_string[i] != "C":
            stri += my_string[i]
    return stri
