from ShapeFactory import ShapeFactory

class RectangleTest():

    def test_area(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.area(), "15")

    def test_perimter(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.perimeter(), 12)

    def test_draw(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.draw(), "Triangle, area: $area, perimeter: $perimeter")

    def test_lt(self):
        square1 = ShapeFactory.create_square(3, 4)
        square2 = ShapeFactory.create_square(3, 5)
        self.assertTrue(square1 < square2)

    def test_gt(self):
        square1 = ShapeFactory.create_square(3, 4)
        square2 = ShapeFactory.create_square(4, 5)
        self.assertTrue(square2 > square1)

    def test_eq(self):
        square1 = ShapeFactory.create_square(3, 4)
        square2 = ShapeFactory.create_square(4, 5)
        square3 = ShapeFactory.create_square(4, 5)
        self.assertFalse(square2 == square1)
        self.assertTrue(square2 == square3)

if __name__ == '__main__':
    unittest.main()