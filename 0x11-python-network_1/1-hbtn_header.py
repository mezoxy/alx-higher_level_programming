#!/usr/bin/python3
'''The module: 1-hbtn_header'''


import urllib.request as req
import sys

with req.urlopen(sys.argv[1]) as resp:
    print(resp.headers['X-Request-Id'])
