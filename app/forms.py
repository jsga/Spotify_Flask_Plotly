from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    tokenID = StringField('Paste your token here', validators=[DataRequired()])
    submit = SubmitField('Gather data')