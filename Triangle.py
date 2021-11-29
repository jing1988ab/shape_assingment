import math

from Shape import Shape


class Triangle(Shape):
    """
    The Triangle class implement the Shape as Triangle.
    """
    def __init__(self,sideone, sidetwo, sidethree):
        super().__init__("Triangle")
        self.__sideone = sideone
        self.__sidetwo = sidetwo
        self.__sidethree = sidethree

    def area(self):
        """
        Calculate the area of the triangle.
        :return: the area of the triangle.
        """
        p = self.perimeter()*0.5
        x = p*(p-self.__sideone)*(p-self.__sidetwo)*(p-self.__sidethree)
        if x <= 0:
            print("not a triangle!")
        area = math.sqrt(x)
        return area

    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        :return: the perimeter of the triangle.
        """
        return self.__sideone + self.__sidetwo + self.__sidethree
