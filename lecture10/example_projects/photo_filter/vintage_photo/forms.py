from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class FileUploadForm(FlaskForm):
    file_path = FileField('File Path')
    upload = SubmitField('Upload file')
