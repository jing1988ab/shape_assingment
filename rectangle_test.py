class RectangleTest():

    def test_area(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.area(), "15")

    def test_perimter(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.perimeter(), "45")

    def test_draw(self):
        triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
        self.assertEqual(triangle.draw(), "Triangle, area: $area, perimeter: $perimeter")