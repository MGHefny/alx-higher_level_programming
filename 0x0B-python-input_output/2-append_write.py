#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """Append string end UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as x:
        return x.write(text)
