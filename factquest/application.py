import web
import app.controllers

Urls = ('/countries/.*', 'app.controllers.query_countries.QueryCountries')

view = web.template.render('views', globals=globals)
web.config.debug = True
app = web.application(Urls, globals())
	
if __name__ == "__main__":	
	app.run()