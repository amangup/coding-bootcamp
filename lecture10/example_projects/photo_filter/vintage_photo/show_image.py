import os

from flask import send_from_directory

from vintage_photo import app, get_save_folder

@app.route('/show_image/<hash_id>/<filename>')
def show_image(hash_id, filename):
    return send_from_directory(get_save_folder(hash_id), filename)
