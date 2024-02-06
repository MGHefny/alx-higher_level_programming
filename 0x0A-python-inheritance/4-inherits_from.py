#!/usr/bin/python3
"""inherite class function"""


def inherits_from(obj, a_class):
    """object inherite instance class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
