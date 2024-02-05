#!/usr/bin/python3
"""class checking"""


def is_same_class(obj, a_class):
    """object exactly instance given class"""
    if type(obj) == a_class:
        return True
    return False
