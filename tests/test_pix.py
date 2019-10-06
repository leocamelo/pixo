from pytest import raises

from pixo.pix import Pix


def test_as_json():
    key = 'sunflowers'
    meta = {
        'base': 'image.jpg',
        'tags': {
            'text': {
                'size': 34,
                'font': 'Arial',
                'color': '#333333',
                'position': {
                    'x': 526,
                    'y': 360
                }
            }
        }
    }

    json = Pix(key, meta).as_json()

    assert type(json) is dict

    assert 'key' in json
    assert 'tags' in json

    assert json['key'] == key


def test_mime():
    png_image = Pix('foo', {'base': 'image.png', 'tags': {}})
    jpg_image = Pix('bar', {'base': 'image.jpg', 'tags': {}})
    gif_image = Pix('baz', {'base': 'image.gif', 'tags': {}})

    assert png_image.mime() == 'png'
    assert jpg_image.mime() == 'jpeg'

    with raises(ValueError, match=r'^Extension not supported'):
        gif_image.mime()


def test_perform():
    assert 1 == 1
