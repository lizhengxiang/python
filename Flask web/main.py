from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

#define base moldboard
bootstrpa = Bootstrap(app)

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_serve_error(e):
	return render_template('500.html'), 500

#define login 
@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(debug = True)
