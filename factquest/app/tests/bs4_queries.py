# figuring out how to navigate the cia country pages to get the category data
# this test only runs if the working dir is tests folder and a file exists named input.htm
from bs4 import BeautifulSoup
import re

def extract_category(category):
	soup = BeautifulSoup(open("input.htm"))
	anchor = soup.find("a", { "alt" : re.compile('.+%s.+' % category, re.IGNORECASE)})
	return anchor.findNext('div', {'class' : 'category_data'}).text

if __name__ == '__main__':
	extract_category('flag')