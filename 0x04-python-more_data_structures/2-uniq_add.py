#!/usr/bin/python3
def uniq_add(my_list=[]):
    sume = 0
    for i in set(my_list):
        sume += i
    return sume
