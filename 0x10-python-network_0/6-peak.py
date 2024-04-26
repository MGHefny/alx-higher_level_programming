#!/usr/bin/python3
"""peak"""


def find_peak(list_of_integers):
    """peak"""
    if not list_of_integers:
        return None

    rgh = len(list_of_integers) - 1
    lif = 0

    while lif < rgh:
        middle = (lif + rgh) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            lif = middle + 1
        else:
            rgh = middle

    return list_of_integers[lif]
