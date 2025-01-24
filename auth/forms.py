from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[
        DataRequired(message='El nombre de usuario es obligatorio'),
        Length(min=4, max=64, message='El nombre debe tener entre 4 y 64 caracteres')
    ])
    email = StringField('Correo electrónico', validators=[
        DataRequired(message='El correo electrónico es obligatorio'),
        Email(message='Por favor ingresa un correo electrónico válido')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es obligatoria'),
        Length(min=6, message='La contraseña debe tener al menos 6 caracteres')
    ])
    confirm_password = PasswordField('Confirmar contraseña', validators=[
        DataRequired(message='Por favor confirma tu contraseña'),
        EqualTo('password', message='Las contraseñas deben coincidir')
    ])
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[
        DataRequired(message='El correo electrónico es obligatorio'),
        Email(message='Por favor ingresa un correo electrónico válido')
    ])
    password = PasswordField('Contraseña', validators=[
        DataRequired(message='La contraseña es obligatoria')
    ])
    submit = SubmitField('Ingresar')
