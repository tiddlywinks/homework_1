from bs4 import BeautifulSoup
from utils import curry
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