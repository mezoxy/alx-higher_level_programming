#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for i in a_dictionary:
        a_dictionary[i] = a_dictionary.get(i) * 2
    return a_dictionary
