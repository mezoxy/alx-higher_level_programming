#!/usr/bin/python3
import hidden_4
import sys
if __name__ == '__main__':
    x = dir(hidden_4)
    y = sorted(x)
    for i in y:
        if i[0] != "_" and i[1] != "_":
            print("{}".format(i))
