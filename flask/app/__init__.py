from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__)
	#app.config.from_obgect(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)

	from app.main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	# addition  route and define page error
	return app
