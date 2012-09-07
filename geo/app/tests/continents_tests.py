import unittest
import os
import sys
sys.path.append(os.path.abspath('../..'))
import json
from paste.fixture import TestApp
from nose.tools import *
from app.controllers.continents import List
from application import app

class ContinentsTests(unittest.TestCase):
	def setUp(self):
		middleware = []
		self.testApp = TestApp(app.wsgifunc(*middleware))
		
	def test_List_GET(self):
		r = self.testApp.get('/continents/')
		assert_equal(r.status, 200)
		continents = json.loads(r.body)
		self.assertListEqual(continents, List._continents)

if __name__ == '__main__':
    print "=================="
    print "STARTING - continents TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(ContinentsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)