import random
from Simulator import Simulator
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Investor(object):
	'''Represents an object that simulates a set of investments
	and outputs the results.'''

	def __init__(self, positions, num_trials, initial_budget):
		'''Constructor.

		Args:
			positions: the number of positions to take
			num_trials: the number of simulation trials to run
			initial_budget: the initial budget to spend on the positions
		'''
		self.positions = positions
		self.num_trials = num_trials
		self.initial_budget = initial_budget
		self.run_simulations()


	def run_simulations(self):
		'''Run all the simulations for each position'''
		self.results = []
		for position in self.positions:
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

		# Run the simulator, and multiply each of the results by the value
		# of a share for this position
		trial_returns = simulator.run() * position_value

		# Collapse all investments on each day into cumulative return
		cumu_ret = self.initial_budget + trial_returns.sum(axis=0)

		# The daily rate of return, which is the final result
		daily_ret = (cumu_ret / float(self.initial_budget)) - 1.

		return daily_ret


	def get_results(self):
		'''Return array of summary results

		Each position's result is a single row, with the columns:
		number of positions, mean returns, standard deviation of returns
		'''
		positions = np.array(self.positions)
		results = np.vstack(self.results)
		means = results.mean(axis=1)
		stds = results.std(axis=1)
		return np.vstack((positions, means, stds)).T


	def plot(self):
		'''Output a histogram of returns for each position'''
		for i, result in enumerate(self.results):

			plt.figure()
			plt.hist(result, 100, range=[-1,1]) # Using 101 bins looks better, but assignment specifies 100 bins
			
			# Set title based on parameters of the result
			plt.title("Returns from {0:,} Position{1}, {2:,} Simulations".format(
				(self.positions[i]), 
				's' if self.positions[i] > 1 else '', # Make "position" plural if number of positions > 1
				self.num_trials))

			# Label axes
			plt.xlabel("Return")
			plt.ylabel("Number of Trials")

			# Save figure as PDF
			filename = "histogram_{0:04.0f}_pos.pdf".format(self.positions[i])
			try:
				plt.savefig(filename)
			except IOError:
				print "Could not save figure {0}. Check that file is writable.".format(filename)
			else:
				print "Saved figure {0}".format(filename)

			plt.close()






