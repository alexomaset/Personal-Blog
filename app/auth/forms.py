from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtfforms.validators import DataRequired, Length, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequire(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password' validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()


class LoginForm(FlaskForm): 
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('password' validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
