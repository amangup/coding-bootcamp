from flask import render_template, url_for

from vintage_photo import app, get_save_folder, get_original_image_path, filters

class ImageDetails:
    def __init__(self, url, caption):
        self.url = url
        self.caption = caption


@app.route('/slideshow/<image_type>/<hash_id>')
def slideshow(image_type, hash_id):
    slideshow_images = [ImageDetails(
        url_for('show_image', hash_id=hash_id,
                filename="original." + image_type), "Original picture")]
    for _, filename, caption in filters:
        slideshow_images.append(ImageDetails(
            url_for('show_image', hash_id=hash_id,
                    filename=filename + "." + image_type), caption
        ))

    return render_template('slideshow.html', slideshow=slideshow_images)
