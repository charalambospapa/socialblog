from myapp import app
@app.route('/')
@app.route('/index')
def index():
	return 'All good!'