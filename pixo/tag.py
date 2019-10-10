from PIL import ImageFont


class Tag:
    def __init__(self, key, meta):
        self.key = key

        self.size = meta['size']
        self.font = meta['font']
        self.color = meta['color']

        self.x = meta['position']['x']
        self.y = meta['position']['y']

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

    def read_font(self, folder, text):
        path = str(folder / self.font)
        font = ImageFont.truetype(path, self.size)

        w, h = font.getsize(text)
        x = self.x - (w // 2)
        y = self.y - (h // 2)

        return (font, (x, y))
