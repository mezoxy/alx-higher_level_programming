#!/usr/bin/python3
'''The module: 4-hbtn_status'''


import requests

if __name__ == '__main__':

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print("\t- type:", type(res.text))
    print("\t- content:", res.text)
