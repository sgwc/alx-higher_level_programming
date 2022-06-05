#!/usr/bin/python3
def print_list_integer(my_list=[]):
    elem_list = len(my_list)
    for i in range(elem_list):
        print("{:d}".format(my_list[i]))
