#!/usr/bin/python3
"""Script that returns the result from the url"""


if __name__ == '__main__':
    import urllib.request as web

    with web.urlopen('https://alx-intranet.hbtn.io/status') as res:
        result = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
        print("\t- utf8 content: {}".format(result.decode('utf-8')))
