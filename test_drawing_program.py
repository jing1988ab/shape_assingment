import unittest
from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
from Square import Square

class DrawingProgramTest(unittest.TestCase):

	"""
	the drawing program should initialize successfully
	"""
	def test_init(self):
		try:
			init = DrawingProgram()
		except ValueError as value_error:
			print("Drawing program failed to initialize")

	"""
	it should add a shape to the its collection
	"""
	def test_add_shape(self):
		add_shape_dp = DrawingProgram()
		circle = ShapeFactory.create_circle(5)
		try:
			add_shape_dp.add_shape(circle)
			print(add_shape_dp.collection_of_shapes[0])
		except RuntimeError as runtimeerror:
			print("failed to add shape")

		# self.assertRaises(TypeError, add_shape_dp.add_shape("a string that shouldn't be added"))

	"""
	it should remove a shape from its collection
	"""
	def test_remove_shape(self):
		remove_shape = DrawingProgram()
		circle = ShapeFactory.create_circle(5)
		try:
			remove_shape.add_shape(circle)
			remove_shape.remove_shape(circle)
		except RuntimeError as runtimeerror:
			print("failed to remove shape")

	"""
	it should print the shape
	"""
	def test_print_shape(self):
		print_shape = DrawingProgram()
		print_shape.add_shape(ShapeFactory.create_square(5))
		print_shape.add_shape(ShapeFactory.create_square(6))
		mySquare = ShapeFactory.create_square(7)
		print_shape.print_shape(mySquare)

	"""
	it should sort the shapes first by shape in alphabetical order
	and then by area if the shapes are the same
	"""
	def test_sort_shapes(self):
		sort_shapes_dp = DrawingProgram()
		ORDERED_LIST = [
			# ShapeFactory.create_circle(4),
			ShapeFactory.create_rectangle(3, 4),
			ShapeFactory.create_triangle(5, 5, 5),
			ShapeFactory.create_square(4),
			ShapeFactory.create_triangle(4, 4, 4),
		]
		for shape in reversed(ORDERED_LIST):
			sort_shapes_dp.add_shape(shape)
		sort_shapes_dp.sort_shapes()
		self.assertEqual(sort_shapes_dp.collection_of_shapes[0].__str__(), "Rectangle, area:12.0, perimeter:14.0")
		self.assertEqual(sort_shapes_dp.collection_of_shapes[1].__str__(), "Square, area:16.0, perimeter:16.0")
		self.assertEqual(sort_shapes_dp.collection_of_shapes[2].__str__(), "Triangle, area:6.928203230275509, perimeter:12.0")
		self.assertEqual(sort_shapes_dp.collection_of_shapes[3].__str__(), "Triangle, area:10.825317547305483, perimeter:15.0")

	"""
	it should get a specified shape from the list of shapes by index
	"""
	def test_get_shape(self):
		get_shape_dp = DrawingProgram()
		get_shape_dp.add_shape(ShapeFactory.create_rectangle(3, 4))
		got_shape = get_shape_dp.get_shape(0)
		self.assertEqual(got_shape.__str__(), "Rectangle, area:12.0, perimeter:14.0")

	"""
	it should put a shape at a specified index in the collection
	"""
	def test_set_shape(self):
		set_shape_dp = DrawingProgram()
		set_shape_dp.add_shape(ShapeFactory.create_rectangle(3, 4))
		set_shape_dp.add_shape(ShapeFactory.create_rectangle(5, 6))
		set_shape_dp.set_shape(1, ShapeFactory.create_rectangle(6, 7))
		self.assertEqual(set_shape_dp.collection_of_shapes[1].__str__(), "Rectangle, area:42.0, perimeter:26.0")

if __name__ == '__main__':
    unittest.main()