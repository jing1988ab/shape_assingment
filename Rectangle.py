import math

from Shape import Shape


class Rectangle(Shape):
    """
    The Rectangle class implement the Shape as Rectangle.
    """
    def __init__(self, sideone, sidetwo):
        super().__init__("Rectangle")
        self.__sideone = sideone
        self.__sidetwo = sidetwo

    def area(self):
        """
        Calculate the area of the rectangle.
        :return: the area of the rectangle.
        """
        # return self.sideone*self.sidetwo*0.5
        return self.__sideone * self.__sidetwo

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        :return: the perimeter of the rectangle.
        """
        return 2 * (self.__sideone + self.__sidetwo)
        # return math.sqrt(self.sideone**2+self.sidetwo**2) + self.sideone + self.sidetwo
