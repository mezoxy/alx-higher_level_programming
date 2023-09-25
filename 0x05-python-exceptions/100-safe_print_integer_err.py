#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        #error = "Exception: Unknown format"
        #message = f"code 'd' for object of type '{type(value).__name__}'"
        print("{}".format(e))
    finally:
        if isinstance(value, int):
            return True
        return False
