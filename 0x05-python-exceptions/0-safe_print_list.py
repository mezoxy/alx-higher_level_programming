#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            y += 1
        print("")
    except IndexError:
        print("")
    return y
