#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as e:
        sys.stderr.write(e)
        return False
    finally:
        if isinstance(value, int):
            return True
        return False
