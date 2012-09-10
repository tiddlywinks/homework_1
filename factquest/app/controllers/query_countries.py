import web
from config import debug, geo_url
from bs4 import BeautifulSoup
from ..models.countries import Countries
from ..models.query import Query
import json
if debug:
	from ..mock import urllib2
else:
	import urllib2

class QueryCountries:
	def GET(self):
		input = web.input()
		qp = Query()
		r = qp.execute(input)
		web.header('Content-Type', 'application/json')
		return json.dumps(r)