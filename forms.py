from flask_wtf import Form, RecaptchaField
from wtforms import  *

class RegisterForm(Form):   
    name = StringField('Nombre', 
        [
            validators.DataRequired(), 
            validators.length(max=5, message='Maximo 50 caracteres')
        ])
    password = PasswordField('Nueva contraseña', 
        [
            validators.DataRequired(),
            validators.length(min=8, message='Contraseña minimo de 8 caracteres')
        ])
    email = EmailField('Correo electronico', 
        [  
            validators.DataRequired(), 
            validators.length(min=6, max=35, message='Correo minimo de 6 caracteres y maximo de 35')
        ])
        
    recaptcha = RecaptchaField()