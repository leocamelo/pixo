from io import BytesIO
from base64 import b64encode
from pathlib import PurePath

from PIL import Image, ImageDraw

from .tag import Tag


class Pix:
    def __init__(self, key, meta):
        self.key = key
        self.base = PurePath(meta['base'])
        self.tags = [Tag(k, v) for k, v in meta['tags'].items()]

    def as_json(self):
        return {
            'key': self.key,
            'tags': [t.as_json() for t in self.tags]
        }

    def mime(self):
        suffix = self.base.suffix
        if suffix == '.png':
            return 'png'
        elif suffix in ('.jpg', '.jpeg'):
            return 'jpeg'
        else:
            raise ValueError('Extension not supported: {}'.format(suffix))

    def perform(self, library, params):
        path = library / self.key / self.base

        image = Image.open(path)
        draw = ImageDraw.Draw(image)

        for tag in self.tags:
            text = params.get(tag.key, '')
            draw.text(tag.position(text), text, tag.color, tag.ttf)

        buffered = BytesIO()
        image.save(buffered, self.mime().upper())

        return b64encode(buffered.getvalue()).decode('utf-8')
