import unittest

class DrawingProgramTest(unittest.TestCase):

	def test_init(self):
		try:
			myDrawingProgram = DrawingProgram()
		except ValueError as value_error:
			print("Drawing program failed to initialize")

	def test_add_shape(self):
		myDrawingProgram = DrawingProgram()
		circle = ShapeFactory.create_shape("Circle", 5)
		try:
			myDrawingProgram.add_shape(circle)
			new_shape = myDrawingProgram.shapes[0]
		except RuntimeError as runtimeerror:
			print("failed to add shape")

	def test_remove_shape(self):
		myDrawingProgram = DrawingProgram()
		circle = ShapeFactory.create_shape("Circle", 5)
		try:
			myDrawingProgram.add_shape(circle)
			myDrawingProgram.remove_shape(circle)
		except RuntimeError as runtimeerror:
			print("failed to remove shape")

	def test_print_shape(self):
		myDrawingProgram = DrawingProgram()
		circle = ShapeFactory.create_shape("Circle", 5)
		myDrawingProgram.add_shape()

	def test_sort_shapes(self):
		pass

	def test_get_shape(self):
		pass

	def test_set_shape(self):
		pass