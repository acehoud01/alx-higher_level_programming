#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    This class represents a rectangle with a width and height.

    Attributes:
        number_of_instances (int): The number of rectangle instances
        print_symbol (any): The sysmbol for string represantation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialise a Rectangle.

        Attributes:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """The height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """The area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with great area.

        Attributes:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle : Second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """Return a printable represatantion of the rectangle

        Character represation by #
        """
        if self.width == 0 or self.height == 0:
            return ("")
        else:
            return ("\n".join([str(self.print_symbol) *
                    self.__width] * self.__height))

    def __repr__(self):
        """Return string represatation of rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Print a messange upon delete of rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
