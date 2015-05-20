from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp
#from wtforms import ValidationError
#from flask.ext.pagedown.fields import PageDownField
#from ..models import Role, User


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class EditprofileForm(From):
	name = StringField('Real name', validators = [Length(0, 64)])
	location = StringField('Location', validators=[Length(0, 64)])
	about_me = TextAreaFiled('About me')
	submit = SubmitFiled('Submet')

