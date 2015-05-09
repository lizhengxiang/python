from flask import Flask, render_template, session, url_for, redirect, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from flask.ext.mail import Mail
from flask.ext.script import Shell
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from datetime import datetime
import multiprocessing
import os

app = Flask(__name__)
mail = Mail(app)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


def make_shell_context():
	return dict(app = app, db = db, User = User, Role = Role)
#manager.add_command("shell", Shell(make_context=make_shell_context))
#define Role and User
app.config['MAIL_SEVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

