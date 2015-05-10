import os
# config database
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECREY_KEY = os.environ.get('SECREY_KEY') or 'hard to guess string'
	#automatic submit database
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True	
	#config email 
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flask Adimn<flasky@example.com>'
	# environment varible
	FLASK_ADMIN = os.environ.get('FLASK_ADMIN')
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	#config Flask-Mail
	MAIL_SEVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	#config database
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingCofig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
	 SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
	'development': DevelopmentConfig,
	'testing': TestingCofig,
	'production':ProductionConfig,

	'default': DevelopmentConfig

}
