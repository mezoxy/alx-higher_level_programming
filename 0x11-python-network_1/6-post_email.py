#!/usr/bin/python3
'''The module: 6-post_email'''


import requests
import sys

if __name__ == '__main__':

    inf = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=inf)
    print(res.text)

