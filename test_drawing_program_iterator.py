import unittest
from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory
from DrawingProgramlterator import DrawingProgramIterator


class DrawingProgramIteratorTest(unittest.TestCase):

	"""
	test should initialize the iterator with an index of 0 and return an instance of the iterator
	"""
	def test_init(self):
		try:
			iterator = DrawingProgramIterator(None)
			self.assertEqual(iterator.index, 0)
		except RuntimeError as runtimeerror:
			print("failed to initialize iterator")

	"""
	test should call the __next__ method but not increment if no
	shapes are present
	"""
	def test_next_no_objects(self):
		no_object_dp = DrawingProgram()
		j = 0
		for i in no_object_dp:
			j += 1
		self.assertEqual(j, 0)

	"""
	test should call the __next__ method and increment by one
	if one shape is present
	"""
	def test_next_one_object(self):
		one_object_dp = DrawingProgram()
		one_object_dp.add_shape(ShapeFactory.create_square(4))
		j = 0
		for i in one_object_dp:
			j += 1
		self.assertEqual(j, 1)

	"""
	test should call the __next__ method and increment as many times
	as there are objects
	"""
	def test_next_many_objects(self):
		multi_object_dp = DrawingProgram()
		multi_object_dp.add_shape(ShapeFactory.create_circle(4))
		multi_object_dp.add_shape(ShapeFactory.create_square(4))
		multi_object_dp.add_shape(ShapeFactory.create_rectangle(4, 3))
		multi_object_dp.add_shape(ShapeFactory.create_triangle(3, 4, 4))
		j = 0
		for i in multi_object_dp:
			j += 1
		self.assertEqual(j, 4)

if __name__ == '__main__':
    unittest.main()