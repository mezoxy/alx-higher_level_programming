#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    #try:
    j = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            print("{:d}".format(my_list[i]), end="")
            j += 1
            continue
    print()
    #except IndexError as e:
        #print("{}".format(e))
    #finally:
    return j
