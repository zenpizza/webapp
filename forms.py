from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CalcForm(FlaskForm):
    x = IntegerField("X", validators=[DataRequired()])
    y = IntegerField('Y', validators=[DataRequired()])
    submit = SubmitField('cLacuLate')