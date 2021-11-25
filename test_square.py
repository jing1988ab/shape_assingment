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
        pass

    def test_gt(self):
        pass

    def test_eq(self):
        pass

if __name__ == '__main__':
    unittest.main()