from countries import Countries
from crawler import Crawler
import strategies

class Query():
	_country_url = 'https://www.cia.gov/library/publications/the-world-factbook/geos/%s.html'
	def __init__(self, input):
		continent = ''
		if input.has_key('continent'):
			continent = input['continent'].lower()
			del input['continent']
		countries = Countries.byContinent(continent)
		self.country_urls = [(country, Query._country_url % country['code'].lower() if country['code'] else '') for country in countries]
		# TODO make strategy_name and parameters separate parts of query
		for key in input:
			self.strategy_name = key
			self.parameters = input[key]
		
	def execute(self):
		strategy = getattr(strategies, self.strategy_name) # get the strategy from module
		clr = Crawler(urls=[url for (c, url) in self.country_urls])
		pages = clr.crawl()
		result = None
		if 'all_pages' in dir(strategy): # i.e. max degrees
			result = strategy(all_pages, self.parameters)
		else:
			mask = map(lambda page: strategy(page['response'], self.parameters), pages)
			result_pages = [page['url'] for (page, satisfied) in zip(pages, mask) if satisfied]
			result = [country for (country, url) in self.country_urls if url in result_pages]
		return result