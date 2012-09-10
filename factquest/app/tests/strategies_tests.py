from test_utils import *
import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
from models import strategies

class StrategiesTests(unittest.TestCase):
	_hazards = ['earthquake', 'drought', 'floods', 'landslides']
	def setUp(self):
		f = open('input.htm', 'r')
		self.html = f.read()
		f.close()
		f = open('input2.htm', 'r')
		self.html2 = f.read()
		f.close()
	def _test_category_hazards(self):
		category_data = strategies.category(self.html, 'natural hazards')
		self.assertTrue(category_data.startswith("periodic droughts; frequent"))
	def _test_category_political_parties(self):
		category_data = strategies.category(self.html, 'political parties')
		self.assertTrue(category_data.startswith("Al-Wasat Party;"))
	def _test_category_flag(self):
		category_data = strategies.category(self.html, 'flag')
		self.assertTrue(category_data.startswith("three equal horizontal bands"))
	def _test_natural_hazard(self):
		for hazard in StrategiesTests._hazards:
			self.assertTrue(strategies.natural_hazard(self.html, hazard))
		self.assertFalse(strategies.natural_hazard(self.html, 'fake_hazard'))
	def	test_political_party_count(self):
		self.assertEqual(strategies.political_party_count(self.html), 10)
		self.assertEqual(strategies.political_party_count(self.html2), 15)
	def test_political_party_count_gt_n(self):
		self.assertTrue(strategies.political_party_count_gt_n(self.html, 9))
		self.assertFalse(strategies.political_party_count_gt_n(self.html, 10))
		self.assertTrue(strategies.political_party_count_gt_n(self.html, 5))
		self.assertTrue(strategies.political_party_count_gt_n(self.html2, 14))
		self.assertFalse(strategies.political_party_count_gt_n(self.html2, 15))
	def _test_flag_contains_color(self):
		self.assertTrue(strategies.flag_contains_color(self.html, 'red'))
		self.assertTrue(strategies.flag_contains_color(self.html, 'white'))
		self.assertTrue(strategies.flag_contains_color(self.html, 'black'))
		self.assertFalse(strategies.flag_contains_color(self.html, 'lavendar'))
		
if __name__ == '__main__':
    print "=================="
    print "STARTING - Strategies TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(StrategiesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)