#!/usr/bin/python3
'''The modue: 10-my_github'''


import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/users/' + sys.argv[1]
    res = requests.get(url, headers={'Authorization': 'token ' +sys.argv[2]})
    print(res.json().get('id'))
