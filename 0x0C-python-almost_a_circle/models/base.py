#!/usr/bin/python3
"""base class"""
import json
import csv
import turtle


class Base:
    """Base model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """rightly and longer"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """dictionary"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """object file"""
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as z:
            z.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """instance dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """file unjsonifies"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as z:
            return [cls.create(**q) for q in cls.from_json_string(z.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as z:
            writer = csv.writer(z)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        s = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as z:
            re = csv.re(z)
            for ro in re:
                ro = [int(r) for r in ro]
                if cls is Rectangle:
                    q = {"id": ro[0], "width": ro[1], "height": ro[2],
                         "x": ro[3], "y": ro[4]}
                else:
                    q = {"id": ro[0], "size": ro[1],
                         "x": ro[2], "y": ro[3]}
                s.append(cls.create(**q))
        return s

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for ix in list_rectangles + list_squares:
            xt = turtle.Turtle()
            xt.color((randrange(255), randrange(255), randrange(255)))
            xt.pensize(1)
            xt.penup()
            xt.pendown()
            xt.setpos((ix.x + xt.pos()[0], ix.y - xt.pos()[1]))
            xt.pensize(10)
            xt.forward(ix.width)
            xt.left(90)
            xt.forward(ix.height)
            xt.left(90)
            xt.forward(ix.width)
            xt.left(90)
            xt.forward(ix.height)
            xt.left(90)
            xt.end_fill()

        time.sleep(5)
