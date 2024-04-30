#!/usr/bin/python3
""" sends request to URL and display body """
import sys
import urllib.request


if __name__ == '__main__':
    argv = sys.argv
    u = argv[1]
    try:
        with request.urlopen(u) as x:
            print(x.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
