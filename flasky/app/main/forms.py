from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import Required, Length, Email, Regexp
#from wtforms import ValidationError
#from flask.ext.pagedown.fields import PageDownField
#from ..models import Role, User


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class EditprofileForm(Form):
	name = StringField('Real name', validators = [Length(0, 64)])
	location = StringField('Location', validators=[Length(0, 64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')

class EditprofileAdminFrom(Form):
	email = StringField('Email', validators = [Required(), Length(0, 64), Email()])
	username = StringField('Username', validators = [Required(), Length(0, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 
			'Username must have only,number, dots or unedrscores')])
	confirmed = BooleanField('Confirmed')
	role = SelectField('Role', coerce = int)
	name = StringField('Role Name', validators = [Length(0, 64)])	
	location = StringField('Location', validators = [Length(0, 64)])
	about_me = TextAreaField('About me')
	submit = SubmitField('Submit')
	
	def __init__(self, user, *args, **kwargs):
		super(EditprofileAdminFrom, self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name)
								for role in Role.order_by(Role.name).all()]
		self.user = user
	def validate_email(self, field):
		if field.data != self.user.email and \
				User.query.filter_by(email = field.data).first():
			raise ValidationError('Email already register.')
	
	def validate_username(self, field):
		if field.data != self.user.username and \
				User.query.filter_by(username = field.data).first():
			raise ValidationError('Username already register.')
