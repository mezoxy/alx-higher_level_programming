#!/usr/bin/python3
import hidden_4
import sys
if __name__ == '__main__':
    print(sorted(i for i in dir(hidden_4) if i[0] != "_" and i[1] != "_"))
