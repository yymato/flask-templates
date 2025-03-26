from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astronaut= StringField('id Астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль Астронавта', validators=[DataRequired()])
    id_captain = StringField('id Капитана', validators=[DataRequired()])
    password_captain = PasswordField('Пароль Капитана', validators=[DataRequired()])
    submit = SubmitField('Войти')