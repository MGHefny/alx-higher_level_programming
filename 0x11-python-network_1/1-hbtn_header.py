#!/usr/bin/python3
""" the X-Request-Id vresponse """
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as x:
        print(x.headers["X-Request-Id"])
