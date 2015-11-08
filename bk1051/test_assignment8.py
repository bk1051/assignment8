import unittest
from assignment8 import *

class assignment8_testcase(unittest.TestCase):

	def test_parse_positions(self):
		self.assertEqual(parse_positions("1, 10, 100, 1000"), [1, 10, 100, 1000])
		self.assertEqual(parse_positions("1 10 100 1000"), [1, 10, 100, 1000])
		with self.assertRaises(PositionsParseException):
			parse_positions("hello")

	def test_quit(self):
		with self.assertRaises(QuitException):
			parse_positions("quit")

		with self.assertRaises(QuitException):
			parse_positions("Please QUIT")

		with self.assertRaises(QuitException):
			parse_num_trials("Please QUIT")
		