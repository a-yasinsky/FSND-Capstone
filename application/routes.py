from flask import current_app as app
from flask import jsonify
from . import models

@app.route('/', methods=['POST', 'GET'])
def health():
    return jsonify("Healthy")

@app.route('/localities', methods=['GET'])
def retrieve_localities():
    selection = models.Locality.query.order_by(models.Locality.name).all()
    if len(selection) == 0:
        abort(404)

    localities = {loc.id: loc.name for loc in selection}
    return jsonify({
        'success': True,
        'localities': localities,
        'total_categories': len(selection)
        })
