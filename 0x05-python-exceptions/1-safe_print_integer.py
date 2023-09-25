#!/usr/bin/python3
def safe_print_integer(value):
    try:
        e = "is not an integer"
        print("{:d}".format(value))
    except:
        print("{} {}".format(valua, e))
    finally:
        if isinstance(value, int):
            return True
        return False
