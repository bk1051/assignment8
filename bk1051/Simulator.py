import numpy as np


class Simulator(object):


	def __init__(self, returns, num_trials, seed=0):
		self.returns = returns
		self.num_trials = num_trials
		# Initialize random seed
		np.random.seed(seed)

	def run(self):
		trials = np.random.rand(self.num_trials)
		for interval in self.returns.keys():
			trials[np.logical_and(trials >= interval[0], trials <= interval[1])] = self.returns[interval]
		return trials