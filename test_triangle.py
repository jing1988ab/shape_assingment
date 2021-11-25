import unittest
from ShapeFactory import ShapeFactory


class TriangleTest(unittest.TestCase):

    """
    it should calculate the area
    """
    def test_area(self):
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    """
    it should calculate the perimeter
    """
    def test_perimeter(self):
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    """
    it should override the less than operator based on area
    """
    def test_lt(self):
        triangle1 = ShapeFactory.create_triangle(3, 4, 5)
        triangle2 = ShapeFactory.create_triangle(3, 4, 6)
        self.assertTrue(triangle2 < triangle1)

    """
    it should override the less than operator based on area
    """
    def test_gt(self):
        triangle1 = ShapeFactory.create_triangle(3, 4, 5)
        triangle2 = ShapeFactory.create_triangle(3, 4, 6)
        self.assertTrue(triangle1 > triangle2)

    """
    it should override the equality operator based on area
    """
    def test_eq(self):
        triangle1 = ShapeFactory.create_triangle(3, 4, 5)
        triangle2 = ShapeFactory.create_triangle(3, 4, 6)
        triangle3 = ShapeFactory.create_triangle(3, 4, 6)
        self.assertFalse(triangle2 == triangle1)
        self.assertTrue(triangle2 == triangle3)


if __name__ == '__main__':
    unittest.main()
