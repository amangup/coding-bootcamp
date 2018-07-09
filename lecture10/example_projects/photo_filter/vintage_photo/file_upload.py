import os
import secrets
from flask import render_template, request, redirect, url_for

from vintage_photo import app, forms, get_save_folder, get_original_image_path


def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def allowed_extension(extension):
    return extension in app.config['ALLOWED_EXTENSIONS']


@app.route('/',  methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        # this is a file upload request
        file = request.files['file_path']
        if file and '.' in file.filename:
            extension = get_extension(file.filename)
            if allowed_extension(extension):
                hash_id = secrets.token_urlsafe(8)

                save_folder = get_save_folder(hash_id)
                os.mkdir(save_folder)

                filepath = get_original_image_path(hash_id, extension)
                file.save(filepath)

                return redirect(url_for('image_filter', image_type=extension,
                                        hash_id=hash_id))
    else:
        form = forms.FileUploadForm()
        return render_template('file_upload.html', form=form)
