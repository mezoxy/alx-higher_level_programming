#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        if not my_list or x < 0:
            return 0
        for i in range(x):
            print(my_list[i], end="")
            y += 1
        print()
    except:
        print("")
    finally:
        return y
