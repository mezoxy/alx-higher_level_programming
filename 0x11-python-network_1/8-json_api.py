#!/usr/bin/python3
'''The module: 8-json_api'''


import requests
import sys

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        res = requests.post(url, data={'q': sys.argv[1]})
    else:
        res = requests.post(url, data={'q': ""})
    try:
        if not res.json():
            print("No result")
        else:
            print("[{}] {}".format(
                res.json().get('id'), res.json().get('name')))
    except Exception as e:
        print("Not a valid JSON")
