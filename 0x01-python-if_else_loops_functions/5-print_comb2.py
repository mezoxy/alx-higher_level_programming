#!/usr/bin/python3
for i in range(100):
    if i // 10 == 9 and i % 10 == 9:
        print("{}{}".format(i // 10, i % 10))
    else:
        print("{}{}".format(i // 10, i % 10), end=", ")
