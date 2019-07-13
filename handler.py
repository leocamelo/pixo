from json import dumps

from pixo import get_images, find_image, perform_image


def _response(status, body, extras={}):
    return {'statusCode': status, 'body': dumps(body), **extras}


def index(event, context):
    return _response(200, {'images': get_images()})


def show(event, context):
    key = event['pathParameters']['key']
    return _response(200, {'image': find_image(key)})


def perform(event, context):
    key = event['pathParameters']['key']

    try:
        image, mime = perform_image(key)
        return _response(200, image, {
            'headers': {
                'Content-Type': 'image/{}'.format(mime)
            },
            'isBase64Encoded': True
        })
    except ValueError as err:
        return _response(422, {'message': str(err)})
