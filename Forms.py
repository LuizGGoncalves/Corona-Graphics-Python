from flask_wtf import Form
from wtforms import IntegerField,StringField,SelectField
from wtforms.validators import DataRequired

class info(Form):
    idade = SelectField('Idades', choices=[('25', 'Novo'), ('50', 'Jovem'), ('90', 'Velho')])
    cidade = SelectField('cidade', choices=[('01', 'Sao Jose Dos campos'), ('02', 'Caçapava'), ('03', 'Jacarei')])
    sexo = SelectField('sexo', choices=[('H', 'H'), ('F', 'M')])
    tipo = SelectField('tipo', choices=[('H', 'H'), ('F', 'M')])