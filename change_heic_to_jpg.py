import pyheif
import PIL
import exifread

def read_heic(path: str):
    with open(path, 'rb') as file:
        image = pyheif.read_heif(file)
        for metadata in image.metadata or []:
            if metadata['type'] == 'Exif':
                fstream = io.BytesIO(metadata['data'][6:])

    # now just convert to jpeg
    pi = PIL.Image.open(fstream)
    pi.save("file.jpg", "JPEG")

    # or do EXIF processing with exifread
    tags = exifread.process_file(fstream)

read_heic("/Users/lhj/workspace/pet_project/IMG_3997 2.HEIC")
