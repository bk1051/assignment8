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

	def run_simulation(self, num_investments):
		'''Run a single simulation with a given number of shares'''
		position_value = self.initial_budget / num_investments
		# Create the simulator object
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, num_investments, seed=random.randint(10e2, 10e6))

		cumu_ret = np.array(self.num_trials)
		daily_ret = np.array(self.num_trials)

		for trial in range(self.num_trials):
			trial_returns = simulator.run() * position_value
			cumu_ret[trial] = np.sum(trial_returns)


	def plot():
		pass