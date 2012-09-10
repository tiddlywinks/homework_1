import unittest
import web
from test_utils import *
from app.models.query import Query
from paste.fixture import TestApp
from application import app

class QueryTests(unittest.TestCase):
	def setUp(self):
		self.query = Query()

	def test_continent(self):
		storage = web.Storage()
		storage.continent = 'AS'
		storage.natural_hazard='earthquake'
		self.query.execute(storage)

if __name__ == '__main__':
    print "=================="
    print "STARTING - QueryCountries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(QueryTests)
    unittest.TextTestRunner(verbosity=2).run(suite)