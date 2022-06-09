#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = []
    s1 = list(set_1)
    s2 = list(set_2)
    com_el = [y for x in s1 for y in s2 if x == y]
    for el in s1:
        if el not in com_el:
            od_set.append(el)
    for e2 in s2:
        if e2 not in com_el:
            od_set.append(e2)
    
    return od_set
