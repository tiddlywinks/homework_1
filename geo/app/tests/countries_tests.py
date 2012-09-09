import unittest
from paste.fixture import TestApp
from nose.tools import *
import os
import sys
sys.path.append(os.path.abspath('../..'))
import json
from app.controllers.countries import ByContinent
from app.models.countries import Countries
from application import app

class CountriesTests(unittest.TestCase):
	def setUp(self):
		middleware = []
		self.testApp = TestApp(app.wsgifunc(*middleware))
		
	def test_Countries(self):
		countries = Countries.find(lambda c: True)
		with_code = [country for country in countries if country['code']]
		self.assertTrue(len(with_code)/float(len(countries)) > 0.67)
		
	def test_GetWithNoParams(self):
		r = self.testApp.get('/countries/')
		self.assertEqual(r.status, 200)
		countries = json.loads(r.body)
		self.assertListEqual(countries, Countries.find(lambda c: True))
		
	def test_GetCountriesByContinent(self):
		r = self.testApp.get('/continents/')
		self.assertEqual(r.status, 200)
		continents = json.loads(r.body)
		for continent in continents:
			r = self.testApp.get('/countries/%s' % continent['code'])
			actualCountries = [c for c in Countries._countries if c['continent'] == continent['code']]
			self.assertEqual(r.status, 200)
			responseCountries = json.loads(r.body)
			self.assertListEqual(responseCountries, actualCountries)

if __name__ == '__main__':
    print "=================="
    print "STARTING - countries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(CountriesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)