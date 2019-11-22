import json
from base64 import b64encode

from pyxo import get_images, find_image, perform_image


def _response(status_code, body, **extras):
    parsed_body = json.dumps(body) if type(body) is dict else body
    return {'statusCode': status_code, 'body': parsed_body, **extras}


def index(event, context):
    return _response(200, {'message': 'Welcome to Pyxo!'})


def list(event, context):
    return _response(200, {'images': get_images()})


def show(event, context):
    key = event['pathParameters']['key']
    return _response(200, {'image': find_image(key)})


def perform(event, context):
    key = event['pathParameters']['key']
    params = event['queryStringParameters'] or {}

    try:
        image, mime = perform_image(key, params)
        image64 = b64encode(image).decode('utf-8')
        headers = {'Content-Type': 'image/{}'.format(mime)}
        return _response(200, image64, headers=headers, isBase64Encoded=True)
    except ValueError as err:
        return _response(422, {'message': str(err)})
