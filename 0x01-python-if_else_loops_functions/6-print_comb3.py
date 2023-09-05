#!/usr/bin/python3
for i in range(9):
    for j in range(i, 9):
        if i == 8 and j == 8:
            print("{}{}".format(i, j + 1))
        else:
            print("{}{}".format(i, j + 1), end=", ")
