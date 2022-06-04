#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    args = len(sys.argv) - 1
    sum_arg = 0

    if args <= 0:
        print(0)
    else:
        for i in range(args):
            sum_arg += int(sys.argv[i + 1])
        print("{:d}".format(sum_arg))
