import os
from flask import render_template, url_for

from vintage_photo import app, get_original_image_path, filters

class ImageDetails:
    def __init__(self, url, caption):
        self.url = url
        self.caption = caption


@app.route('/slideshow/<image_type>/<hash_id>')
def slideshow(image_type, hash_id):
    # first check if this slideshow exists:
    original_image_path = get_original_image_path(hash_id, image_type)
    if not os.path.isfile(original_image_path):
        return render_template('slideshow_not_found.html'), 404

    slideshow_images = [ImageDetails(
        url_for('show_image', hash_id=hash_id,
                filename="original." + image_type), "Original picture")]
    for _, filename, caption in filters:
        slideshow_images.append(ImageDetails(
            url_for('show_image', hash_id=hash_id,
                    filename=filename + "." + image_type), caption
        ))

    return render_template('slideshow.html', slideshow=slideshow_images)
