

class Investor(object):

	def __init__(self, positions, num_trials, initial_budget):
		self.positions = positions
		self.num_trials = num_trials
		self.initial_budget = initial_budget

	def run_simulations(self):
		simulator = Simulator({(0, .51): 1.0, (.51, 1): -1.0}, num_trials)
		for trial in num_trials:
			simulator.run()

	def plot():
		pass