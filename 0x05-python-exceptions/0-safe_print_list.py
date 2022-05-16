#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for c in range(x):
            print(f"{my_list[c]}", end="")
        print("")
    except ValueError:
        print("")
        return c
    return(x)
