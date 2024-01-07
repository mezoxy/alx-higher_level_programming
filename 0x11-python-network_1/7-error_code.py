#!/usr/bin/python3
'''The module: 7-error_code'''


import requests
import sys

if __name__ == '__main__':

    res = requests.get(sys.argv[1])

    if res.status_code == 200:
        print(res.text)
    else:
        print("Error code:", res.status_code)
