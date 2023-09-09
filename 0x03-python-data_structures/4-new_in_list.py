#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx in range(len(my_list)):
        copy_list = my_list[:idx] + [element] + my_list[idx + 1:]
        return copy_list
    return my_list
