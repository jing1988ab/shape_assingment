import unittest
from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory

class DrawingProgramTest(unittest.TestCase):

	def test_init(self):
		try:
			init = DrawingProgram()
		except ValueError as value_error:
			print("Drawing program failed to initialize")

	def test_add_shape(self):
		add_shape_dp = DrawingProgram()
		circle = ShapeFactory.create_circle(5)
		try:
			add_shape_dp.add_shape(circle)
			print(add_shape_dp.collection_of_shapes[0])
		except RuntimeError as runtimeerror:
			print("failed to add shape")

		# self.assertRaises(TypeError, add_shape_dp.add_shape("a string that shouldn't be added"))

	def test_remove_shape(self):
		remove_shape = DrawingProgram()
		circle = ShapeFactory.create_circle(5)
		try:
			remove_shape.add_shape(circle)
			remove_shape.remove_shape(circle)
		except RuntimeError as runtimeerror:
			print("failed to remove shape")

	def test_print_shape(self):
		print_shape = DrawingProgram()
		square = ShapeFactory.create_square(5)
		print_shape.add_shape(square)

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

		# self.assertEqual(ORDERED_LIST[0].__str__, "Circle, area:50.265482457436692, perimeter:25.132741228718346")
		# print(ShapeFactory.create_rectangle(3, 4).__str__())
		# print(ORDERED_LIST[0].__str__())
		self.assertEqual(sort_shapes_dp.collection_of_shapes[0].__str__(), "Rectangle, area:12.0, perimeter:14.0")
		self.assertEqual(sort_shapes_dp.collection_of_shapes[1].__str__(), "Square, area:16.0, perimeter:16.0")
		self.assertEqual(sort_shapes_dp.collection_of_shapes[2].__str__(), "Triangle, area:6.928203230275509, perimeter:12.0")
		self.assertEqual(sort_shapes_dp.collection_of_shapes[3].__str__(), "Triangle, area:10.825317547305483, perimeter:15.0")


	def test_get_shape(self):
		get_shape_dp = DrawingProgram()
		get_shape_dp.add_shape(ShapeFactory.create_rectangle(3, 4))
		got_shape = get_shape_dp.get_shape(0)
		self.assertEqual(got_shape.__str__(), "Rectangle, area:12.0, perimeter:14.0")


	def test_set_shape(self):
		set_shape_dp = DrawingProgram()
		set_shape_dp.add_shape(ShapeFactory.create_rectangle(3, 4))
		set_shape_dp.add_shape(ShapeFactory.create_rectangle(5, 6))
		set_shape_dp.set_shape(1, ShapeFactory.create_rectangle(6, 7))
		the_shape_i_set = set_shape_dp.get_shape(1)
		self.assertEqual(the_shape_i_set.__str__(), "Rectangle, area:42.0, perimeter:26.0")

if __name__ == '__main__':
    unittest.main()