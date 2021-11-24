from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle


class ShapeFactory:
    """
    The ShapeFactory class creates shape objects that can be add to the
    DrawingProgram. The methods in ShapeFactory validate data
    being passed to the classes.
    """

    # @staticmethod
    # def create_shape(shape_name, shape_data):
    #     """
    #     This is a static
    #     :param shape_name:
    #     :param shape_data:
    #     :return:
    #     """
    #     pass

    @staticmethod
    def create_circle(radius):
        """
        This is a static method that creates a circle based on radius
        length passed as an argument. It verifies that this value can
        converted to a float before creating a concrete Circle object.
        """
        radius, = ShapeFactory.to_positive_number(float, radius)
        return Circle(radius)

    @staticmethod
    def create_square(length):
        """
        This is a static method that creates a square based on side
        length passed as an argument. It verifies that this value can
        converted to a float before creating a concrete Square object.
        """
        length, = ShapeFactory.to_positive_number(float, length)
        return Square(length)

    @staticmethod
    def create_rectangle(sideone, sidetwo):
        """
        This is a static method that creates a rectangle based on two side
        length passed as arguments. It verifies that these values can
        converted to floats before creating a concrete Rectangle object.
        """
        sideone, sidetwo, = ShapeFactory.to_positive_number(float, sideone, sidetwo)
        return Rectangle(sideone, sidetwo)

    @staticmethod
    def create_triangle(sideone, sidetwo, sidethree):
        """
        This is a static method that creates a triangle based on three side
        length passed as arguments. It verifies that these values can
        converted to floats before creating a concrete triangle object.
        """
        sideone, sidetwo, sidethree, = ShapeFactory.to_positive_number(float, sideone, sidetwo, sidethree)
        return Triangle(sideone, sidetwo, sidethree)

    @staticmethod
    def to_positive_number(type, *args):
        """
        This is a static method that  checks if a passed value can be
        represented as an input number type greater than zero, and
        returns it as that number type if ture.
        Raises an exception as returns of error message if false.
        """
        for number in args:
            if type(number) > 0:
                yield type(number)
            else:
                raise ValueError("not a good number")