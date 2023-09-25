#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        i = "Inside result: "
        c = a / b
    except ZeroDivisionError:
        c = None
    finally:
        print("{}{}".format(i, c))
        return c
