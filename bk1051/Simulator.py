import numpy as np

class InvalidReturnsException(Exception):
	'''Exception thrown when initialized with invalid returns dict'''
	pass

class Simulator(object):


	def __init__(self, returns, nrows, ncols, seed=0):
		self.returns = returns
		try:
			self.ranges = self.returns.keys()
			self.ranges.sort(key=lambda rng: rng[0])
		except AttributeError:
			raise InvalidReturnsException("Could not set and sort ranges in returns.")

		self._validate_returns()
		self.nrows, self.ncols = nrows, ncols

		#self.num_trials = num_trials
		# Initialize random seed
		np.random.seed(seed)

	def _validate_returns(self):
		'''Validate the returns dict'''

		print self.ranges
		for i in range(len(self.ranges) - 1):
			if self.ranges[i][1] != self.ranges[i+1][0]:
				raise InvalidReturnsException("Nonoverlapping ranges in returns")

		if self.ranges[-1][1] != 1:
			raise InvalidReturnsException("Last returns range must end in 1")

		if self.ranges[0][0] != 0:
			raise InvalidReturnsException("First return range must start with 0")


	def run(self):
		'''Run the simulation, returning the result'''
		# Create a random array of trials
		trials = np.random.rand(self.nrows, self.ncols)
		for interval in self.ranges:
			trials[np.logical_and(trials >= interval[0], trials < interval[1])] = self.returns[interval]
		print trials
		return trials