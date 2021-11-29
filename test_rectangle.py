import unittest
from ShapeFactory import ShapeFactory

class RectangleTest(unittest.TestCase):

    """
    it should calculate the area
    """
    def test_area(self):
        rectangle1 = ShapeFactory.create_rectangle(3, 4)
        self.assertEqual(rectangle1.area(), 12)

    """
    it should calculate the perimeter
    """
    def test_perimeter(self):
        rectangle2 = ShapeFactory.create_rectangle(3, 4)
        self.assertEqual(rectangle2.perimeter(), 14)

    """
    it should override the less than operator based on area
    """
    def test_lt(self):
        rectangle3 = ShapeFactory.create_rectangle(3, 4)
        rectangle4 = ShapeFactory.create_rectangle(3, 5)
        self.assertTrue(rectangle3 < rectangle4)

    """
    it should override the less than operator based on area
    """
    def test_gt(self):
        rectangle5 = ShapeFactory.create_rectangle(3, 4)
        rectangle6 = ShapeFactory.create_rectangle(4, 5)
        self.assertTrue(rectangle6 > rectangle5)

    """
    it should override the equality operator based on area
    """
    def test_eq(self):
        rectangle7 = ShapeFactory.create_rectangle(3, 4)
        rectangle8 = ShapeFactory.create_rectangle(4, 5)
        rectangle9 = ShapeFactory.create_rectangle(4, 5)
        self.assertFalse(rectangle7 == rectangle8)
        self.assertTrue(rectangle8 == rectangle9)

    def test_get_name(self):
        rectangle10 = ShapeFactory.create_rectangle(5, 6)
        self.assertEqual(rectangle10.get_name_of_shape(), "Rectangle")


if __name__ == '__main__':
    unittest.main()