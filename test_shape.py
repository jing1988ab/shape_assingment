import unittest
from Shape import Shape

class ShapeTest(unittest.TestCase):

	# def test_triangle(self):
	# 	triangle = ShapeFactory.create_triangle(3, 4, 5)
	# 	print(triangle.area())
	# 	self.assertEqual(triangle.area(), "15")
	# 	self.assertEqual(triangle.perimeter(), "45")
	# 	self.assertEqual(triangle.draw(), "Triangle, area: $area, perimeter: $perimeter")
	#
	#
	# def test_circle(self):
	# 	circle = ShapeFactory.create_circle(5)
	# 	print(circle.area())
	# 	self.assertEqual(circle.area(), 15.7)
	# 	self.assertEqual(circle.perimeter(), 31.41)
	# 	self.assertEqual(circle.draw(), "Circle, area: $area, perimeter: $perimeter")
	#
	# def test_square(self):
	# 	square = ShapeFactory.create_square(5)
	# 	self.assertEqual(square.area(), "25")
	# 	self.assertEqual(square.perimeter(), "20")
	# 	self.assertEqual(square.draw(), "Square, area: $area, perimeter: $perimeter")
	#
	# def test_rectangle(self):
	# 	rectangle = ShapeFactory.create_shape("Rectangle", 2, 4)
	# 	self.assertEqual(rectangle.area(), "5")
	# 	self.assertEqual(rectangle.perimeter(), "20")
	# 	self.assertEqual(rectangle.draw(), "Rectangle, area: $area, perimeter: $perimeter")

	def test_init_and_get_name(self):
		try:
			init_shape = Shape("Triangle")
		except RuntimeError as runtimeerror:
			print("shape failed to initialize")
		self.assertEqual(init_shape.get_name_of_shape(), "Triangle")

	def test_lt(self):
		pass

	def test_gt(self):
		pass

	def test_eq(self):
		pass


if __name__ == '__main__':
    unittest.main()