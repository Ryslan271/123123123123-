from datetime import date
import datetime

import sqlalchemy as sa
from flask_wtf import FlaskForm
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    city = StringField('Город', validators=[DataRequired()])
    mail = StringField('Эл. Почта', validators=[DataRequired()])
    phone = StringField('Телефон', validators=[DataRequired()])
    msg = StringField('Сообщение', validators=[DataRequired()])
    submit = SubmitField('Отправить заявку')
