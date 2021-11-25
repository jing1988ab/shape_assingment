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

        def test_lt(self):
            triangle1 = ShapeFactory.create_triangle(3, 4, 5)
            triangle2 = ShapeFactory.create_triangle(3, 4, 6)
            self.assertTrue(triangle2 < triangle1)

        def test_gt(self):
            triangle1 = ShapeFactory.create_triangle(3, 4, 5)
            triangle2 = ShapeFactory.create_triangle(3, 4, 6)
            self.assertTrue(triangle1 > triangle2)

        def test_eq(self):
            triangle1 = ShapeFactory.create_triangle(3, 4, 5)
            triangle2 = ShapeFactory.create_triangle(3, 4, 6)
            triangle3 = ShapeFactory.create_triangle(3, 4, 6)
            self.assertFalse(triangle2 == triangle1)
            self.assertTrue(triangle2 == triangle3)


if __name__ == '__main__':
    unittest.main()
