#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [-2, -1, 1, 2, 3, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
