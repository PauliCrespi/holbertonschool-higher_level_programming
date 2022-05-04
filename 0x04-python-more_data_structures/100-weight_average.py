#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    weight = 0
    for i in my_list:
        num = num + i[1]
        weight = weight + (i[0] * i[1])
    return (weight / num)
