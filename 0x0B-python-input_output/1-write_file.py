#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """string UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as x:
        return x.write(text)
