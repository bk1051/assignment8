import random
from Simulator import Simulator
import numpy as np

class Investor(object):

	def __init__(self, positions, num_trials, initial_budget):
		self.positions = positions
		self.num_trials = num_trials
		self.initial_budget = initial_budget
		# Set inital seed for random generator
		#random.seed(9876)
		self.run_simulations()

	def run_simulations(self):
		self.results = []
		for i, position in enumerate(self.positions):
			self.results.append(self._run_simulation(position))
		return self.results


	def _run_simulation(self, num_investments):
		'''Run a single simulation with a given number of investments

		For each position, the number of investments is the number of rows.
		For each investment, we run num_trial trials, where each trial is
		a column in that row.

		We multiply all the trials for each investment by the value of that
		investment, which is simply the intial budget divided by the number
		of investments.

		For each trial (column), we sum up the returns from all the investments
		(rows), producing a 1xnum_trials array with the cumulative returns from 
		each day.'''

		position_value = self.initial_budget / num_investments

		# Create the simulator object
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, 
			nrows=num_investments, 
			ncols=self.num_trials) 
			#seed=random.random()) # random seed

		# Run the simulator, and multiply each of the results by the value
		# of a share for this position
		trial_returns = simulator.run() * position_value

		# Collapse all investments on each day into cumulative return
		cumu_ret = trial_returns.sum(axis=0)
		# The daily rate of return
		daily_ret = (cumu_ret / 1000.) - 1.

		return daily_ret

	def get_results(self):
		'''Return summary results'''
		positions = np.array(self.positions)
		results = np.vstack(self.results)
		means = results.mean(axis=1)
		stds = results.std(axis=1)
		print results
		print means
		print stds
		return np.vstack((positions, means, stds)).T


	def plot(self):
		pass