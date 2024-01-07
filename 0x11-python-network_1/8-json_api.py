#!/usr/bin/python3
'''The module: 8-json_api'''


import requests
import sys

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        res = requests.post(url, date={'q': sys.argv[1]})
    else:
        res = requests.post(url, data={'q': ""})
    try:
        if len(res.json()) != 0:
            print("[{}] {}".format(
                res.json().get('id'), res.json().get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
