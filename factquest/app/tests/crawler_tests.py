import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
from models.crawler import Crawler

# TODO wrapper that gets $('.category').after($(".category_data"))[0].innerHTML
class CrawlerTests(unittest.TestCase):
	TestUrls = [ "http://www.google.com", "http://www.markvelez.com", "https://www.cia.gov/library/publications/the-world-factbook/geos/ag.html", "http://k2_7.asdf1234.net"]
	def setUp(self):
		self.crawler = Crawler(CrawlerTests.TestUrls)
		
	def test_crawl(self):
		rs = self.crawler.crawl()
		for url_index in range(0, len(CrawlerTests.TestUrls)-2):
			self.assertEqual(CrawlerTests.TestUrls[url_index], rs[url_index]['url'])
			self.assertTrue(len(rs[url_index]['response']) > 0)
		lastIndex = len(CrawlerTests.TestUrls)-1
		badResult = rs[lastIndex]
		self.assertEqual(badResult['url'], CrawlerTests.TestUrls[lastIndex])
		self.assertIsNone(badResult['response'])
		self.assertIsNotNone(badResult['error'])
#
#	def test_CountryCrawler(self):
#		def countriesWithEarthquakes(t):
#			return 'earthquake' in t
#		def countriesWithMoreThanNParties(t, n):
#			import re
#			anchorWithParties = findAnchor() # do with bs4
#			partyText = anchorWithParties.after('.category_date').content # get the category_date immediately after
#			partyCount = len([m.start() for m in re.finditer(';', partyText)])-1
#			return partyCount > n
#		def countriesWithColorFlag(t, c):
#			import re
#			anchorWithParties = findAnchor() # do with bs4
#			partyText = anchorWithParties.after('.category_date').content # get the category_date immediately after
#			partyCount = len([m.start() for m in re.finditer(';', partyText)])-1
#			return partyCount > n
#		spider = CountrySpider(countries, countriesWithEarthquakes) # this takes a predicate that pages must satisfy
#		countriesWithEarthQuakes = spider.crawl()
#		actualCountriesWithEarthQuakes = []
#		spider = CountrySpider(countries, countriesWithMoreThanNParties, n) # this takes a predicate that pages must satisfy
#		countriesWithEarthQuakes = spider.crawl()
#		actualCountriesWithEarthQuakes = []


if __name__ == '__main__':
    print "=================="
    print "STARTING - Crawler TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(CrawlerTests)
    unittest.TextTestRunner(verbosity=2).run(suite)