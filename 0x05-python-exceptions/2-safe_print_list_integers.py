#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    p = 0
    for c in range(x):
        try:
            print("{:d}".format(my_list[c]), end="")
            p = p + 1
        except (TypeError, ValueError):
            x = x + 1
    print("")
    return p
