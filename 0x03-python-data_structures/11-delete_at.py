#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list == []:
        return my_list
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    if len(my_list) == 1:
        return []
    else:
        my_list.remove(my_list[idx])
        return my_list
