from flask import Flask, render_template, session, url_for, redirect, flash
from flask.ext.bootstrap import Bootstrap
#from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.wtf import Form
from flask.ext.mail import Mail
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#from flask.exe.moment import Moment
from datetime import datetime
#from flaskext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
mail = Mail(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
#moment = Moment(app)
class NameFrom(Form):
	name = StringField('what you name?', validators = [Required()])
	submit = SubmitField('Submit')
app.config['MAIL_SEVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameFrom()
	if form.validate_on_submit():
		old_name = session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('Looks link you have changed you name!')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', form = form, name = session.get('name'))
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
