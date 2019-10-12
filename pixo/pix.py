from io import BytesIO
from base64 import b64encode
from pathlib import PurePath

from PIL import Image, ImageDraw, ImageFont

from .tag import Tag


class Pix:
    def __init__(self, key, meta):
        self.key = key
        self.base = PurePath(meta['base'])
        self.tags = [Tag(k, v) for k, v in meta['tags'].items()]

    def __read_tag(self, folder, tag, text):
        path = str(folder / tag.font)
        font = ImageFont.truetype(path, tag.size)

        w, h = font.getsize(text)
        x = tag.x - (w // 2)
        y = tag.y - (h // 2)

        return (font, (x, y))

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
        folder = library / self.key

        image = Image.open(folder / self.base)
        draw = ImageDraw.Draw(image)

        for tag in self.tags:
            text = params.get(tag.key, '')
            font, xy = self.__read_tag(folder, tag, text)
            draw.text(xy, text, tag.color, font)

        buffered = BytesIO()
        image.save(buffered, self.mime().upper())

        return b64encode(buffered.getvalue()).decode('utf-8')
