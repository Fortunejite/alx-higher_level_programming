#!/usr/bin/python3
"""Script that returns the result from the url"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
