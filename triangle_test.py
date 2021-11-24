import unittest
from ShapeFactory import ShapeFactory


class TriangleTest(unittest.TestCase):

    def test_area(self):
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_perimeter(self):
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    def test_draw(self):
        triangle = ShapeFactory.create_triangle(3, 4, 5)
        self.assertEqual(triangle.__str__(), "Triangle, area:6.0, perimeter:12.0")


if __name__ == '__main__':
    unittest.main()
