#!/usr/bin/python3
"""Defines attribute lookup function"""


def lookup(obj):
    """Return available attributes"""
    return (dir(obj))
