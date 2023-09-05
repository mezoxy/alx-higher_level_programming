#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            x = chr(ord(str[i]) - 32)
        else:
            x = str[i]
        print("{}".format(x), end="")
    print("")
