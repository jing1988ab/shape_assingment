import unittest
from ShapeFactory import ShapeFactory


class CircleTest(unittest.TestCase):

    """
    it should calculate the area
    """
    def test_area(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(circle.area(), 78.53981633974483)

    """
    it should calculate the perimeter
    """
    def test_perimeter(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(circle.perimeter(), 31.41592653589793)

    """
    it should override the less than operator based on area
    """
    def test_lt(self):
        circle1 = ShapeFactory.create_circle(3)
        circle2 = ShapeFactory.create_circle(5)
        self.assertTrue(circle1 < circle2)

    """
    it should override the less than operator based on area
    """
    def test_gt(self):
        circle1 = ShapeFactory.create_circle(3)
        circle2 = ShapeFactory.create_circle(4)
        self.assertTrue(circle2 > circle1)

    """
    it should override the equality operator based on area
    """
    def test_eq(self):
        circle1 = ShapeFactory.create_circle(3)
        circle2 = ShapeFactory.create_circle(4)
        circle3 = ShapeFactory.create_circle(4)
        self.assertFalse(circle2 == circle1)
        self.assertTrue(circle2 == circle3)

    def test_get_name_of_circle(self):
        circle1 = ShapeFactory.create_circle(3)
        self.assertEqual(circle1.get_name_of_shape(), "Circle")


if __name__ == '__main__':
    unittest.main()
