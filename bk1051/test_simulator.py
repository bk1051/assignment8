import unittest
from Simulator import *

class SimulatorTestCase(unittest.TestCase):

	def test_returns(self):
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 1, seed=1234)

		self.assertEqual(simulator.run(), np.array([1.0]))
		self.assertEqual(simulator.run(), np.array([-1.0]))
		self.assertEqual(simulator.run(), np.array([1.0]))
		self.assertEqual(simulator.run(), np.array([-1.0]))
		self.assertEqual(simulator.run(), np.array([-1.0]))
		self.assertEqual(simulator.run(), np.array([1.0]))


		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 5, seed=1234)
		self.assertTrue(np.array_equal(simulator.run(), np.array([1, -1, 1, -1, -1])))