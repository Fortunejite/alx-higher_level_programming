#!/usr/bin/python3
"""Script that returns the result from the url"""


if __name__ == '__main__':
    import  requests

    result = requests.get('https://alx-intranet.hbtn.io/status')
    result = result.text
    print("Body response:")
    print("\t- type: {}".format(type(result)))
    print("\t- content: {}".format(result))
