from pathlib import Path
from json import load

from .pix import Pix


__version__ = '0.1.0'


def _image(key):
    library = Path('library')
    metafile = library / key / 'meta.json'

    with metafile.open() as f:
        return Pix(key, load(f))


def get_images():
    library = Path('library')

    return [{'key': i.name}
            for i in library.iterdir() if i.is_dir()]


def find_image(key):
    return _image(key).as_json()


def perform_image(key):
    return _image(key).perform()
