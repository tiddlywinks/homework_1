import unittest
from paste.fixture import TestApp
from nose.tools import *
import os
import sys
sys.path.append(os.path.abspath('../..'))
import json
from app.controllers.countries import ByContinent
from application import app

class CountriesTests(unittest.TestCase):
	def setUp(self):
		middleware = []
		self.testApp = TestApp(app.wsgifunc(*middleware))
		
	def test_GetWithNoParams(self):
		r = self.testApp.get('/countries/')
		self.assertEqual(r.status, 200)
		countries = json.loads(r.body)
		self.assertListEqual(countries, ByContinent._countries)
		
	def test_GetCountriesByContinent(self):
		r = self.testApp.get('/continents/')
		continents = json.loads(r.body)
		for continent in continents:
			r = self.testApp.get('/countries/%s' % continent['code'])
			self.assertEqual(r.status, 200)
			responseCountries = json.loads(r.body)
			actualCountries = [c for c in ByContinent._countries if c['continent'] == continent['code']]
			self.assertListEqual(responseCountries, actualCountries)

if __name__ == '__main__':
    print "=================="
    print "STARTING - countries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(CountriesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)