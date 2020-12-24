from io import BytesIO
from django.core.files import File
from PIL import Image
import os

def make_thumbnail(image, size=(1000, 800),name=None):
    """Makes thumbnails of given size from given image"""
    im = Image.open(image)
    im.thumbnail(size, Image.ANTIALIAS)

    thumb_name, thumb_extension = os.path.splitext(image.name)
    thumb_filename = thumb_name + '_thumb' + thumb_extension
    thumb_extension = thumb_extension.lower()

    if thumb_extension in ['.jpg', '.jpeg']:
        FTYPE = 'JPEG'
    elif thumb_extension == '.gif':
        FTYPE = 'GIF'
    elif thumb_extension == '.png':
        FTYPE = 'PNG'
    else:
        return False

    # im.convert('RGB') # convert mode
    # im.thumbnail(size) # resize image
    thumb_io = BytesIO() # create a BytesIO object
    im.save(thumb_io, FTYPE) # save image to BytesIO object
    thumbnail = File(thumb_io, name=(str(name) if name else image.name)) # create a django friendly File object
    return thumbnail
