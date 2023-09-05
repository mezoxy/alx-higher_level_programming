#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):

        if ord(str[i]) in range(97, 123):
            x = chr(ord(str[i]) - 32)
            print("{}".format(x), end="" if i < len(str) - 1 else "\n")
        else:
            print("{}".format(str[i]), end="" if i < len(str) - 1 else "\n")
