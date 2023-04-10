#!/usr/bin/python3
"""Script that returns the result from the url"""


if __name__ == '__main__':
    import urllib.request as web
    import sys

    url = sys.argv[1]
    request = web.Request(url)
    with web.urlopen(request) as res:
        result = dict(res.headers).get('X-Request-Id')
        print(result)
