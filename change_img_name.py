from PIL import Image
import os



def get_date_taken(path):
    return Image.open(path)._getexif()[36867]

print(get_date_taken('IMG_3829.JPG'))

os.rename('IMG_3829.JPG',get_date_taken('IMG_3829.JPG') + '.JPG')