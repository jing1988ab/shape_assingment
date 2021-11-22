from wang_weinberg_shape_assignment.Shape import Shape


class Triangle(Shape):
    def __init__(self,sideone, sidetwo, sidethree):
        super().__init__("Triangle")
        self.sideone = sideone
        self.sidetwo = sidetwo
        self.sidethree = sidethree

    def area(self):
        p = self.perimeter()
        x = p*(p-self.sideone)*(p-self.sidetwo)*(p-self.sidethree)
        while x <= 0:
            print("not a triangle!")
        area = x**2
        return area

    def perimeter(self):
        return self.sideone + self.sidetwo + self.sidethree
