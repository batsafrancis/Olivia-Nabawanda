from numbers  import Number
from numpy import*

def area_cylinder(radius,height):
    """
calculates the area of a cylinder provided the radius and the height are given.both variables should have the same unit.
    :param radius:radius of the cylinder
    :param height:height of the cylinder
    :return:the area of a triangle(in units squared)
    >>> area_cylinder(7,2)
    396
    """
    return 2*pi*radius*(radius+height)
print(area_cylinder(7,2))

def rectangle_area(length,width):
    """
calculates the area of a rectangle given length and width.
    :param length:length of the rectangle
    :param width:width of the rectangle
    :return:the area of a rectangle(in square units)
    >>> rectangle_area(2,3)
    6
    """
    return length*width
print(rectangle_area(2,3))

def pentagon_perimeter(side:5):
    """
calculates the perimeter of a regular pentagon provided one side is known.




def circle_area(side):
    return math.pi*side**2
print(circle_area(7))


def perimeter_regularhexagon(side:6):
    return 6*side
print(perimeter_regularhexagon(10))

def area_triangle(b,h):
    return 1/2*b*h
print(area_triangle(2,4))


import math
def area_semicircle(r):
    return 1/2 *math.pi*r*r
print(area_semicircle(2))