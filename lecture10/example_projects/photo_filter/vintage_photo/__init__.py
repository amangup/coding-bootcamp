import os

from flask import Flask
from instagram_filters import image_filters

UPLOAD_FOLDER = 'E:\\uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-hard-password'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

filters = [(image_filters.cross_process, "cross_process", "Cross Processed"),
           (image_filters.aged_photo, "aged_photo", "Aged Photo"),
           (image_filters.vivid, "vivid", "Vivid"),
           (image_filters.bw_punch, "bw_punch", "Black & White Punch"),
           (image_filters.vignette, "vignette", "Vignette")]


def get_save_folder(hash_id):
    return os.path.join(app.config['UPLOAD_FOLDER'], hash_id)


def get_original_image_path(hash_id, image_type):
    return os.path.join(get_save_folder(hash_id), "original." + image_type)

from vintage_photo import file_upload, apply_filter, show_image, slideshow