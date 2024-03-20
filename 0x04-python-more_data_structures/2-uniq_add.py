#!/usr/bin/python3
def uniq_add(my_list=[]):
    init_list = set(my_list)
    total = 0

    for i in init_list:
        total += i

    return (total)
