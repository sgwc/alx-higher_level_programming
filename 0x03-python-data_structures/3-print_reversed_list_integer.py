#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        list_elem = len(my_list)
        my_list.reverse()
        for i in range(list_elem):
            print("{:d}".format(my_list[i]))
