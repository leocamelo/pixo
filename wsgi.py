from flask import Flask, request, jsonify, make_response

from pyxo import get_images, find_image, perform_image


app = Flask(__name__)
app.config.from_mapping(SECRET_KEY='Z1ON0101')


@app.route('/api')
def index():
    return jsonify(images=get_images())


@app.route('/api/<key>')
def show(key):
    return jsonify(image=find_image(key))


@app.route('/image/<key>')
def perform(key):
    image, mime = perform_image(key, request.args.to_dict())

    response = make_response(image)
    response.headers['Content-Type'] = 'image/{}'.format(mime)
    response.headers['Content-Transfer-Encoding'] = 'base64'

    return response
