from pixo.tag import Tag


def test_as_json():
    key = 'text'
    meta = {
        'size': 12,
        'font': 'lato',
        'color': '#000000'
    }

    json = Tag(key, meta).as_json()

    assert type(json) is dict

    assert 'key' in json
    assert 'size' in json
    assert 'font' in json
    assert 'color' in json

    assert json['key'] == key
