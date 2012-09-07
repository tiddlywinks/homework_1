from os import path
import config

class Request():
	def __init__(self, url, headers):
		self.url = url
		self.filename = path.basename(url)
		self.headers = headers

def urlopen(request):
	return open(config.base_dir + 'app\\resources\\' + request.filename, 'r')