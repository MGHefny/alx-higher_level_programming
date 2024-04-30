#!/usr/bin/python3
"""  send post req to 5000 """
from sys import argv
from requests import post

if __name__ == "__main__":
    u = 'http://0.0.0.0:5000/search_user'
    d = {'q': argv[1] if len(argv) >= 2 else ""}
    x = post(u, d)

    t_req = x.headers['content-type']

    if t_req == 'application/json':
        res = x.json()
        i_id = res.get('id')
        name = res.get('name')
        if (res != {} and i_id and name):
            print("[{}] {}".format(i_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
