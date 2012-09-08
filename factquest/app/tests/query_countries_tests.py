import unittest
from app.
import os
import sys
sys.path.append(os.path.abspath('../..'))
import urllib2
import json
from paste.fixture import TestApp
from nose.tools import *
from test_utils import *

class QueryCountriesTests(unittest.TestCase):
	def setUp(self):
		middleware = []
		self.testApp = TestApp(app.wsgifunc(*middleware))
	
	def test_QueryCountriesForEarthquake(self):
		continents = getContinents()
		hazards = ['earthquake']
		for continent in continents:
			for hazard in hazards:
				r = self.testApp.get('/countries/?continent=%s&natural_hazard=%s' % (continent, hazard))
				countries = json.loads(r)
				self.assertIsInstance(list)
	
	def test_QueryCountriesForMoreThanNPoliticalParties(self):
		continents = getContinents()
		for continent in continents:
			for party_count in range(10, 12):
				r = self.testApp.get('/countries/?continent=%s&start_party_count=%s' % (continent, party_count))
				# the query parser will map from_<property>=x and to_<property>=y as x < country.property < y
				# count_<propety> will map to len()
				countries = json.loads(r)
				self.asertIsInstance(list)

	def test_QueryCountriesWithColorFlag(self):
		continents = getContinents()
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
    print "STARTING - continents TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(QueryCountriesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)