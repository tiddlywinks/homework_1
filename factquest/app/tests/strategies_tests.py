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
		f = open('greece.htm', 'r')
		self.greece = f.read()
		f.close()
		f = open('kosovo.htm', 'r')
		self.kosovo = f.read()
		f.close()
		f = open('albania.htm', 'r')
		self.albania = f.read()
		f.close()
		f = open('macedonia.htm', 'r')
		self.macedonia = f.read()
		f.close()
		f = open('senegal.htm', 'r')
		self.senegal = f.read()
		f.close()
		f = open('gambia.htm', 'r')
		self.gambia = f.read()
		f.close()
		f = open('guinea-bissau.htm', 'r')
		self.guinea_bissau = f.read()
		f.close()
		f = open('russia.htm', 'r')
		self.russia = f.read()
		f.close()
	def test_country(self):
		r = strategies.country(self.kosovo)
		self.assertEqual(r, 'Kosovo')
		r = strategies.country(self.albania)
		self.assertEqual(r, 'Albania')
		r = strategies.country(self.macedonia)
		self.assertEqual(r, 'Macedonia')
		r = strategies.country(self.vatican)
		self.assertEqual(r, 'Holy See (Vatican City)')
	def test_category_hazards(self):
		category_data = strategies.category(self.egypt, 'natural hazards')
		self.assertTrue(category_data.startswith("periodic droughts; frequent"))
	def test_category_political_parties(self):
		category_data = strategies.category(self.egypt, 'political parties')
		self.assertTrue(category_data.startswith("Al-Wasat Party;"))
	def test_category_flag(self):
		category_data = strategies.category(self.egypt, 'flag')
		self.assertTrue(category_data.startswith("three equal horizontal bands"))
	def test_natural_hazard(self):
		for hazard in StrategiesTests._hazards:
			self.assertTrue(strategies.natural_hazard(self.egypt, hazard))
		self.assertFalse(strategies.natural_hazard(self.egypt, 'fake_hazard'))
	def	test_political_party_count(self):
		self.assertEqual(strategies.political_party_count(self.egypt), 10)
		self.assertEqual(strategies.political_party_count(self.algeria), 15)
	def test_political_party_count_gt_n(self):
		self.assertTrue(strategies.political_party_count_gt_n(self.egypt, 9))
		self.assertFalse(strategies.political_party_count_gt_n(self.egypt, 10))
		self.assertTrue(strategies.political_party_count_gt_n(self.egypt, 5))
		self.assertTrue(strategies.political_party_count_gt_n(self.algeria, 14))
		self.assertFalse(strategies.political_party_count_gt_n(self.algeria, 15))
	def test_flag_contains_color(self):
		self.assertTrue(strategies.flag_contains_color(self.egypt, 'red'))
		self.assertTrue(strategies.flag_contains_color(self.egypt, 'white'))
		self.assertTrue(strategies.flag_contains_color(self.egypt, 'black'))
		self.assertFalse(strategies.flag_contains_color(self.egypt, 'lavendar'))
	def test_enclave(self):
		self.assertFalse(strategies.enclave(self.egypt, 1))
		self.assertTrue(strategies.enclave(self.vatican, 1))
	def test__capital_coordinates(self):
		r = strategies._capital_coordinates(self.anguilla, 1)
		self.assertEqual(r['country'], 'Anguilla')
		self.assertEqual(r['capital'], 'The Valley')
		coordinates = r['coordinates']
		self.assertEqual(coordinates['latitude'], 18.13)
		self.assertEqual(coordinates['longitude'], -63.03)
		
		r = strategies._capital_coordinates(self.russia, 1)
		self.assertEqual(r['country'], 'Russia')
		self.assertEqual(r['capital'], 'Moscow')
		coordinates = r['coordinates']
		self.assertEqual(coordinates['latitude'], 55.45)
		self.assertEqual(coordinates['longitude'], 37.36)
		
		
		r = strategies._capital_coordinates(self.vatican, 1)
		self.assertEqual(r['country'], 'Holy See (Vatican City)')
		self.assertEqual(r['capital'], 'Vatican City')
		coordinates = r['coordinates']
		self.assertEqual(coordinates['latitude'], 41.54)
		self.assertEqual(coordinates['longitude'], 12.27)
		
		r = strategies._capital_coordinates(self.egypt, 1)
		self.assertEqual(r['country'], 'Egypt')
		self.assertEqual(r['capital'], 'Cairo')
		coordinates = r['coordinates']
		self.assertEqual(coordinates['latitude'], 30.03)
		self.assertEqual(coordinates['longitude'], 31.15)

	def test_capital_coordinates(self):
		# greece: 37.59, 23.44
		# kosovo: 42.40, 21.10
		country_input = [self.kosovo, self.albania, self.macedonia, self.greece, self.senegal, self.gambia, self.guinea_bissau, self.russia]
		expected_capitals = ['Pristina (Prishtine, Prishtina)', 'Tirana (Tirane)', 'Skopje', 'Athens']
		result = strategies.capital_coordinates(country_input, 10)
		for expected_capital in expected_capitals:
			matches = [1 for capital_coords in result if capital_coords['capital'] == expected_capital]
			self.assertEqual(len(matches), 1)

if __name__ == '__main__':
    print "=================="
    print "STARTING - Strategies TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(StrategiesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)