#!/usr/bin/python3
"""The module: 6-peak"""


def find_peak(list_of_integers):
    """
        find_peak: A function that finds the biggest num
                    in a list
    """
    if list_of_integers or len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
