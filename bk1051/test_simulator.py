import unittest
from Simulator import *

class SimulatorTestCase(unittest.TestCase):

	def test_returns(self):
		simulator = Simulator({.51: 1.0, .49: -1.0}, seed=1234)
		self.assertEqual(simulator.run(), 1.0)
		self.assertEqual(simulator.run(), 1.0)
		self.assertEqual(simulator.run(), 1.0)
		self.assertEqual(simulator.run(), 1.0)
		self.assertEqual(simulator.run(), 1.0)
		self.assertEqual(simulator.run(), 1.0)