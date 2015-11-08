import unittest
from Investor import *
import numpy as np

class InvestorTestCase(unittest.TestCase):

	def test_run_simulation(self):
		'''Investor: Running a simulation returns well formed daily returns'''
		inv = Investor([1, 10], 10, 1000)
		test_array = inv._run_simulation(10)
		success = np.array([-1.0, -1.0, -1.2, -1.4, -0.6, -0.8, -1.0, -0.8, -1.4, -0.6])
		print test_array.tolist()
		self.assertTrue(np.array_equiv(test_array, success))

	def test_returns_means(self):
		inv = Investor([1, 10], 10000, 1000)
		test = inv.get_results()
		print test
		self.assertEqual(test, 0)

		