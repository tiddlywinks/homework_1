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
		strategy = getattr(strategies, self.strategy_name)
		clr = Crawler(urls=[url for (c, url) in self.country_urls])
		pages = clr.crawl()
		mask = map(lambda page: strategy(page['response'], self.parameters), pages)
		result_pages = [page['url'] for (page, satisfied) in zip(pages, mask) if satisfied]
		result = [country for (country, url) in self.country_urls if url in result_pages]
		return result