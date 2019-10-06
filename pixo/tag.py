from PIL import ImageFont


class Tag:
    def __init__(self, key, meta):
        self.key = key

        self.size = meta['size']
        self.font = meta['font']
        self.color = meta['color']

        self.x = meta['position']['x']
        self.y = meta['position']['y']

        self.__ttf = None

    @ property
    def ttf(self):
        if not self.__ttf:
            self.__ttf = ImageFont.truetype(self.font, self.size)
        return self.__ttf

    def as_json(self):
        return {
            'key': self.key,
            'size': self.size,
            'font': self.font,
            'color': self.color,
            'position': {
                'x': self.x,
                'y': self.y
            }
        }

    def position(self, text):
        w, h = self.ttf.getsize(text)
        return (self.x - (w // 2), self.y - (h // 2))
