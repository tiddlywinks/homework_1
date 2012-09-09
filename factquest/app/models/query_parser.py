class QueryParser():
	"""the query parser maps from_<property>=x and to_<property>=y as x < country.property < y
	count_<propety> will map to len()"""
	def parse(self, ps):
		def predicate(t):
			for p in ps:
				print t +' ' + p + ': ' + str(ps[p])
		predicate('hello')