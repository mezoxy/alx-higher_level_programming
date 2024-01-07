#!/usr/bin/python3
'''The module: 2-post_email'''


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    data = urllib.parse.urlencode(val)
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as resp:
        print(resp.read().decode('utf-8'))
