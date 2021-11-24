from Shape import Shape


class Square(Shape):
    """
    The Square class implement the Shape as Square.
    """
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        """
        Calculate the area of the square.
        :return: the area of the square.
        """
        return self.length**2

    def perimeter(self):
        """
        Calculate the perimeter of the square.
        :return: the perimeter of the square.
        """
        return self.length*4
