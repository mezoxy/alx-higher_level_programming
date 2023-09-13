#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lis = []
    for i in my_list:
        if i == search:
            i = replace
        lis.append(i)
    return lis
