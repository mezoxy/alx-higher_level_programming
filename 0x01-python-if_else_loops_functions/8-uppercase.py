#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < 123 and ord(str[i]) > 96:
            print("{}".format(chr(ord(str[i])) - 32), end="" if i < len(str) - 1 else "\n")
        else: 
            print("{}".format(str[i]), end="" if i < len(str) - 1 else "\n")
