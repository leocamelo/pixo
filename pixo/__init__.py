import json
from pathlib import Path

from .pix import Pix


with open('package.json') as f:
    __version__ = json.load(f)['version']


def _library():
    return Path('library')


def _image(key):
    metafile = _library() / key / 'meta.json'

    with metafile.open() as f:
        return Pix(key, json.load(f))


def get_images():
    return [{'key': i.name} for i in _library().iterdir() if i.is_dir()]


def find_image(key):
    return _image(key).as_json()


def perform_image(key, params):
    image = _image(key)

    return image.perform(_library(), params), image.mime()
