#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        error = "Exception: Unknown format"
        message = f"code 'd' for object of type '{type(value).__name__}'"
        print("{} {}".format(error, message))
    finally:
        if isinstance(value, int):
            return True
        return False
