from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    tokenID = StringField('And then paste it here', validators=[DataRequired()])
    submit = SubmitField('Gather data!')