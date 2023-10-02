#!/usr/bin/python3
"""3-say_my_name"""


def say_my_name(first_name, last_name=""):
    """say_my_name  a function that prints My name is <first name> <last name>.
    Args: 
        first_name (str): A string
        last_name (str): A string
    """

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
