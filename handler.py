from json import dumps

from pixo import get_images, find_image, perform_image


def _response(status, body):
    return {'statusCode': status, 'body': dumps(body)}


def index(event, context):
    return _response(200, {'images': get_images()})


def show(event, context):
    key = event['pathParameters']['key']
    return _response(200, {'image': find_image(key)})


def perform(event, context):
    key = event['pathParameters']['key']

    try:
        return _response(200, {'image': perform_image(key)})
    except ValueError as err:
        return _response(422, {'message': str(err)})
