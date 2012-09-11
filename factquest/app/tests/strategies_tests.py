from test_utils import *
import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
from models import strategies

class StrategiesTests(unittest.TestCase):
	_hazards = ['earthquake', 'drought', 'floods', 'landslides']
	def setUp(self):
		f = open('egypt.htm', 'r')
		self.egypt = f.read()
		f.close()
		f = open('algeria.htm', 'r')
		self.algeria = f.read()
		f.close()
		f = open('vatican.htm', 'r')
		self.vatican = f.read()
		f.close()
		f = open('anguilla.htm', 'r')
		self.anguilla = f.read()
		f.close()
		f = open('russia.htm', 'r')
		self.russia = f.read()
		f.close()
	def _test_category_hazards(self):
		category_data = strategies.category(self.egypt, 'natural hazards')
		self.assertTrue(category_data.startswith("periodic droughts; frequent"))
	def _test_category_political_parties(self):
		category_data = strategies.category(self.egypt, 'political parties')
		self.assertTrue(category_data.startswith("Al-Wasat Party;"))
	def _test_category_flag(self):
		category_data = strategies.category(self.egypt, 'flag')
		self.assertTrue(category_data.startswith("three equal horizontal bands"))
	def _test_natural_hazard(self):
		for hazard in StrategiesTests._hazards:
			self.assertTrue(strategies.natural_hazard(self.egypt, hazard))
		self.assertFalse(strategies.natural_hazard(self.egypt, 'fake_hazard'))
	def	_test_political_party_count(self):
		self.assertEqual(strategies.political_party_count(self.egypt), 10)
		self.assertEqual(strategies.political_party_count(self.algeria), 15)
	def _test_political_party_count_gt_n(self):
		self.assertTrue(strategies.political_party_count_gt_n(self.egypt, 9))
		self.assertFalse(strategies.political_party_count_gt_n(self.egypt, 10))
		self.assertTrue(strategies.political_party_count_gt_n(self.egypt, 5))
		self.assertTrue(strategies.political_party_count_gt_n(self.algeria, 14))
		self.assertFalse(strategies.political_party_count_gt_n(self.algeria, 15))
	def _test_flag_contains_color(self):
		self.assertTrue(strategies.flag_contains_color(self.egypt, 'red'))
		self.assertTrue(strategies.flag_contains_color(self.egypt, 'white'))
		self.assertTrue(strategies.flag_contains_color(self.egypt, 'black'))
		self.assertFalse(strategies.flag_contains_color(self.egypt, 'lavendar'))
	def _test_enclave(self):
		self.assertFalse(strategies.enclave(self.egypt, 1))
		self.assertTrue(strategies.enclave(self.vatican, 1))
	def test_capital_coords(self):
		r = strategies.capital_coordinates(self.anguilla, 1)
		self.assertEqual(r, ('The Valley', (18.13, -63.03)))
		r = strategies.capital_coordinates(self.russia, 1)
		self.assertEqual(r, ('Moscow', (55.45, 37.36)))
		r = strategies.capital_coordinates(self.vatican, 1)
		self.assertEqual(r, ('Vatican City', (41.54, 12.27)))
		r = strategies.capital_coordinates(self.egypt, 1)
		self.assertEqual(r, ('Cairo', (30.03, 31.15)))
		
if __name__ == '__main__':
    print "=================="
    print "STARTING - Strategies TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(StrategiesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)