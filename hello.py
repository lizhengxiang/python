from flask import Flask, render_template, session, url_for, redirect, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.wtf import Form
from flask.ext.mail import Mail
from flask.ext.script import Shell
from wtforms import StringField, SubmitField
from wtforms.validators import Required
#from flask.exe.moment import Moment
from datetime import datetime
import multiprocessing
from NameForm import NameForm

#from flaskext.sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
mail = Mail(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'
#moment = Moment(app)

#Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

def make_shell_context():
	return dict(app = app, db = db, User = User, Role = Role)
#manager.add_command("shell", Shell(make_context=make_shell_context))
#define Role and User
class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(64), unique = True)
	users = db.relationship('User', backref = 'role')
	def __repr__(self):
		return '<Role %r> % self.name'
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique = True, index = True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	@property
	def password(self):
		return AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User %r> % self.username'

class NameFrom(Form):
	name = StringField('what you name?', validators = [Required()])
	submit = SubmitField('Submit')
app.config['MAIL_SEVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

#form = NameFrom(Form)

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.name.data).first()
		if user is None:
			user = User(username = form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
		session['name'] = form.name.data
		form.name.data = ''
		old_name = session.get('name')
  		if old_name is not None and old_name != form.name.data:
 			flash('Looks link you have changed you name!')
		return redirect(url_for('index'))
	return render_template('index.html', form = form, name = session.get('name'), known = session.get('known', False))
		#old_name = session.get('name')
		#if old_name is not None and old_name != form.name.data:
		#	flash('Looks link you have changed you name!')
		#session['name'] = form.name.data
		#return redirect(url_for('index'))
	#return render_template('index.html', form = form, name = session.get('name'))
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
