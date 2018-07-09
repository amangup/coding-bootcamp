## Assignment : Photo filters

If you like photos, then this will be a fun assignment for you. We will create a webapp where an user can upload any picture, and the app creates multiple versions of it by applying different image filters (like making it look like an aged photo). The app will display those filtered images in a slideshow to the user.

To implement this, you will need to learn a few more things over what we learned in the lecture:
- How to upload files
- How to apply filters on images
- How to create an image slideshow (includes learning to use `for` statements in HTML templates)
- URL redirection

For someone who is new to building webapps, this one till take a bit of effort and time, so do persevere. Whenever I get stuck, I find that it helps to come back after some time (especially if I've had a sleep in that time). You also have to search on the internet about concepts you don't already know, see examples of how others have done similar stuff and even search for errors you're getting to find explanations of why they're occurring.

### Uploading files

To apply image filters, we will first upload the user's image file, and then apply filters to that image. Flask has a method to do that.

First, we need the form to allow user to select an image from their device. `Flask-WTF` package has a form field type for that:

```python3
from wtforms import FileField


class FileUploadForm(FlaskForm):
    file_path = FileField('File Path')
```

When you render the `file_path` field in the form, it will show a "Browse..." button to the user.

Once you submit the form, the view function receiving that HTTP POST request can access an object which helps you save that file, as shown below:

```python3
if request.method == 'POST':
    # this is a file upload request
    
    # 'file' is an object of type FileStorage defined by Flask
    file = request.files['file_path']
    
    # We are doing some basic checks on the filename before saving it.
    if file and '.' in file.filename:
        extension = get_extension(file.filename)
        
        # We only save files which have an extension referring to an image type
        if allowed_extension(extension):
            # create a variable `filepath` with the location where you're 
            # going to save the file
            file.save(filepath)
```            

Flask's own documentation for file uploads is here: [http://flask.pocoo.org/docs/1.0/patterns/fileuploads/](http://flask.pocoo.org/docs/1.0/patterns/fileuploads/).

### Applying image filters
To implement image filters, we are going to use a third party library called `Wand`. `Wand` is a python library which is a _wrapper_ over the **ImageMagick** library, i.e., it creates Python classes and methods which in turn execute the commands in ImageMagick (as ImageMagick is not implemented in Python). ImageMagick is a well-known library for manipulating images and is available for all platforms (Windows, Mac, Linux).

To install `Wand`, you can follow the same instructions as you did to install `Flask` or `Flask-WTF` (the latest version is 0.4.4). For `Wand` to function, you also need to install ImageMagick separately on your OS. You can follow the instructions here to do that: [http://docs.wand-py.org/en/0.4.4/guide/install.html](http://docs.wand-py.org/en/0.4.4/guide/install.html).

Once installed, we will use the `wand` package's `Image` class to read, manipulate and write image files. You're not required to learn to do that, but if you are interested in creating your own filters, this can be a fun sub-exercise for you. I have created some simple filters implemented in the code listed below - you can study that code, and use the documentation on Wand's website to come up with more (e.g., try to create a filter which adds some text to the middle of an image).

```python3
from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing


def cross_process(image_filename, output_path):
    with Image(filename=image_filename) as image:
        image.contrast_stretch(black_point=0.15, white_point=0.90,
                               channel='red')
        image.contrast_stretch(black_point=0.10, white_point=0.95,
                               channel='green')
        image.save(filename=output_path)


def aged_photo(image_filename, output_path):
    with Image(filename=image_filename) as image:
        tone_image = Image(height=image.height, width=image.width,
                           background=Color('#705a41'))
        image.modulate(brightness=100, saturation=20, hue=100)
        image.composite_channel(channel='all_channels', operator='overlay',
                                image=tone_image, left=0, top=0)

        image.save(filename=output_path)


def vivid(image_filename, output_path):
    with Image(filename=image_filename) as image:
        image.contrast_stretch(black_point=0.05, white_point=0.95,
                               channel='all_channels')
        image.linear_stretch(black_point=0.05, white_point=0.95)
        image.unsharp_mask(radius=1.5, amount=200, threshold=0.2, sigma=0.5)
        image.save(filename=output_path)


def bw_punch(image_filename, output_path):
    with Image(filename=image_filename) as image:
        image.transform_colorspace('gray')
        image.normalize()
        image.contrast_stretch(black_point=0.1, white_point=0.90)
        image.gamma(1.2)
        image.save(filename=output_path)


def vignette(image_filename, output_path):
    with Image(filename=image_filename) as image:
        with Drawing() as draw:
            draw.stroke_color = Color('black')
            draw.stroke_width = 2
            draw.fill_color = Color('white')
            perimeter_point = (image.height + image.width) / 5000
            draw.circle((image.width // 200, image.height // 200),  # Center point
                        (perimeter_point, perimeter_point))  # Perimeter point
            with Image(width=(image.width // 100), height=(image.height // 100),
                       background=Color('black')) as vignette_border:
                draw(vignette_border)
                vignette_border.resize(width=image.width, height=image.height,
                                       filter='hermite', blur=6.0)
                image.composite_channel(channel='all_channels',
                                        operator='multiply',
                                        image=vignette_border,
                                        left=0, top=0)
                image.save(filename=output_path)
```

### Creating a slideshow

For image slideshows, we need some JS and CSS code to make it run. Fortunately, there are numerous such libraries. I have chosen a library called [bxSlider](https://bxslider.com/), as it looked to be one of the simplest to use. It's also mobile friendly, so this app should run well on your phone's browser as well.

It's a good idea to look at one of the examples here to understand how to use it: [https://bxslider.com/examples/image-slideshow-captions/](https://bxslider.com/examples/image-slideshow-captions/). In the example, there is some Javascript that is used to configure bxSlider. In the HTML section, it shows that to create a slideshow, you need an outer `div` tag with `class="bxslider"`, and then inside it you need a `div` tag for each image in the slideshow. Finally the `img` tag for your image should be present inside that `div`.

To create a bunch of internal `div` and `img` tags, you need to use `for` statements functionality in the HTML template system. I have explained this in the [dictionary assignment document](https://github.com/amangup/coding-bootcamp/blob/master/lecture10/assignment_dictionary.md#if-and-for-statements-in-html-templates).

You can configure bxSlider to your liking as it has many configuration parameters. Here is how the `head` section of my template looks like:

```html
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js"></script>
    <script>
        $(document).ready(function(){
            $('.slider').bxSlider({
                mode: 'fade',
                captions: true,
                responsive: true,
                useCss: true,
                touchEnabled: true,
                controls: true,
                keyboardEnabled: true,
                slideWidth: 800,
            });
        });
    </script>
</head>
```

- Note how all the JS and CSS files are just downloaded from the internet instead of being stored as part of our project.

What is the image src that is used in the img tag? To create that, we will use another of Flask's utility functions called `send_from_directory`. Here is an example usage:

```python
from flask import send_from_directory

@app.route('/show_image/<hash_id>/<filename>')
def show_image(hash_id, filename):
    # create filepath variable which points to the image file you want to show
    return send_from_directory(filepath)
```

Then, the image URL can be created as follows:

```python3
url_for('show_image', hash_id=hash_id, filename=image_filename)
```

### URL redirection

This topic has also been discussed in the [dictionary assignment document](https://github.com/amangup/coding-bootcamp/blob/master/lecture10/assignment_dictionary.md#url-redirection).

The use case for this app is similar: When the user sees a slideshow, we want to create an URL which the user can then share. To achieve that, the view function which receives the content of the form will have to redirect to another page which applies image filters and returns the slideshow to the user. 

Here are some more tips on how to do this well for this assignment:

- Save images on a new random folder every time the user uploads one (and the filtered output images). You can generate the folder name using the [python module `secrets`](https://docs.python.org/3/library/secrets.html) (use the `token_urlsafe()` function). This can be used to create a link like `http://myapp.com/slideshow/<random_token>`.
- The process to manipulate images is CPU heavy, and it is wasteful to do that every time the user opens the `slideshow` view. To solve this issue, you can use double redirection: The file upload view redirects to a temporary view `apply_filters` (that applies filters and stores the resulting images), which redirects to the `slideshow` view when it redirects (which just creates a slideshow of existing images). When an user returns to the `slideshow` link later on, the filtered images already exist.


