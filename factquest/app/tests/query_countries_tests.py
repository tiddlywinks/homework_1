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
		msg = 'countries in %s with earthquakes: %s'
		hazards = ['earthquake']
		for continent in continents:
			for hazard in hazards:
				r = self.testApp.get('/countries/?continent=%s&natural_hazard=%s' % (continent['code'], hazard))
				countries = json.loads(r)
				print msg % (continent, str(countries))
				self.assertIsInstance(list)
	
	def test_QueryCountriesForMoreThanNPoliticalParties(self):
		continents = get_continents()
		msg = 'countries in %s with more than %d political parties: %s'
		for continent in continents:
			for party_count in range(9, 11):
				r = self.testApp.get('/countries/?continent=%s&political_party_count_gt_n=%s' % (continent['code'], party_count))
				countries = json.loads(r)
				print msg % (continent, party_count, str(r))
				self.asertIsInstance(list)

	def test_QueryCountriesWithColorFlag(self):
		continents = get_continents()
		colors = ['blue', 'red']
		for continent in continents:
			for color in colors:
				r = self.testApp.get('/countries/?continent=%s&flag_contains_color=%s' % (continent['code'], color))
				countries = json.loads(r)
				self.assertIsInstance(list)

	def ignore_QueryCountriesLandlocked(self):
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