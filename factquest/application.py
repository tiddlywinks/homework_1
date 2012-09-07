import web
import app.controllers

Urls = ('/continents/', 'app.controllers.continents.List',
		'/countries/(|AF|AS|EU|NA|SA|OC|AN)', 'app.controllers.countries.ByContinent')

view = web.template.render('views', globals=globals)
web.config.debug = True
app = web.application(Urls, globals())
	
if __name__ == "__main__":	
	app.run()