FactQuest 0.01
==============
This a web.py project that provides answers to questions regarding 
data provided by the CIA's World Factbook website 
(https://www.cia.gov/library/publications/the-world-factbook/).

- The project consists of two MVC web applications:
   - /factquest - The main application; consists of a simple web interface (http://localhost:1235/query_ui/).*
				  This also exposes a REST interface so that other types of clients can use the application.
   - /geo       - a simple REST service that gets data regarding continents 
                  and countries by cross-referencing a wikipedia article** and the CIA Factbook Appendix D.***
				  
*    An example output is available in factquest/static/example_response.htm which illustrates the functionality
     if you are unwilling to setup and run the web applications.
**   http://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)
***  https://www.cia.gov/library/publications/the-world-factbook/appendix/appendix-d.html

Questions FactQuest Answers
===========================
Here I describe the approaches that were taken to answer the questions.

1. List countries in <continent> that are prone to <natural_hazard>.
FactQuest gets the list of countries in the specified continent by requesting it from the geo service.
A crawler with a specified delay time (to prevent being blacklisted as a bot) obtains the list of pages
associated with each country in the CIA Factbook. A strategy method (predicate) that is mapped to the specified 
query is inferred and mapped onto the set of pages with the natural hazard of interest. The category data 
for natural hazards is found by parsing and finding distinct patterns in the html files. If the text
describing the hazard is found the predicate is satisfied. The service returns the countries associated
with the pages that satisfied the predicate.

2. List countries in <continent> with more than <n> political parties.
The approach is similar to that mentioned in 1. The predicate is more complex however. The composite pattern
is used to divide the task in to stages. The first task is to extract the category data, then to
count the number of political parties described in it (based on the number of semicolons in the section)
and then to compare this to the number supplied in the query.

3. Find all countries that have the color <color> in their flag.
The approach is similar to that mentioned in 1 except that the category data is flag.

4. There are certain countries that are entirely landlocked by a single country. Find these countries.
The approach is similar to that mentioned in 1 except that the category data is in the geography::location
section of the country page. Countries landlocked by a single country are called "enclaves;" the text
"enclave" is currently present in all enclave countries. If FactQuest finds this, the predicate is satisfied
and the country is returned.

5. Capitals that are within <n> degrees of latitude and longitude of each other. Find the lat/long coordinates 
and the list of countries/capitals so that the number of capitals is maximized.
A list of every country is obtained from the geo service. The capital latitude and longitude is extracted from 
the "Definitions and Notes: Capital" section of the CIA Factbook of each page and parsed. Once the list of 
capitals and their coordinate pairs are obtained, they are clustered using the Euclidean distance metric and
with the farthest-neighbor method with the aide of the scipy library. The specified parameter is used as a 
threshold to break up the clusters. The first largest cluster is the one that is selected.

Issues
======
* The geo service has a bug that causes countries whose name consists of multiple words to not parse correctly.
  I used some text processing to reduce the problem, but 10 countries do not parse properly.
  
 * Question number 5 will generate duplicates for Saint Barthelemy

Dependencies
------------
FactQuest depends on the following to run:
 Python 2.7+      - download from http://www.python.org/getit/releases/2.7/
 web.py           - easy_install web.py
 Beautiful Soup 4 - easy_install bs4
 html5lib         - easy_install html5lib
 scipy			  - download from http://www.scipy.org/Download
 Any javascript-enabled browser
 
Testing
-------
For testing you will need
 paste - easy_install paste
 nose  - easy_install nose
Tests can be run with
	factquest/app/tests/all_tests.py
	geo/app/tests/all_tests.py
 
Running
-------
This application has only been tested in a Windows environment.
Once the dependencies are installed, execute run_webs.bat. This will deploy both
web applications. By default:

geo runs at http://localhost:1234/
factquest runs at http://localhost:1235/

The user interface is accessible at http://localhost:1235/query_ui/.

Geo REST service
================
Here I describe the methods exposed by the geo REST service.

GET countries/ - Returns the list of countries
----------------------------------------------

Example: Return countries in South America 
REQUEST       
	GET http://localhost:1234/countries/SA 
RESPONSE 
[
   {
      "country_name":"Argentina Argentine Republic", // name
      "code":"AR",									 // FIPS code which is heavily used by the World FactBook website
      "continent":"SA"								 // continent code
   }, ...,
   {
      "country_name":"Venezuela Bolivarian Republic of",
      "code":"VE",
      "continent":"SA"
   }
]

GET continents/ - Returns the list of continents
------------------------------------------------

Example: Return all continents
REQUEST
	GET http://localhost:1234/continents/
RESPONSE
[
   {
      "code":"AF",		// code
      "name":"Africa"	// name
   }, ...,
   {
      "code":"AN",
      "name":"Antarctica"
   }
]


Factquest REST service
======================
Here I describe the methods exposed by the Factquest REST service.

GET countries/ - Returns the list of countries that match a specified query
---------------------------------------------------------------------------

Example 1: Return countries in Asia that are prone to earthquakes
 GET http://localhost:1235/countries/?continent=as&natural_hazard=earthquake

Example 2: Return countries in Africa with more than 10 political parties
 GET http://localhost:1235/countries/?continent=af&political_party_count_gt_n=10
 
Example 3: Return countries that have the color red in their flag
 GET http://localhost:1235/countries/?flag_contains_color=red

Example 4: Return countries that are entirely landlocked by a single country.
 GET http://localhost:1235/countries/?enclave=1

Example 5: Return countries whose capitals are within 10 degrees of latitude and longitude of eachother
 GET http://localhost:1235/countries/?capital_coordinates=10