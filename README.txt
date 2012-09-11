In addition to the source code (and the se.txt file), you should also submit a text file titled readme.txt, 
which should contain a short write-up about your software. How to run your program, any problems you experienced, etc. 
Think of the readme as a combination of instructions for the user and a chance for you to get partial credit.

FactQuest 0.01
==============
This a web.py project that provides answers to questions regarding 
data provided by the CIA's World Factbook website 
(https://www.cia.gov/library/publications/the-world-factbook/).

- The project consists of two MVC web applications:
   - /factquest - The main application; consists of a simple web interface.
				  This also exposes a REST interface so that other types 
				  of clients can use the application.
   - /geo       - a simple REST service that gets data regarding continents 
                  and countries.

Dependencies
------------
FactQuest depends on the following to run:
 Python 2.7+      - download from http://www.python.org/getit/releases/2.7/
 web.py           - easy_install web.py
 Beautiful Soup 4 - easy_install bs4
 html5lib         - easy_install html5lib
 Any javascript-enabled browser
 
Testing
-------
For testing you will need
 paste - easy_install paste
 nose  - easy_install nose
 
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
 GET http://localhost:1235/countries/?within_degrees=10