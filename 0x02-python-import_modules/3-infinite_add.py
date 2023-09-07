#!/usr/bin/python3
import sys
if __name__ == '__main__':
    sum = 0
    i = len(sys.argv) - 1
    while i > 0:
        sum += int(sys.argv[i])
        i -= 1
    print("{}".format(sum))
