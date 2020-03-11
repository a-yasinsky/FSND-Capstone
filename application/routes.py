import sys
from flask import current_app as app
from flask import jsonify, abort, request

from . import models
from .auth.auth import AuthError, requires_auth

@app.route('/', methods=['POST', 'GET'])
def health():
    return jsonify("Healthy")

@app.route('/localities', methods=['GET'])
def retrieve_localities():
    selection = models.Locality.query.order_by(models.Locality.name).all()
    localities = {loc.id: loc.name for loc in selection}
    return jsonify({
        'success': True,
        'localities': localities,
        'total_localities': len(selection)
        })

@app.route('/localities/<int:locality_id>/housing', methods=['GET'])
def retrieve_housing_by_locality(locality_id):
    locality = models.Locality.query.get_or_404(locality_id)
    return jsonify({
        'success': True,
        'locality_id': locality_id,
        'locality_name': locality.name,
        'housing': [housing.format() for housing in locality.housing],
        'total_housing': len(locality.housing)
        })

@app.route('/housing', methods=['GET'])
def retrieve_housing():
    selection = models.Housing.query.all()
    if len(selection) == 0:
        abort(404)

    housing = {house.id: house.format() for house in selection}
    return jsonify({
        'success': True,
        'housing': housing,
        'total_categories': len(selection)
        })

@app.route('/housing', methods=['POST'])
@requires_auth('post:housing')
def create_housing(payload):
    body = request.get_json()

    new_name = body.get('name', None)
    new_description = body.get('description', None)
    new_locality_id = body.get('locality', None)
    new_category_id = body.get('category', None)
    new_photos = body.get('photos', [])
    new_room_types = body.get('room_types', [])
    new_contacts = body.get('contacts', {})
    try:
        housing = models.Housing(new_name, new_description,
                                new_locality_id, new_category_id)

        housing.insert(photos=new_photos, room_types=new_room_types,
                        contacts=new_contacts)

        return jsonify({
            'success': True,
            'housing': housing.format()
            })

    except:
        print(sys.exc_info())
        abort(422)

@app.route('/housing/<int:housing_id>', methods=['GET'])
def retrieve_housing_info(housing_id):
    housing = models.Housing.query.get_or_404(housing_id)
    return jsonify({
        'success': True,
        'housing': housing.format()
        })

@app.route('/housing/search', methods=['GET'])
def search_housing():
    search_term = request.args.get('q')
    selection = models.Housing.getSearchResults(search_term)

    housing = {house.id: house.format() for house in selection}
    return jsonify({
        'success': True,
        'housing': housing,
        'total_housing': len(selection)
        })

@app.route('/housing/<int:housing_id>', methods=['PATCH'])
@requires_auth('patch:housing')
def update_housing(payload, housing_id):
    body = request.get_json()

    new_name = body.get('name', None)
    new_description = body.get('description', None)
    new_photos = body.get('photos', [])
    new_room_types = body.get('room_types', [])
    new_contacts = body.get('contacts', {})
    try:
        housing = models.Housing.query.get_or_404(housing_id)
        if new_description:
            housing.description = new_description
        if new_name:
            housing.name = new_name

        housing.update(photos=new_photos, room_types=new_room_types,
                        contacts=new_contacts)

        return jsonify({
            'success': True,
            'housing': housing.format()
            })

    except:
        print(sys.exc_info())
        abort(422)

@app.route('/housing/<int:housing_id>', methods=['DELETE'])
@requires_auth('delete:housing')
def delete_housing(payload, housing_id):
    try:
        housing = models.Housing.query.get_or_404(housing_id)
        housing.delete()

        return jsonify({
            'success': True,
            'housing': housing_id
            })

    except:
        print(sys.exc_info())
        abort(422)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
                    "success": False,
                    "erorr": 404,
                    "message": "resource not found"
                    }), 404

@app.errorhandler(422)
def not_found(error):
    return jsonify({
                    "success": False,
                    "erorr": 422,
                    "message": "unprocessable entity"
                    }), 422

@app.errorhandler(400)
def not_found(error):
    return jsonify({
                    "success": False,
                    "erorr": 400,
                    "message": "bad request"
                    }), 400

@app.errorhandler(500)
def not_found(error):
    return jsonify({
                    "success": False,
                    "erorr": 500,
                    "message": "internal server error"
                    }), 500

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
