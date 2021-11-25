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
        pass

    def test_gt(self):
        pass

    def test_eq(self):
        pass


if __name__ == '__main__':
    unittest.main()
