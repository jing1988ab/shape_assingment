class CircleTest(unittest.TestCase):

    def test_area(self):
        circle = ShapeFactory.create_shape("Circle", 5)
        self.assertEqual(circle.area(), 15.7)

    def test_perimeter(self):
        circle = ShapeFactory.create_shape("Circle", 5)
        self.assertEqual(circle.perimeter(), 31.41)

    def test_draw(self):
        circle = ShapeFactory.create_shape("Circle", 5)
        self.assertEqual(circle.draw(), "Circle, area: $area, perimeter: $perimeter")