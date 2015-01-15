import web

urls = (
	'/hello_form', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index:
	def GET(self):
		form = web.input(name="Nobody")
		greeting = "Hello %s" % form.name
		return render.index(greeting = greeting)
		
if __name__ == "__main__":
	app.run()