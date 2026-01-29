from wtforms import Form, StringField
from wtforms import EmailField
from wtforms import validators
from wtforms import IntegerField, PasswordField, FloatField


class UserForm(Form):
    matricula = IntegerField('Matricula', [validators.DataRequired(message="Campo Requerido"),
    validators.NumberRange(min=10, max=100, message="Ingrese valor valido")])
    nombre = StringField('Nombre' ,[validators.DataRequired(message="Campo Requerido"),
    validators.Length(min=2, max=20, message="Ingrese valor valido")])
    apaterno = StringField('Apellido Paterno' ,[validators.DataRequired(message="Campo Requerido")])
    amaterno = StringField('Apellido Materno' ,[validators.DataRequired(message="Campo Requerido")])
    correo = EmailField('Correo', [validators.Email(message='Ingresa un correo valido')])
