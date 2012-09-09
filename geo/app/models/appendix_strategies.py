import urllib2
from bs4 import BeautifulSoup

## == entities and codes strategies
## i.e. https://www.cia.gov/library/publications/the-world-factbook/appendix/appendix-d.html
def get_fips_10(html):
	countries = []
	url = 'https://www.cia.gov/library/publications/the-world-factbook/appendix/appendix-d.html'
	req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
	r = urllib2.urlopen(req)
	html = r.read()
	soup = BeautifulSoup(html)
	bs = soup.findAll('table',cellpadding=1, cellspacing=1)
	for b in bs:
		country_rows = b.tbody.findAll('tr', recursive=False)
		for country_row in country_rows:
			cols = country_row.findAll('td', recursive=False)
			if len(cols) < 2:
				continue
			name = cols[0].text.strip()
			code = cols[1].text.strip()
			countries.append({ "name" : name, "fips" : code })
	return countries