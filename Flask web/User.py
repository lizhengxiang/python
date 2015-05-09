from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
import os
from flask import Flask
app = Flask(__name__)

db = SQLAlchemy()
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
	
	def __repr__(self):
		return '<User %r> % self.username'

#test user
####################################################
#u = User()
#u.password = 'cat'
#print u.password_hash
#print u.verify_password('cat')
#print u.verify_password('dog')
#u2 = User()
#u2.password = 'cat'
#print u2.password_hash
