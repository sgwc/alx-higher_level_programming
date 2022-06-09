#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) > 0:
        sum = my_list[0]
        my_list.sort()
        prev = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] == prev:
                pass
            else:
                sum += my_list[i]
                prev = my_list[i]
            return sum
    else:
        return 0
