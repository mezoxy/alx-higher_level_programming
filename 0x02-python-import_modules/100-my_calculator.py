#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == '__main__':
    op = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div
            }
    if len(sys.argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        sys.exit(1)
    if sys.argv[2] in op:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
    else:
        strr = "Unknown operator. Available operators: +, -, * and /"
        print("{}".format(strr))
        sys.exit(1)
