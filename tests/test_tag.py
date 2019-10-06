from pixo.tag import Tag


def test_as_json():
    key = 'text'
    meta = {
        'size': 34,
        'font': 'Arial',
        'color': '#333333',
        'position': {
            'x': 526,
            'y': 360
        }
    }

    json = Tag(key, meta).as_json()

    assert type(json) is dict

    assert 'key' in json
    assert 'size' in json
    assert 'font' in json
    assert 'color' in json

    assert 'position' in json
    assert 'x' in json['position']
    assert 'y' in json['position']

    assert json['key'] == key
