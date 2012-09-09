from bs4 import BeautifulSoup
from utils import curry

"""these are strategies (algorithms determined at runtime)"""
## i.e. https://www.cia.gov/library/publications/the-world-factbook/geos/aa.html

# gets the data associated with a category; category is distinct text in category header
def get_category(html, category):
	soup = BeautifulSoup(html)
	anchor = soup.find("a", { "alt" : re.compile(".+%s.+" % category) })
	return anchor.findNext('div', {'class' : 'category_data'}).text

# gets the political party text
strategy_political_party = curry(strategy_get_category, category='political party')

# gets the number of political parties
def strategy_political_party_count(html):
	text = strategy_political_party(html=html)
	return len(text.split(';'))-1
