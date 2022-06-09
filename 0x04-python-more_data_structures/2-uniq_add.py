#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    nw_list = list(set(my_list))

    for ele in nw_list:
        sum += ele
    return sum
