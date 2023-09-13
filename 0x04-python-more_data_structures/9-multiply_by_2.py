#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {}
    for i in a_dictionary:
        d[i] = a_dictionary.get(i) * 2
    return d
