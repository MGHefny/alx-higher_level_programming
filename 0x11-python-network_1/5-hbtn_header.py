#!/usr/bin/python3
""" fetch X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    req = get(argv[1])
    print(req.headers.get('X-Request-Id'))
