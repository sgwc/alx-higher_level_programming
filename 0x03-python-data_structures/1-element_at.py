#!/usr/bin/python3
def element_at(my_list, idx):
    list_elem = len(my_list)
    if not(idx < 0 or idx > list_elem):
        return (my_list[idx])
