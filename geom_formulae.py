from numpy import*


def area_cylinder(radius, height):
    """
    calculates the area of a cylinder provided the radius and the
    height are given.both variables should have the same unit.
    @param radius:radius of the cylinder
    @param height:height of the cylinder
    @return:the area of a triangle(in units squared)

    >>> area_cylinder(7, 2)
    396
    """
    area = 2*pi*radius*(radius + height)
    return area


if __name__ == '__main__':
    print("Area of the cylinder is: ", area_cylinder(7, 2))


def rectangle_area(length, width):
    """
    calculates the area of a rectangle given length and width.
    @param length:length of the rectangle
    @param width:width of the rectangle
    @return:the area of a rectangle(in square units)

    >>> rectangle_area(2, 3)
    6
    """
    area = length*width
    return area


if __name__ == '__main__':
    print("area of rectangle is: ", rectangle_area(2, 3))


def pentagon_perimeter(side: 5):
    """
    calculates the perimeter of a regular pentagon given one of the sides.
    @param side:side of the pentagon
    @return:perimeter of a regular pentagon(same units as side)

    >>>pentagon_perimeter(3)
    15
    """
    perimeter = 5*side
    return perimeter

if __name__ == '__main__':
    print("perimeter of a regular pentagon:", pentagon_perimeter(3))


def circle_area(radius):
    """
    calculates area of a circle given the radius of that circle.
    @param radius:radius of the circle
    @return:area of the circle(in square units)

    >>>circle_area(7)
    154
    """
    area = pi*radius*radius
    return area

if __name__ == '__main__':
    print("area of the circle:", circle_area(7))


def hexagon_perimeter(side):
    """
    calculates the perimeter of a regular hexagon given one of the sides.
    @param side:side of a regular hexagon
    @return:perimeter of a regular hexagon(same unit as side)

    >>>hexagon_perimeter(6)
    36
    """
    perimeter = 6*side
    return perimeter

if __name__ == '__main__':
    print("perimeter of a regular hexagon:", hexagon_perimeter(6))


def triangle_area(base, height):
    """
    calculates the area of a triangle given the base and height of that triangle.
    @param base: base of the triangle
    @param height: height of the triangle
    @return:area of triangle(in square units)

    >>>triangle_area(4,8)
    16
    """
    area = base*height/2
    return area

if __name__ == '__main__':
    print("area of triangle:", triangle_area(4, 8))


def cuboid_volume(length, width, height):
    """
    calculates the volume of a cuboid provided its length,width and height are given.
    @param length:length of the cuboid
    @param width: width of the cuboid
    @param height: height of the cuboid
    @return:volume of the the cuboid(in cubic units)

    >>>cuboid_volume(4,5,10)
    200
    """
    volume = length*width*height
    return volume

if __name__ == '__main__':
    print("volume of the cuboid:", cuboid_volume(4, 5, 10))


def pyramid_volume(length, width, height):
    """
    calculates the volume of the pyramid provided the length,width and height of pyramid are given.
    @param length: length of the pyramid
    @param width: width of the pyramid
    @param height:height of the pyramid
    @return:volume of the pyramid(in cubic units)

    >>>pyramid_volume(10,20,30)
    2000
    """
    volume = length*width*height/3
    return volume

if __name__ == '__main__':
    print("volume of the pyramid:", pyramid_volume(10, 20, 30))


def cone_surface_area(radius, height):
    """
    calculates the surface area of a cone given the radius and height.
    @param radius:radius of the cone
    @param height:height of the cone
    @return:surface area of the cone(in square units)

    >>>cone_surface_area(7,4)
    22((7+(65)**0.5)
    """
    surface_area = pi*radius*(radius+((height**2)+(radius**2))**0.5)
    return surface_area

if __name__ == '__main__':
    print("surface area of the cone:", cone_surface_area(7, 4))


def sphere_volume(radius):
    """
    calculates the volume of a sphere given its radius.
    @param radius:radius of the sphere
    @return:volume of the sphere(in cubic units)

    >>>sphere_volume(1)
    4.19
    """
    volume = 4*pi*radius**3/3
    return volume


if __name__ == '__main__':
    print("volume of the sphere:", sphere_volume(1))


def triangle_area(a, b, c):
    """
    calculates the area of a triangle given the dimensions of its three sides.
    @param a:one of the sides of triangle
    @param b:second side of triangle
    @param c: third side of triangle
    @return:area of triangle(in square units)

    >>>triangle_area(4,3,3)
    (20)**0.5
    """

    if a+b > c & a+c > b & b+c > a:
        s = (a+b+c)/2.
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        return area
    else:
        return "Enter correct input"



print("area of triangle:",triangle_area(45,12,23))