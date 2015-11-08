

class Investor(object):

	def __init__(self, positions, num_trials):
		self.positions = positions
		self.num_trials = num_trials
		self.initial_budget = 1000

	def run_simulations(self):
		simulator = Simulator({.51: 1.0, .49: -1.0})
		for trial in num_trials:
			simulator.run()

	def plot():
		pass