#!/usr/bin/python3
"""
add_integer: A function that calulates somme of to integers or floats
Args: two numbers a and b
returns: a + b
"""


def add_integer(a, b=98):
    """add_integer.
    Args:
        a (int, float):
        b (int, float):
    """

    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    """Checking if b is float or an integer"""

    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")
    """Return the somme of number after casting"""

    return int(a) + int(b)
