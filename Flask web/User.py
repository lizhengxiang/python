from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(64), unique = True, index = True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
		
	password_hash = db.Column(db.String(128))
	
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

#test user
u = User()
u.password = 'cat'
print u.password_hash
print u.verify_password('cat')
print u.verify_password('dog')
u2 = User()
u2.password = 'cat'
print u2.password_hash
