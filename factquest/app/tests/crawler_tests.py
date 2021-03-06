import unittest
import sys
import os
sys.path.append(os.path.abspath('..'))
from models.crawler import Crawler

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

if __name__ == '__main__':
    print "=================="
    print "STARTING - Crawler TESTS"
    print "=================="
    print "######################################################################"
    suite = unittest.TestLoader().loadTestsFromTestCase(CrawlerTests)
    unittest.TextTestRunner(verbosity=2).run(suite)