from ShapeFactory import ShapeFactory

class SquareTest():

    def test_area(self):
        square = ShapeFactory.create_shape("Square", 5)
        self.assertEqual(square.area(), "25")

    def test_perimeter(self):
        square = ShapeFactory.create_shape("Square", 5)
        self.assertEqual(square.perimeter(), "20")

    def test_draw(self):
        square = ShapeFactory.create_shape("Square", 5)
        self.assertEqual(square.draw(), "Square, area: $area, perimeter: $perimeter")

    def test_lt(self):
        square1 = ShapeFactory.create_square(3)
        square2 = ShapeFactory.create_square(5)
        self.assertTrue(square1 < square2)

    def test_gt(self):
        square1 = ShapeFactory.create_square(3)
        square2 = ShapeFactory.create_square(4)
        self.assertTrue(square2 > square1)

    def test_eq(self):
        square1 = ShapeFactory.create_square(3)
        square2 = ShapeFactory.create_square(4)
        square3 = ShapeFactory.create_square(4)
        self.assertFalse(square2 == square1)
        self.assertTrue(square2 == square3)

if __name__ == '__main__':
    unittest.main()