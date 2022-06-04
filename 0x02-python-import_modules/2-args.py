#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    num_of_arg = len(sys.argv) - 1
    if num_of_arg >= 1:
        print("{:d} arguments:".format(num_of_arg))
        for i in range(num_of_arg):
            print("{:d}: {}".format(i + 1, sys.argv[i + 1]))

    else:
        print("{} arguments.".format(0))
