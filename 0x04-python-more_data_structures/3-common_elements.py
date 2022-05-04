#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = set()
    set_1 = list(set_1)
    set_2 = list(set_2)
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            if set_1[i] == set_2[j]:
                new.add(set_1[i])
    return new
