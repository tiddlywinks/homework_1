import unittest
from test_utils import *
from app.models.countries import Countries

class CountriesTests(unittest.TestCase):
	def test_byContinent(self):
		continents = get_continents()
		for continent in map(lambda continent: continent['code'], continents):
			countries = Countries.byContinent(continent)
			self.assertIsInstance(countries, list)
			for country in countries:
				self.assertEqual(continent, country['continent'])

if __name__ == '__main__':
    print "=================="
    print "STARTING - countries TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(CountriesTests)
    unittest.TextTestRunner(verbosity=2).run(suite)