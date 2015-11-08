import unittest
from Simulator import *

class SimulatorTestCase(unittest.TestCase):

	def test_returns_correct_result(self):
		'''Test that running a simulator returns the correct result'''
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 1, seed=1234)

		self.assertEqual(simulator.run(), np.array([1.0]))
		self.assertEqual(simulator.run(), np.array([-1.0]))
		self.assertEqual(simulator.run(), np.array([1.0]))
		self.assertEqual(simulator.run(), np.array([-1.0]))
		self.assertEqual(simulator.run(), np.array([-1.0]))
		self.assertEqual(simulator.run(), np.array([1.0]))


		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 5, seed=1234)
		self.assertTrue(np.array_equal(simulator.run(), np.array([1, -1, 1, -1, -1])))

		# Make sure a single outcome returns a single result
		simulator = Simulator({(0, 1): 21}, 5, seed=1234)
		self.assertTrue(np.array_equal(simulator.run(), np.array([21, 21, 21, 21, 21])))

