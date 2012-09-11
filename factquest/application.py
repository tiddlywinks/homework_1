import web
import app.controllers

Urls = ('/countries/.*', 'app.controllers.query_countries.QueryCountries',
	    '/query_ui/(.*)', 'app.controllers.query_ui.QueryUI')

view = web.template.render('views', globals=globals)
web.config.debug = True
app = web.application(Urls, globals())
	
if __name__ == "__main__":	
	app.run()