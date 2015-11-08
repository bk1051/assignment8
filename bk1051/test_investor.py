import unittest
from Investor import *
import random

class InvestorTestCase(unittest.TestCase):

	def test_run_simulation(self):
		'''Investor: Running a simulation returns...'''
		inv = Investor([1, 10], 10, 1000)
		inv.run_simulation(10)