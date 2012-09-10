from countries import Countries
from crawler import Crawler
import strategies

class Query():
	_country_url = 'https://www.cia.gov/library/publications/the-world-factbook/geos/%s.html'
	"""the query parser maps from_<property>=x and to_<property>=y as x < country.property < y
	count_<propety> will map to len()"""
	def execute(self, input):
		countries = Countries.byContinent(input['continent'] if input.has_key('continent') else '')
		del input['continent']
		country_urls = [(country, Query._country_url % country['code'].lower() if country['code'] else '') for country in countries]
		clr = Crawler(urls=[url for (c, url) in country_urls])
		pages = clr.crawl()
		for key in input:
			strategy_name = key
			parameters = input[key]
		strategy = getattr(strategies, strategy_name)
		mask = map(lambda page: strategy(page['response'], parameters), pages)
		result_pages = [page['url'] for (page, satisfied) in zip(pages, mask) if satisfied]
		result = [country for (country, url) in country_urls if url in result_pages]
		return result