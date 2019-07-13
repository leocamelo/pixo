from pathlib import Path
from json import load

from .pix import Pix


__version__ = '0.1.0'


def _library():
    return Path('library')


def _image(key):
    metafile = _library() / key / 'meta.json'

    with metafile.open() as f:
        return Pix(key, load(f))


def get_images():
    return [{'key': i.name}
            for i in _library().iterdir() if i.is_dir()]


def find_image(key):
    return _image(key).as_json()


def perform_image(key):
    image = _image(key)

    return image.perform(_library()), image.mime()
