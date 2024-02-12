#!/usr/bin/python3
"""base class"""
import json
import csv
import dumps, loads
import turtle


class Base:
    """Base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
