from ShapeFactory import ShapeFactory

class RectangleTest():

    """
    it should calculate the area
    """
    def test_area(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.area(), "15")

    """
    it should calculate the perimeter
    """
    def test_perimeter(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    """
    it should override the less than operator based on area
    """
    def test_lt(self):
        square1 = ShapeFactory.create_square(3, 4)
        square2 = ShapeFactory.create_square(3, 5)
        self.assertTrue(square1 < square2)

    """
    it should override the less than operator based on area
    """
    def test_gt(self):
        square1 = ShapeFactory.create_square(3, 4)
        square2 = ShapeFactory.create_square(4, 5)
        self.assertTrue(square2 > square1)

    """
    it should override the equality operator based on area
    """
    def test_eq(self):
        square1 = ShapeFactory.create_square(3, 4)
        square2 = ShapeFactory.create_square(4, 5)
        square3 = ShapeFactory.create_square(4, 5)
        self.assertFalse(square2 == square1)
        self.assertTrue(square2 == square3)

if __name__ == '__main__':
    unittest.main()