from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    tokenID = StringField('tokenID', validators=[DataRequired()])
    limit = StringField('Limit', validators=[DataRequired()])
    offset = StringField('Offset', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')