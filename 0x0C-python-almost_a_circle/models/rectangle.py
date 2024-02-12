#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            z = 0
            for arg in args:
                if z == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif z == 1:
                    self.width = arg
                elif z == 2:
                    self.height = arg
                elif z == 3:
                    self.x = arg
                elif z == 4:
                    self.y = arg
                z += 1

        elif kwargs and len(kwargs) != 0:
            for g, f in kwargs.items():
                if g == "id":
                    if f is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = f
                elif g == "width":
                    self.width = f
                elif g == "height":
                    self.height = f
                elif g == "x":
                    self.x = f
                elif g == "y":
                    self.y = f

    def to_dictionary(self):
        return {
            "id": self.id,"width": self.width,
            "height": self.height,"x": self.x,
            "y": self.y}

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
			self.x, self.y,self.width, self.height)
