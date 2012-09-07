import unittest
import os
import sys
sys.path.append(os.path.abspath('..'))
from mock import urllib2

class Urllib2Tests(unittest.TestCase):
	def setUp(self):
		os.chdir('..')
		self.url = 'http://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)'

	def test_Request(self):
		req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"})
		self.assertEqual(req.filename, 'List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)')
		con = urllib2.urlopen(req)
		t = con.read()
		self.assertTrue(len(t) == 39540)

if __name__ == '__main__':
    print "=================="
    print "STARTING - mock TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(Urllib2Tests)
    unittest.TextTestRunner(verbosity=2).run(suite)