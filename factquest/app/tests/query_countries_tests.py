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
	
	def _test_QueryCountriesForEarthquake(self):
		continents = get_continents()
		continents = continents[0:1]
		msg = 'countries in %s with earthquakes: %s'
		hazards = ['earthquake']
		for continent in continents:
			for hazard in hazards:
				r = self.testApp.get('/countries/?continent=%s&natural_hazard=%s' % (continent['code'], hazard))
				countries = json.loads(r.body)
				print msg % (continent['code'], str(countries))
	
	def test_QueryCountriesForMoreThanNPoliticalParties(self):
		continents = get_continents()
		continents = continents[0:1]
		msg = 'countries in %s with more than %d political parties: %s'
		for continent in continents:
			for party_count in range(5, 8):
				r = self.testApp.get('/countries/?continent=%s&political_party_count_gt_n=%s' % (continent['code'], party_count))
				countries = json.loads(r.body)
				self.assertIsInstance(countries, list)
				print msg % (continent['code'], party_count, str(countries))

	def _test_QueryCountriesWithColorFlag(self):
		colors = ['blue', 'red', 'lavendar']
		msg = 'countries with %s in flag: %s'
		for color in colors:
			r = self.testApp.get('/countries/?continent=NA&flag_contains_color=%s' % color)
			countries = json.loads(r.body)
			self.assertIsInstance(countries, list)
			print msg % (color, str(countries))

	def _QueryCountriesLandlocked(self):
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