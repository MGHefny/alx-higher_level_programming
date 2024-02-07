#!/usr/bin/python3
"""define function"""
import json


def load_from_json_file(filename):
    """object JSON file"""
    with open(filename) as x:
        return json.load(x)
