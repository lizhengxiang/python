from flask import render_template
from . import main

#define 404 not page found
@main.app_errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#define 505 internal sever error
@main.app_errorhandler
def internal_sever_error(e):
	return render_template('505.html'), 505
	
