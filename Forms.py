from flask_wtf import Form
from wtforms import SelectField,BooleanField


class info(Form):
    idade = SelectField('Idades', choices=[('25', 'Novo'), ('50', 'Jovem'), ('90', 'Velho')])
    cidade = SelectField('cidade', choices=[('01', 'Sao Jose Dos campos'), ('02', 'Caçapava'), ('03', 'Jacarei')])
    sexo = SelectField('sexo', choices=[('H', 'H'), ('F', 'M')])
    tipo = SelectField('tipo', choices=[('H', 'H'), ('F', 'M')])
    situacao_cidade = BooleanField('situacao_cidade')