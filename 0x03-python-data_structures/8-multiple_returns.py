#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if length > 0:
        first_c = sentence[0]
    else:
        first_c = None
    return (length, first_c)
