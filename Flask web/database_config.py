import config
import os
from flask.ext.sqlalchemy import SQLAlchemy
#Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
config.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
config.app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(config.app)

