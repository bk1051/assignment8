import unittest
from Investor import *
import numpy as np

class InvestorTestCase(unittest.TestCase):

	def test_run_simulation(self):
		'''Investor: Running a simulation returns well formed daily returns'''
		inv = Investor([1, 10], 10, 1000)
		test_array = inv._run_simulation(10)
		success = np.array([0, 0, -.2, -.4, .4, .2, 0, .2, -.4, .4])
		print test_array.tolist()
		self.assertTrue(np.allclose(test_array, success))

	def test_returns_correct_results(self):
		'''Investor: Returned results are correct values for mean/std'''
		inv = Investor([1, 10], 10000, 1000)
		test = inv.get_results()
		success = np.array([[ 1., 0.0332, 0.99944873],
 							[10., 0.02084, 0.31293081]])
		self.assertTrue(np.allclose(test, success))

		