from countries import Countries
from crawler import Crawler
import strategies

class Query():
	_country_url = 'https://www.cia.gov/library/publications/the-world-factbook/geos/%s.html'
	"""the query parser maps from_<property>=x and to_<property>=y as x < country.property < y
	count_<propety> will map to len()"""
	def __init__(self, input):
		countries = Countries.byContinent(input['continent'].lower() if input.has_key('continent') else '')
		del input['continent']
		self.country_urls = [(country, Query._country_url % country['code'].lower() if country['code'] else '') for country in countries]
		for key in input:
			self.strategy_name = key
			self.parameters = input[key]
	def execute(self):
		print 'queyr.parameters: %s with type %s' % (str(self.parameters), str(type(self.parameters)))
		strategy = getattr(strategies, self.strategy_name) # get the strategy from module
		clr = Crawler(urls=[url for (c, url) in self.country_urls])
		pages = clr.crawl()
		print 'query.execute pages: %s' % len([page for page in pages if page['response']])
		mask = map(lambda page: strategy(page['response'], self.parameters), pages)
		print 'result map: ' + str(map)
		result_pages = [page['url'] for (page, satisfied) in zip(pages, mask) if satisfied]
		print 'result_pages: ' + str(result_pages)
		result = [country for (country, url) in self.country_urls if url in result_pages]
		return result