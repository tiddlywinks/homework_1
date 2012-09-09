import unittest
from test_utils import *
from app.controllers.query_countries import QueryCountries
import urllib2
import json
from paste.fixture import TestApp
from nose.tools import *
from application import app

class QueryCountriesTests(unittest.TestCase):
	def setUp(self):
		middleware = []
		self.testApp = TestApp(app.wsgifunc(*middleware))
	
	def test_QueryCountriesForEarthquake(self):
		continents = get_continents()
		hazards = ['earthquake']
		for continent in continents:
			for hazard in hazards:
				r = self.testApp.get('/countries/?continent=%s&natural_hazard=%s' % (continent, hazard))
				countries = json.loads(r)
				self.assertIsInstance(list)
	
	def test_QueryCountriesForMoreThanNPoliticalParties(self):
		continents = get_continents()
		for continent in continents:
			for party_count in range(10, 12):
				r = self.testApp.get('/countries/?continent=%s&start_party_count=%s' % (continent, party_count))
				countries = json.loads(r)
				self.asertIsInstance(list)

	def test_QueryCountriesWithColorFlag(self):
		continents = get_continents()
		colors = ['blue', 'red']
		for continent in continents:
			for color in colors:
				r = self.testApp.get('/countries/?flag_contains=%s' % color)
				countries = json.loads(r)
				self.assertIsInstance(list)

	def test_QueryCountriesLandlocked(self):
		r = self.testApp.get('/countries/?flag_contains=%s' % color)
		countries = json.loads(r)
		self.assertIsInstance(list)

if __name__ == '__main__':
    print "=================="
    print "STARTING - QueryCountries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(QueryCountriesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)