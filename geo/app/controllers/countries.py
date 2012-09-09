import web
from config import debug
from bs4 import BeautifulSoup
import json
from ..models.countries import Countries
if debug:
	from ..mock import urllib2
else:
	import urllib2

class ByContinent:
	def GET(self, continent_code):
		web.header('Content-Type', 'application/json')
		return json.dumps(Countries.find(lambda c: not continent_code or c['continent'] == continent_code))