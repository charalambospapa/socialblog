from flask import render_template
from myapp import app
@app.route('/')
@app.route('/index')
def index():
	user = {'username':'charalambos'}
	posts = [
		{
			'author': {'username': 'Papa'},
			'body': 'Beautiful day today!'
		},
		{
			'author': {'username': 'Takis'},
			'body': 'Hello everyone!!!!'
		},
	]
	return render_template('index.html', title='Home', user=user, posts=posts)
