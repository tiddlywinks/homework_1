from config import debug, geo_url
from bs4 import BeautifulSoup
import json
if debug:
	from ..mock import urllib2
else:
	import urllib2

class QueryCountries:
	def GET(self, ps):
		