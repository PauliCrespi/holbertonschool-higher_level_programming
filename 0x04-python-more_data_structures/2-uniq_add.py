#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    lis = list(set(my_list))
    for i in range(len(lis)):
        summ = summ + lis[i]
    return summ
