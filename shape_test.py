import unittest
from triangle import Triangle
from circle import Circle
from rectangle import Rectangle
from square import Square


class ShapeTest(unittest.TestCase):

	def test_triangle(self):
		triangle = ShapeFactory.create_shape("Triangle", 3, 4, 5)
		self.assertEqual(triangle.area(), "15")
		self.assertEqual(triangle.perimeter(), "45")
		self.assertEqual(triangle.draw(), "Triangle, area: $area, perimeter: $perimeter")
	

	def test_circle(self):
		circle = ShapeFactory.create_shape("Circle", 5)
		self.assertEqual(circle.area(), 15.7)
		self.assertEqual(circle.perimeter(), 31.41)
		self.assertEqual(circle.draw(), "Circle, area: $area, perimeter: $perimeter")

	def test_square(self):
		square = ShapeFactory.create_shape("Square", 5)
		self.assertEqual(square.area(), "25")
		self.assertEqual(square.perimeter(), "20")
		self.assertEqual(square.draw(), "Square, area: $area, perimeter: $perimeter")

	def test_rectangle(self):
		rectangle = ShapeFactory.create_shape("Rectangle", 2, 4)
		self.assertEqual(rectangle.area(), "5")
		self.assertEqual(rectangle.perimeter(), "20")
		self.assertEqual(rectangle.draw(), "Rectangle, area: $area, perimeter: $perimeter")
