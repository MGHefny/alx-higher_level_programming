#!/usr/bin/python3
""" sends a POST request to URL"""
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    argv = sys.argv
    u = argv[1]
    email = argv[2]
    DATA = urllib.parse.urlencode({"email": email})
    DATA = DATA.encode('ascii')

    with urllib.request.urlopen(u, DATA) as x:
        print(x.read().decode('utf-8'))
