import unittest
from Simulator import *

class SimulatorTestCase(unittest.TestCase):

	def test_returns_correct_result(self):
		'''Simulator: running a one-dimensional simulator returns the correct result'''
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 1, 1, seed=1234)

		self.assertEqual(simulator.run(), np.array([[1.0]]))
		self.assertEqual(simulator.run(), np.array([[-1.0]]))
		self.assertEqual(simulator.run(), np.array([[1.0]]))
		self.assertEqual(simulator.run(), np.array([[-1.0]]))
		self.assertEqual(simulator.run(), np.array([[-1.0]]))
		self.assertEqual(simulator.run(), np.array([[1.0]]))


		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 1, 5, seed=1234)
		self.assertTrue(np.array_equal(simulator.run(), np.array([[1, -1, 1, -1, -1]])))

		# Make sure a single outcome returns a single result
		simulator = Simulator({(0, 1): 21}, 1, 5, seed=1234)
		self.assertTrue(np.array_equal(simulator.run(), np.array([[21, 21, 21, 21, 21]])))

	def test_multiple_dimensions(self):
		'''Simulator: Running a multidimensional simulator returns the correct result.'''
		simulator = Simulator({(0, .3): 1.0, (.3, .7): 0, (.7, 1): -1.0}, 3, 3, seed=1234)
		self.assertTrue(np.array_equal(simulator.run(), np.array(
			[[1, 0, 0],
			[-1, -1, 1],
			[1, -1, -1]]
			)))

	def test_invalid_returns(self):
		'''Simulator: Initializing with invalid ranges raises exception'''
		with self.assertRaises(InvalidReturnsException):
			simulator = Simulator({(0, .3): 1.0, (.4, .7): 0, (.7, 1): -1.0}, 1, 1, seed=1234)

		with self.assertRaises(InvalidReturnsException):
			simulator = Simulator({(0, .3): 1.0, (.3, .7): 0}, 1, 1, seed=1234)

