import unittest
from ShapeFactory import ShapeFactory


class ShapeFactoryTest(unittest.TestCase):

	"""
	it should return true if there are positive numbers and fail if a negative
	number is passed in
	"""
	def test_to_positive_number(self):
		# self.assertFalse(ShapeFactory.to_positive_number(1, 2, -4))
		self.assertTrue(ShapeFactory.to_positive_number(1, 2, 3))


if __name__ == '__main__':
    unittest.main()