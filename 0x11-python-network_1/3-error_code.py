#!/usr/bin/python3
""" sends request to URL and display body """
import sys
from urllib import request, error


if __name__ == '__main__':
    argv = sys.argv
    u = argv[1]
    try:
        with request.urlopen(u) as x:
            print(x.read().decode('utf-8'))
    except error.HTTPError as errorr:
        print("Error code: {}".format(errorr.status))
