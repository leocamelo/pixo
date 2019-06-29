from json import dumps


def index(event, context):
    body = {
        'message': 'library here',
        'event': event
    }

    response = {
        'statusCode': 200,
        'body': dumps(body)
    }

    return response


def perform(event, context):
    body = {
        'message': 'awesome image here',
        'event': event
    }

    response = {
        'statusCode': 200,
        'body': dumps(body)
    }

    return response
