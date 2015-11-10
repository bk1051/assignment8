import numpy as np

class InvalidReturnsException(Exception):
	'''Exception thrown when initialized with invalid returns dict'''
	pass

class Simulator(object):
	'''Represents an object that runs simulations.'''

	def __init__(self, returns, nrows, ncols, seed=0):
		'''Constructor.

		Args:
			returns: a dict where the key is a tuple representing a range in [0, 1)
						and the value is the return if the simulated random value is
						within that range. All the ranges must completely cover [0, 1)
						and be non-overlapping. Invalid returns dicts will throw an
						InvalidReturnsException
			nrows: the number of rows in the simulation array
			ncols: the number of columns in the simulation array
			seed: (optional) a seed for the random number generator
		'''
		self.returns = returns
		try:
			self.ranges = self.returns.keys()
			self.ranges.sort(key=lambda rng: rng[0])
		except AttributeError:
			raise InvalidReturnsException("Could not set and sort ranges in returns.")

		self._validate_returns()
		self.nrows, self.ncols = nrows, ncols

		# Initialize random seed
		np.random.seed(seed)

	def _validate_returns(self):
		'''Validate the returns dict. Throws an InvalidReturnsException if
		the ranges that are the keys overlap or do not completely cover the 
		interval [0, 1)
		'''
		for i in range(len(self.ranges) - 1):
			if self.ranges[i][1] != self.ranges[i+1][0]:
				raise InvalidReturnsException("Nonoverlapping ranges in returns")

		if self.ranges[-1][1] != 1:
			raise InvalidReturnsException("Last returns range must end in 1")

		if self.ranges[0][0] != 0:
			raise InvalidReturnsException("First return range must start with 0")


	def run(self):
		'''Run the simulation, returning the result'''
		# Create a random array of trials, and an array of returns initialized to zero
		trials = np.random.rand(self.nrows, self.ncols)
		returns = np.zeros_like(trials)

		# Go through each range specify the returns dict, and if the trial value is
		# within that range, set the value of that trial's return to the return value
		# of that range
		for interval in self.ranges:
			returns[np.logical_and(trials >= interval[0], trials < interval[1])] = self.returns[interval]
			
		return returns


