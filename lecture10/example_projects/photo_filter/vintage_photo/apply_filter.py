import os

from flask import url_for, redirect

from vintage_photo import app, get_save_folder, get_original_image_path, filters
from instagram_filters.image_filters import *


@app.route('/filter/<image_type>/<hash_id>')
def image_filter(image_type, hash_id):
    file_folder = get_save_folder(hash_id)
    original_filepath = get_original_image_path(hash_id, image_type)

    for filter_func, filename, _ in filters:
        filtered_image_path = os.path.join(file_folder, filename + "." +
                                           image_type)
        filter_func(original_filepath, filtered_image_path)

    return redirect(url_for('slideshow', image_type=image_type,
                            hash_id=hash_id))
