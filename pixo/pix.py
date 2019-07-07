# from PIL import Image

from .tag import Tag


class Pix:
    def __init__(self, key, meta):
        self.key = key
        self.base = meta['base']
        self.tags = [Tag(k, v) for k, v in meta['tags'].items()]

    def as_json(self):
        return {
            'key': self.key,
            'tags': [t.as_json() for t in self.tags]
        }

    def perform(self):
        return self.base
