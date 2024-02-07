#!/usr/bin/python3
"""function"""


def read_file(filename=""):
    """contents UTF8 text file stdout"""
    with open(filename, encoding="utf-8") as x:
        print(x.read(), end="")
