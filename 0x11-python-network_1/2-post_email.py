#!/usr/bin/python3
"""Script that returns the result from the url"""


if __name__ == '__main__':
    import urllib.request as web
    import urllib.parse as webparse
    import sys

    url = sys.argv[1]
    values = {}
    values['email'] = sys.argv[2]
    data = webparse.urlencode(values).encode('utf-8')
    request = web.Request(url, data)
    with web.urlopen(request) as res:
        print(res.read.decode('utf-8'))
