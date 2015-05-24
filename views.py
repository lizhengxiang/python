from flask import render_template, flash, redirect, url_for
from . import main
from .forms import EditprofileForm
from ..models import User
from flask.ext.login import current_user, login_required
from app import  db
#from ..decorators import admin_required

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
@login_required
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


@main.route('/edit-profiel/<int:id>', methods=['GET', 'POST'])
@login_required
#@admin_required
def edit_profile():
	user = User.query.get_or_404(id)	
	form = EditprofileAdminForm(user = user)
	if form.validate_on_submit():
		user.email = form.email.data
		user.username = form.username.data
		user.confirmed = form.confirmed.data
		user.role = Role.query.get(form.role.data)
		user.name = form.name.data
		user.location = form.location.data
		user.about_me = form.about_me.data
		db.session.add(user)
		flash('The profile has been updated')
		return redirect('.user', username = user.username)
	form.email.data = user.email
	form.username.data = user.username.data
	form.confirmed.data = user.confirmed
	form.role.data = user.role_id
	form.name.data = user.name
	form.location.data = user.location
	form.about_me.data = user.about_me
	return render_template('edit_profile.html', form = form, user = user)