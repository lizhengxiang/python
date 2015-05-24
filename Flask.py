from flask import Flask, url_for
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#@app.route('/user/<username>')
#def show_user_profile(username):
	#show the user profile for that user
#	return 'User %s' % username
#@app.route('/post/<int:post_id>')
#def show_post(post_id):
#	return 'Post %d'% post_id
#@app.route('/projects/')
#def projects():
#	return 'the projects page'
#@app.route('/about')
#def about():
#	return 'the about page'
#@app.route('/')
#def index():
#	return 'Index Page'
#@app.route('/hello')
#def hello_world():
#	return 'Hello world!'

#@app.route('/login')
#def login():pass
#@app.route('/user/<username>')
#def profile(username):pass
#with app.test_request_context():
	#print url_for('.index')
#	print url_for('login')
#	print url_for('login', next = '/')
#	print url_for('profile', username = 'john Doe')
#@app.route('/login', methods = ['GET', 'POST'])
#def login():
#	if request.method == 'POST':
#		do_the_login()
#	else:
#		show_the_login_from()
if __name__ == '__main__':
	#app.debug = True
	app.run()

