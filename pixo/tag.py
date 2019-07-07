class Tag:
    def __init__(self, key, meta):
        self.key = key

        self.size = meta['size']
        self.font = meta['font']
        self.color = meta['color']

    def as_json(self):
        return {
            'key': self.key,
            'size': self.size,
            'font': self.font,
            'color': self.color
        }
