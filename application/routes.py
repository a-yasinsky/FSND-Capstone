from flask import current_app as app
from flask import jsonify
from . import models

@app.route('/', methods=['POST', 'GET'])
def health():
    return jsonify("Healthy")
