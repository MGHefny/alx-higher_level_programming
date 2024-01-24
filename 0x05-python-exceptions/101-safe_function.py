#!/usr/bin/python3
from __future__ import print_function
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
    except Exception as y:
        print("Exception: {}".format(y), file=sys.stderr)
        return None
    else:
        return x
