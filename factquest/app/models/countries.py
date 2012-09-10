import os
import sys
sys.path.append(os.path.abspath('../..'))
import urllib2
import json
from config import geo_url, debug

class Countries:
	
	@staticmethod
	def byContinent(continent):
		if debug:
			# PROXY is blocking localhost
			from ..tests.test_utils import get_countries
			return get_countries(continent)
		# get countries
		url = "%s/countries/%s" % (geo_url, continent)
		opener = urllib2.build_opener()
		opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')]
		response = opener.open(url)
		r = response.read()
		countries = json.loads(r)
		return countries