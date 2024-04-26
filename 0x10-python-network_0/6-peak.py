#!/usr/bin/python3
"""peak"""


def find_peak(list_of_integers):
    """peak"""
    if not list_of_integers:
        return None

    r = len(list_of_integers) - 1
    l = 0

    while l < r:
        middle = (l + r) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            l = middle + 1
        else:
            r = middle

    return list_of_integers[l]
