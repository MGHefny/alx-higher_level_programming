#!/usr/bin/python3
"""  send post req """
from sys import argv
from requests import get

if __name__ == "__main__":
    u = argv[1]
    x = get(u)
    ERR_TXT = 'Error code: {}'
    status = x.status_code
    print(ERR_TXT.format(status) if (status >= 400) else x.text)
