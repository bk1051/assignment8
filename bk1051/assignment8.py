import Investor
import re

# String to quit program
QUIT = 'quit'
# Budget for investiment on first day
BUDGET = 1000

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
		print element
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


def run():
	positions = ask_for_positions()
	num_trials = ask_for_num_trials()
	
	investor = Investor(positions, num_trials, BUDGET)
	investor.run_simulations()

	investor.plot()





if __name__ == '__main__':
	try:
		run()
	except (QuitException, KeyboardInterrupt):
		print "\nQuitting program\n"
	except Exception as e:
		print "Uncaught exception:"
		print e