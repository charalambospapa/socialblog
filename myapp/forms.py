from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),Length(min=4)]) #first arguments is a label, the second is a LIST of validators (don't forget () ) 
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')
