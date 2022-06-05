#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_elem = len(my_list)

    if not(idx < 0 or idx > (list_elem - 1)):
            my_list[idx] = element
    return(my_list)
