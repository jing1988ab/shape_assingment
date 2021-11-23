import math

from wang_weinberg_shape_assignment.Shape import Shape


class Rectangle(Shape):
    """
    The Rectangle class implement the Shape as Rectangle.
    """
    def __init__(self, sideone, sidetwo):
        super().__init__("Rectangle")
        self.sideone = sideone
        self.sidetwo = sidetwo

    def area(self):
        """
        Calculate the area of the rectangle.
        :return: the area of the rectangle.
        """
        return self.sideone*self.sidetwo*0.5

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        :return: the perimeter of the rectangle.
        """
        return math.sqrt(self.sideone**2+self.sidetwo**2) + self.sideone + self.sidetwo
