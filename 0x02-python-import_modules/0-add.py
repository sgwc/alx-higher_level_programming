#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 5
    b = "H"
    print("{:d} + {:d} = {:d}".format(int(a), int(b), add(a, b)))
