#!/usr/bin/python3
'''The module: 2-post_email'''


import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':

    try:
        with urllib.request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
