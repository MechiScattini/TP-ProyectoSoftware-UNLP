from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ImportForm(FlaskForm):
    file = FileField('Buscar archivo', validators=[
        FileRequired(),
        FileAllowed(['csv'], 'Por favor, seleccione un archivo .csv')
    ])