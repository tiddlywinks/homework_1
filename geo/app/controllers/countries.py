import web
from config import debug
from bs4 import BeautifulSoup
import json
if debug:
	from ..mock import urllib2
else:
	import urllib2

class ByContinent:
	"""Gets the countries within a continent"""
	_url = "http://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
	_countries = []
	def load(self):
		# wikipedia blocks bots, the next 2 lines were borrowed from
		# http://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page
		req = urllib2.Request(ByContinent._url, headers={'User-Agent' : "Magic Browser"})
		con = urllib2.urlopen(req)
		t = con.read()
		bs = BeautifulSoup(t)
		ls = bs.pre.text.split('\n') # data_file here
		for l in ls:
			if not l:
				continue
			parts = [s for s in l.split(' ') if s]
			ByContinent._countries.append({ "continent" : parts[0], "country_name" : parts[4].replace(',','') })

	def GET(self, continent_code):
		if len(ByContinent._countries) == 0:
			self.load()
		web.header('Content-Type', 'application/json')
		return json.dumps([c for c in ByContinent._countries if c['continent'] == continent_code or not continent_code])