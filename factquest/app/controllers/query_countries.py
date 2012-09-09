import web
from config import debug, geo_url
from bs4 import BeautifulSoup
from ..models.countries import Countries
from ..models.query_parser import QueryParser
import json
if debug:
	from ..mock import urllib2
else:
	import urllib2

def url_map(country):
	pass

class QueryCountries:
	def GET(self):
		input = web.input()
		countries = Countries.byContinent(input.continent)
		qp = QueryParser()
		qp.parse(input)