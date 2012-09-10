import unittest
import web
from test_utils import *
from app.models.query import Query
from paste.fixture import TestApp
from application import app

class QueryTests(unittest.TestCase):
	def _test_asia_earthquakes(self):
		storage = web.Storage()
		storage.continent = 'AS'
		storage.natural_hazard='earthquake'
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		print 'countries in asia with earthquakes: %s' % str(countries)
	def test_africa_political_parties_greater_than_10(self):
		storage = web.Storage()
		storage.continent = 'AF'
		storage.political_party_count_gt_n = 10
		query = Query(storage)
		countries = query.execute()
		self.assertIsInstance(countries, list)
		print 'countries in africa with political parties > 10: %s' % str(countries)

if __name__ == '__main__':
    print "=================="
    print "STARTING - QueryCountries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(QueryTests)
    unittest.TextTestRunner(verbosity=2).run(suite)