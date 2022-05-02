#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        l = len(my_list) - 1
        for i in range(l, -1, -1):
            print(f"{my_list[i]}")
