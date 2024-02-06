#!/usr/bin/python3
"""inherite class check function"""


def is_kind_of_class(obj, a_class):
    """object instance inherited class"""
    if isinstance(obj, a_class):
        return True
    return False
