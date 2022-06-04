#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":

    for func in dir(hidden_4):
        if not ("__" in func):
            print(func)
