#!/usr/bin/env python3

import math


class Shape:
    """
    A shape has the following attributes:

    area: a float representing the area of the shape in units
    perimeter: a float representing the perimeter of the shape in units
    units: a string representing the units of measurement e.g. 'mm' or in'
    """

    def __init__(self, name, area=None, perimeter=None, units=None):
        self.name = name
        self.area = area
        self.perimeter = perimeter
        self.units = units

    def __repr__(self):
        return "name:{}\narea:{}\nperimeter:{}\nunits:{}".format(
            self.name, self.area, self.perimeter, self.units
        )


class Circle(Shape):

    def __init__(self, name, radius=1, units=None):
        self.name = name
        self.radius = radius
        self.area = math.pi * radius * radius
        self.perimeter = 2 * math.pi * radius
        self.units = units


if "__main__" == __name__:
    shape = Shape("my shape")
    print(shape)
    print("")
    circle = Circle("my circle")
    print(circle)
