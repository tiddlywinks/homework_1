import unittest
import web
from test_utils import *
from app.models.query import Query
from paste.fixture import TestApp
from application import app

class QueryTests(unittest.TestCase):
	def test_asia_earthquakes(self):
		storage = web.Storage()
		storage.continent = 'AS'
		storage.natural_hazard='earthquake'
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		# print 'countries in Asia with earthquakes: %s' % str(countries)
		
	def test_africa_political_parties_greater_than_10(self):
		storage = web.Storage()
		storage.continent = 'AF'
		storage.political_party_count_gt_n = 10
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		# print 'countries in Africa with political parties > 10: %s' % str(countries)
		
	def test_na_flag_contains_color_orange(self):
		storage = web.Storage()
		storage.continent = 'NA'
		storage.flag_contains_color = 'orange'
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		self.assertEqual(len(countries), 2)
		# print 'countries in North America with flags containing color orange: %s' % str(countries)
		
	def test_enclave(self):
		storage = web.Storage()
		storage.enclave = 1
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		self.assertEqual(len(countries), 3)
		# print 'Enclave countries: %s' % str(countries)
		
	def test_max_within_n_degrees(self):
		storage = web.Storage()
		storage.max_within_n_degrees = 10
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		# print 'Max countries within 10 degrees: %s' % str(countries)

if __name__ == '__main__':
    print "=================="
    print "STARTING - QueryCountries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(QueryTests)
    unittest.TextTestRunner(verbosity=2).run(suite)