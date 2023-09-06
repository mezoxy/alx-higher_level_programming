#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 == 0:
        x = i
    else:
        x = i - 32
    print("{}".format(chr(x)), end="")
    i -= 1
