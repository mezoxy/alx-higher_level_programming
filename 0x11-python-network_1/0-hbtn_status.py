#!/usr/bin/python3
'''the module: 0-hbtn_status'''


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    if response.headers.get_content_charset() == 'utf-8':
        print("\t- utf8 content: OK")
    else:
        print("\t- utf8 content: NO")
