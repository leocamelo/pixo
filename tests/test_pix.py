from pixo.pix import Pix


def test_as_json():
    key = 'sunflowers',
    meta = {
        'base': 'image.jpg',
        'tags': {
            'text': {
                'size': 12,
                'font': 'lato',
                'color': '#000000'
            }
        }
    }

    json = Pix(key, meta).as_json()

    assert type(json) is dict

    assert 'key' in json
    assert 'tags' in json

    assert json['key'] == key


def test_perform():
    assert 1 == 1
