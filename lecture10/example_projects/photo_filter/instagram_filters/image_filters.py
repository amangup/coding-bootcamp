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
        image.modulate(brightness=100, saturation=150, hue=100)
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
