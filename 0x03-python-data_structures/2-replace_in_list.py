#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx in range(len(my_list)):
        my_list[idx:idx + 1] = [element]
        return my_list
    return my_list