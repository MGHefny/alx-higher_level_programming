#!/usr/bin/python3
"""defines function"""
import json


def save_to_json_file(my_obj, filename):
    """object JSON representation"""
    with open(filename, "y") as x:
        json.dump(my_obj, x)
