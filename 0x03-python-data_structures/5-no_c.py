#!/usr/bin/python3
def no_c(my_string):

    leng = len(my_string)

    new_string = ""
    for i in range(leng):
        if not(my_string[i] == 'c' or my_string[i] == 'C'):
            new_string += my_string[i]
    return(new_string)
