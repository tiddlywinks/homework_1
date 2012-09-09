import os
import sys
sys.path.append(os.path.abspath('../..'))
import urllib2
import json
from config import geo_url

class Countries:
	
	@staticmethod
	def byContinent(continent):
		# get countries
		url = "%s/countries/%s" % (geo_url, continent)
		response = urllib2.urlopen(url)
		r = response.read()
		countries = json.loads(r)
		return countries