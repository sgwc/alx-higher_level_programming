#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)

    if leng != 0:
        maxim = my_list[0]
        for i in range(1, leng):
            if (maxim < my_list[i]):
                maxim = my_list[i]
        return(maxim)
    else:
        return(None)
