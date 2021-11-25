import unittest
from ShapeFactory import ShapeFactory

class SquareTest(unittest.TestCase):

    """
    it should calculate the area
    """
    def test_area(self):
        square = ShapeFactory.create_square( 5)
        self.assertEqual(square.area(), 25.0)

    """
    it should calculate the perimeter
    """
    def test_perimeter(self):
        square = ShapeFactory.create_square(5)
        self.assertEqual(square.perimeter(), 20.0)

    """
    it should override the less than operator based on area
    """
    def test_lt(self):
        square1 = ShapeFactory.create_square(3)
        square2 = ShapeFactory.create_square(5)
        self.assertTrue(square1 < square2)

    """
    it should override the less than operator based on area
    """
    def test_gt(self):
        square1 = ShapeFactory.create_square(3)
        square2 = ShapeFactory.create_square(4)
        self.assertTrue(square2 > square1)

    """
    it should override the equality operator based on area
    """
    def test_eq(self):
        square1 = ShapeFactory.create_square(3)
        square2 = ShapeFactory.create_square(4)
        square3 = ShapeFactory.create_square(4)
        self.assertFalse(square2 == square1)
        self.assertTrue(square2 == square3)

if __name__ == '__main__':
    unittest.main()