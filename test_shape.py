import unittest
from Shape import Shape

class ShapeTest(unittest.TestCase):

	"""
	shape should initialize with a name
	"""
	def test_init_and_get_name(self):
		try:
			init_shape = Shape("Triangle")
		except RuntimeError as runtimeerror:
			print("shape failed to initialize")
		self.assertEqual(init_shape.get_name_of_shape(), "Triangle")


if __name__ == '__main__':
    unittest.main()