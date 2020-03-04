import sys
from flask import current_app as app
from flask import jsonify, abort, request
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

@app.route('/housing', methods=['GET'])
def retrieve_housing():
    selection = models.Housing.query.all()
    if len(selection) == 0:
        abort(404)

    housing = {house.id: house.format() for house in selection}
    return jsonify({
        'success': True,
        'localities': housing,
        'total_categories': len(selection)
        })

@app.route('/housing', methods=['POST'])
def create_housing():
    body = request.get_json()

    new_name = body.get('name', None)
    new_description = body.get('description', None)
    new_locality_id = body.get('locality', None)
    new_category_id = body.get('category', None)
    new_photos = body.get('photos', [])
    try:
        housing = models.Housing(new_name, new_description,
                                new_locality_id, new_category_id)

        housing.insert(photos=new_photos)

        return jsonify({
            'success': True,
            'housing': [housing.format()]
            })

    except:
        print(sys.exc_info())
        abort(422)
