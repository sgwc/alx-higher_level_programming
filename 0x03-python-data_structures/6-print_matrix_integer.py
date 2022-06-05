#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ls in matrix:
        i = 0
        for elem in ls:
            if i != 0:
                print(" ", end='')
            print("{:d}".format(elem), end="")
            i += 1
        print()
