import abc


class Shape(metaclass=abc.ABCMeta):
    """
    The Shape class is an abstract base class. It get the name of the shape, and
    calculate its area and perimeter.
    """

    def __init__(self, name_of_shape):
        self.name_of_shape = name_of_shape

    def get_name_of_shape(self):
        """
        Get the name of the shape.
        :return: the name of the shape.
        """
        return self.name_of_shape

    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass

    def __str__(self):
        """
        Return a string representation of the shape.
        :return: the string representation of the shape including the name, the area and the perimeter.
        """
        return str(self.name_of_shape)+", area:"+str(self.area())+", perimeter:"+str(self.perimeter())

    def draw(self):
        """
        Prints the name of the shape followed by the area and perimeter of the shape
        formatted as follows: "name_of_shape, area: value_of_area, perimeter: value_of_perimeter"
        (e.g."Circle, area: 3.141592653589793, perimeter: 6.283185307179586")
        """
        print(self.__str__())

    def __gt__(self, other):
        """
        Defines the behaviour of the greater-than operator > between shapes.
        :param other:Shapes
        :return:Boolean
        """
        if isinstance(other, Shape):
            if other.get_name_of_shape() == self.get_name_of_shape():
                if self.area() > other.area():
                    return True
                return False
            elif self.get_name_of_shape() > other.get_name_of_shape():
                return True
            return False
        raise Exception("Other is not a shape")

    def __eq__(self, other):
        """
        Defines the behaviour of the equal operator = between shapes.
        :param other:Shapes
        :return:Boolean
        """
        if isinstance(other, Shape):
            return other.get_name_of_shape() == self.get_name_of_shape() and self.area()==other.area()
        raise Exception("Other is not a shape")

    def __lt__(self, other):
        """
        Defines the behaviour of the less-than operator < between shapes.
        :param other:Shapes
        :return:Boolean
        """
        return (not self.__gt__(other)) and (not self.__eq__(other))