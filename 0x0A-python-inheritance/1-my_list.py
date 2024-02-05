#!/usr/bin/python3
"""inherite list class myList"""


class MyList(list):
    """implements sorted printing list class"""
    def print_sorted(self):
        print(sorted(self))
