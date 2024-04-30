#!/usr/bin/python3
"""  send post req """
from sys import argv
from requests import post

if __name__ == "__main__":
    u = argv[1]
    email = argv[2]
    req = post(u, {'email': email})
    print(req.text)
