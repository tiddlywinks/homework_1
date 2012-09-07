import unittest
import os
import sys
sys.path.append(os.path.abspath('../..'))
import urllib2
import json
from paste.fixture import TestApp
from nose.tools import *

class QuestTests(unittest.TestCase):
	def setUp(self):
		middleware = []
		self.testApp = TestApp(app.wsgifunc(*middleware))
	
if __name__ == '__main__':
    print "=================="
    print "STARTING - continents TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(QuestTests)
    unittest.TextTestRunner(verbosity=2).run(suite)