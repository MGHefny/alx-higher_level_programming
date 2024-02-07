#!/usr/bin/python3
"""define function"""
import json


def from_json_string(my_str):
    """representation JSON string"""
    return json.loads(my_str)
