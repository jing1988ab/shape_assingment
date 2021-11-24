import unittest
from ShapeFactory import ShapeFactory


class CircleTest(unittest.TestCase):

    def test_area(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(round(circle.area(), 2), 78.54)

    def test_perimeter(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(round(circle.perimeter(), 2), 31.42)

    def test_draw(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(circle.__str__(), "Circle, area:78.53981633974483, perimeter:31.41592653589793")


if __name__ == '__main__':
    unittest.main()
