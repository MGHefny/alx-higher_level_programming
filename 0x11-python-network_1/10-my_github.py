#!/usr/bin/python3
"""  gitHub API """
from sys import argv
from requests import get

if __name__ == "__main__":
    usr = argv[1]
    pass = argv[2]
    u = "https://api.github.com/user"
    response = get(u, auth=(usr, pass))
    x = response.x()
    print(x.get('id'))
