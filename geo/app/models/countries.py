import urllib2
from bs4 import BeautifulSoup
import appendix_strategies
import re

class Countries:
	_continents_url = "http://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
	_appendix_url = "https://www.cia.gov/library/publications/the-world-factbook/appendix/appendix-d.html"
	_countries = []
	
	@staticmethod
	def load():
		# wikipedia blocks bots, the next 2 lines were borrowed from
		# http://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page
		req = urllib2.Request(Countries._continents_url, headers={'User-Agent' : "Magic Browser"})
		con = urllib2.urlopen(req)
		t = con.read()
		bs = BeautifulSoup(t)
		ls = bs.pre.text.split('\n') # data_file here
		countries = []
		for l in ls:
			if not l:
				continue
			parts = [s for s in l.split(' ') if s]
			name = ' '.join(parts[4:]).replace(',','')
			countries.append({ "continent" : parts[0], "country_name" : name })
		# BUG countries with multiple words may not parse correctly
		req = urllib2.Request(Countries._appendix_url, headers={'User-Agent' : "Magic Browser"})
		con = urllib2.urlopen(req)
		html = con.read()
		name_fips = appendix_strategies.get_fips_10(html)
		for country in countries:
			def clean_name(s):
				m = re.sub(' (\(|democratic republic of the|republic of the|rupublic of).*', '', s.lower())
				m = re.sub(', .*', '', m)
				return m.strip()
			def wordsMatchThreshold(n, s, ws):
				contained = 0
				for w in ws:
					if w in s:
						contained = contained + 1
				return contained/float(len(ws)) >= n
			matches = [name_fip['fips'] for name_fip in name_fips if clean_name(name_fip['name']) in country['country_name'].lower()]
#			if not len(matches):
#				print 'no match for "' + country['country_name'] + '"'
			country['code'] = matches[0] if len(matches) else None
		Countries._countries = countries

	@staticmethod
	def find(predicate):
		if len(Countries._countries) == 0: # TODO check memcache
			Countries.load()
		return [country for country in Countries._countries if predicate(country)]