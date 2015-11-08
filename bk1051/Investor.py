import random
from Simulator import Simulator

class Investor(object):

	def __init__(self, positions, num_trials, initial_budget):
		self.positions = positions
		self.num_trials = num_trials
		self.initial_budget = initial_budget
		# Set inital seed for random generator
		random.seed(9876)

	def run_simulations(self):
		for position in positions:
			self.run_simulation(postition)

	def run_simulation(self, num_shares):
		'''Run a single simulation with a given number of shares'''
		position_value = self.initial_budget / num_shares
		# Create the simulator object
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, num_shares, seed=random.randint(10e2, 10e6))
		for trial in range(self.num_trials):
			simulator.run()

	def plot():
		pass