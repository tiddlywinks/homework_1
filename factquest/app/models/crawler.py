import urllib2
import time

class Crawler:
	def __init__(self, urls, delay_seconds=1):
		self.urls = urls
		self.delay_seconds = delay_seconds
	def crawl(self):
		responses = []
		last_response = 0
		for url in self.urls:
			now = time.clock()
			while now - last_response < self.delay_seconds:
				now = time.clock()
			# wikipedia blocks bots, the next 2 lines were borrowed from
			# http://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page
			req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
			con = None
			try:
				con = urllib2.urlopen(req)
				t = con.read()
				responses.append({ 'url' : url, 'response' : t })
			except Exception, e:
				responses.append({ 'url' : url, 'response' : None, 'error' : str(e) })
		return responses