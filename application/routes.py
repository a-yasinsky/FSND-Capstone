from flask import current_app as app
from flask import jsonify

@app.route('/', methods=['POST', 'GET'])
def health():
    return jsonify("Healthy")
