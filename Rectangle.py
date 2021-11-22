import math

from wang_weinberg_shape_assignment.Shape import Shape


class Rectangle(Shape):
    def __init__(self, sideone, sidetwo):
        super().__init__("Rectangle")
        self.sideone = sideone
        self.sidetwo = sidetwo

    def area(self):
        return self.sideone*self.sidetwo*0.5

    def perimeter(self):
        return math.sqrt(self.sideone**2+self.sidetwo**2)
