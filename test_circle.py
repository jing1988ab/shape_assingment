import unittest
from ShapeFactory import ShapeFactory


class CircleTest(unittest.TestCase):

    def test_area(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(circle.area(), 78.53981633974483)

    def test_perimeter(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(circle.perimeter(), 31.41592653589793)

    def test_draw(self):
        circle = ShapeFactory.create_circle(5)
        self.assertEqual(circle.__str__(), "Circle, area:78.53981633974483, perimeter:31.41592653589793")

    def test_lt(self):
        circle1 = ShapeFactory.create_circle(3)
        circle2 = ShapeFactory.create_circle(5)
        self.assertTrue(circle1 < circle2)

    def test_gt(self):
        circle1 = ShapeFactory.create_circle(3)
        circle2 = ShapeFactory.create_circle(4)
        self.assertTrue(circle2 > circle1)

    def test_eq(self):
        circle1 = ShapeFactory.create_circle(3)
        circle2 = ShapeFactory.create_circle(4)
        circle3 = ShapeFactory.create_circle(4)
        self.assertFalse(circle2 == circle1)
        self.assertTrue(circle2 == circle3)


if __name__ == '__main__':
    unittest.main()
