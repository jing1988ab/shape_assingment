from wang_weinberg_shape_assignment.Shape import Shape


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def perimeter(self):
        return self.length*4
