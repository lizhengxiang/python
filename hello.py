from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
#from flask.exe.wtf import From
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#from flask.exe.moment import Moment
from datetime import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
#moment = Moment(app)
class NameFrom(Form):
	name = StringField('what you name?', validators = [Required()])
	submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameFrom()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form = form, name = name)
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
@app.errorhandler(500)
def internal_serve_error(e):
	return render_template('500.html'), 500
if __name__ == '__main__':
	app.run(debug = True)
