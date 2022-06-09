#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    return [y for x in s1 for y in s2 if x == y]
