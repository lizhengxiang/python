from flask import render_template, flash, redirect, url_for
from . import main
from .forms import EditprofileForm
from ..models import User
from flask.ext.login import current_user
from app import  db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username = username).first()
	if user is None:
		abort(404)
	return render_template('user.html', user = user)

@main.route('/edit-profiel', methods=['GET', 'POST'])
#@login_required
def edit_profile():
	form = EditprofileForm()
	if form.validate_on_submit():
		current_user.name = form.name.data
		current_user.location = form.location.data
		current_user.about_me = form.about_me.data
		db.session.add(current_user)
		flash('Your profile has been update.')
		return redirect(url_for('.user', username = current_user.username))
	form.name.data = current_user.name
	form.location.data = current_user.location
	form.about_me.data = current_user. about_me
	return render_template('edit_profile.html', form=form)
