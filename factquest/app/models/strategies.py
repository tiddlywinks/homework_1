from bs4 import BeautifulSoup
from utils import curry
from scipy.cluster.hierarchy import linkage, fcluster
from collections import Counter
import re

"""these are strategies (algorithms determined at runtime)"""
## i.e. https://www.cia.gov/library/publications/the-world-factbook/geos/aa.html

# gets the data associated with a category; category is distinct text in category header
def category(html, category):
	soup = BeautifulSoup(html, 'html5lib')
	anchor = soup.find("a", { "alt" : re.compile(".*%s.*" % category, re.IGNORECASE) })
	if not anchor:
		return None
	category_data = anchor.find_next('div', {'class' : 'category_data'})
	if not category_data:
		return None
	return category_data.text
	
def country(html):
	soup = BeautifulSoup(html, 'html5lib')
	span = soup.find('span', { 'class' : 'region_name1' })
	if span:
		return span.text
	return None

# gets the political party text
political_party = curry(category, category='political parties')

# gets the number of political parties
def political_party_count(html):
	text = political_party(html=html)
	if not text:
		return None
	return len(text.split(';'))-1

def political_party_count_gt_n(html, n):
	return political_party_count(html) > int(n) # bugfix: must ensure serialized to int

# true if natural hazards section contains hazard word
def natural_hazard(html, hazard):
	hazards_data = category(html, 'hazard')
	if not hazards_data:
		return None
	return hazard.lower() in hazards_data.lower()

def flag_contains_color(html, color):
	flag_data = category(html, 'flag')
	if not flag_data:
		return None
	return color.lower() in flag_data.lower()

# True if location mentions enclave
# TODO toss dummy param after fix Query to allow no params
def enclave(html, dummy_param):
	location = category(html, 'Location')
	if not location:
		return None
	return 'enclave' in location.lower()
	
def convert_coords(ll):
	lat_frag, long_frag = map(lambda s: s.strip(), ll.split(','))
	lat_mul = -1.0 if lat_frag[len(lat_frag)-1].lower() == 's' else 1.0
	lon_mul = -1.0 if long_frag[len(long_frag)-1].lower() == 'w' else 1.0
	lat = float('.'.join(lat_frag.split(' ')[0:2])) * lat_mul
	lon = float('.'.join(long_frag.split(' ')[0:2])) * lon_mul
	return lat, lon
	
def _capital_coordinates(html, dummy_param):
	soup = BeautifulSoup(html, 'html5lib')
	anchor = soup.find("a", { "alt" : re.compile(".*Definitions and Notes: Capital.*", re.IGNORECASE) })
	try:
		td = anchor.find_next('tr').find('td')
		divs = td.find_all('div')
		country_name = country(html)
		capital_name = divs[0].find('span').text
		ll = divs[1].find('span').text
		coords = convert_coords(ll)
		return { 'capital' : capital_name, 'country' : country_name, 'coordinates' : { 'latitude' : coords[0], 'longitude' : coords[1] } }
	except Exception, e:
		return None

def capital_coordinates(htmls, n):
	capitals_coords = []
	for html in htmls:
		r = _capital_coordinates(html, n)
		if r:
			capitals_coords.append(r)
	coords = [(capital_coord['coordinates']['latitude'], capital_coord['coordinates']['longitude'])  for capital_coord in capitals_coords]
	# flat cluster using farthest-neighbor cluster distance method
	z = linkage(coords, method='complete') 
	clusters = fcluster(z, t=float(n), criterion='distance')
	# which cluster has the most items in it?
	counter = Counter(clusters) 
	selected_cluster = counter.most_common(1)[0][0]
	result = []
	for i in range(0, len(capitals_coords)-1):
		if clusters[i] == selected_cluster:
			result.append(capitals_coords[i]) # { 'capital' : capital_name, 'country' : country_name, 'coordinates' : { 'latitude' : coords[0], 'longitude' : coords[1] } }
	return result
capital_coordinates.all_pages = True