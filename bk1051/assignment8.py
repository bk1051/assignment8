"""
Assignment 8

Author: Brian Karfunkel (bk1051)
Date: 11/9/2015

This program asks the user for a number of positions and a number
of trials to run. It then simulates a biased coinflip for each position,
repeating the simulation for every trial. Using the results, the program
outputs PDFs of histograms for all the trials, as well as a text file
with the means and standard deviations for each set of positions.
"""

from Investor import Investor
import re

# String to quit program
QUIT = 'quit'
# Budget for investiment on first day
BUDGET = 1000

# Custom exceptions
class PositionsParseException(Exception):
	pass

class NumTrialsParseException(Exception):
	pass

class QuitException(Exception):
	pass



def parse_positions(input_string):
	'''Parse the positions input into a list.

	Raises a PositionsParseException if cannot be parsed
	Raises a QuitException if user enters the quit string'''
	# Test for quit
	if QUIT in input_string.lower():
		raise QuitException("Quitting...")

	# Split the input string on either spaces or commas
	list_re = r'(\s|[,])+'
	input_string = re.sub('[[()\]]', '', input_string)
	elements = re.split(list_re, input_string)

	# For each element of the list, test if it is all digits
	# and an integer. If it is, add it to the output list.
	# Otherwise, if it's not a delimiter, throw and exception.
	positions = []
	for element in elements:
		if element.isdigit() and float(element)==int(element):
			positions.append(int(element))
		elif re.match(list_re, element):
			continue
		else:
			raise PositionsParseException("List items must be integers")

	return positions


def parse_num_trials(input_string):
	'''Parse the number of trials.

	Raises a NumTrialsParseException if cannot be parsed
	Raises a QuitException if user enters the quit string'''
	if QUIT in input_string.lower():
		raise QuitException("Quitting...")

	if input_string.isdigit() and float(input_string)==int(input_string):
		return int(input_string)
	else:
		raise NumTrialsParseException("Number of trials must be an integer")


def ask_for_positions():
	'''Ask the user for list of positions, and return the parsed list

	If positions cannot be parsed, print an error message and ask again.'''
	try:
		return parse_positions(raw_input("What positions should be tested?\n> "))
	except PositionsParseException:
		print "Invalid positions. Please type a list of integers. Type '%s' to exit" % QUIT
		ask_for_positions()

def ask_for_num_trials():
	'''Ask the user for the number of trials, and return the parsed result.

	If number of trials cannot be parsed, print an error message and ask again.'''
	try:
		return parse_num_trials(raw_input("How many trials should be run?\n> "))
	except NumTrialsParseException:
		print "Invalid number of trials to run. Please input an integer. Type '%s' to exit" % QUIT
		ask_for_num_trials()

def output_results(results):
	'''Print results and save to text file'''
	print "Results of simulations:"
	with open('results.txt', 'w') as outfile:
		for result in results: # For each row
			outstring = "Number of Positions:  {positions:6.0f}  Mean:  {mean:6.4f}  Std. Dev.:  {std:6.4f}".format(
				positions=result[0],
				mean=result[1],
				std=result[2]
			)
			print outstring


def run():
	'''Main function for module. Asks for input, runs simulations, and outputs the results.'''
	positions = ask_for_positions()
	num_trials = ask_for_num_trials()
	
	print "Running trials..."
	investor = Investor(positions, num_trials, BUDGET)

	# Save the results to a text file and print to screen
	output_results(investor.get_results())

	# Save histograms as PDFs
	investor.plot()



# Run the module
if __name__ == '__main__':
	try:
		run()
	except (QuitException, KeyboardInterrupt):
		print "\nQuitting program\n"