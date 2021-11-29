import math

from Shape import Shape


class Circle(Shape):
    """
    The Circle class implement the Shape as circle.
    """
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        :return: the area of the circle.
        """
        return math.pi * self.__radius**2

    def perimeter(self):
        """
        Calculate the perimeter of the circle.
        :return: the perimeter of the circle.
        """
        return 2 * math.pi * self.__radius
