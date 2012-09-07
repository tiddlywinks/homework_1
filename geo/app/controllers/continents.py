import json
import web

class List:
	"""Obtains list of continents"""
	_continents = [{ 'code' : 'AF', 'name' : 'Africa' },
				{ 'code' : 'AS', 'name' : 'Asia' }, 
				{ 'code' : 'EU', 'name' : 'Europe' },
				{ 'code' : 'NA', 'name' : 'North America' },
				{ 'code' : 'SA', 'name' : 'South America' },
				{ 'code' : 'OC', 'name' : 'Oceania' },
				{ 'code' : 'AN', 'name' : 'Antarctica' }]
	def GET(self):
		web.header('Content-Type', 'application/json')
		return json.dumps(List._continents)