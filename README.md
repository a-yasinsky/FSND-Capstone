# Guest houses list API

This is an API for hotels, guest houses or any other housing listing. Includes different roles for posting, updating and deleting housing. Implemented using python and FLASK Framework with auth0 for authentication and authorization, under Udacity Capstone project. Could be a starter boilerplate for a booking engine.

## Installing Dependencies

### Python

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.

- [python-jose](https://pypi.org/project/python-jose/) A JOSE implementation in Python. Used for working with JWT tokens.

- [Gunicorn](https://gunicorn.org/) is a Python WSGI HTTP Server for UNIX. Used for Heroku production.

## Database Setup
With Postgres running, in terminal run:
```bash
createdb housing
flask db upgrade
```

## Running the local server

First ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```

## Live application
The application is hosted on heroku under the url:
[https://sky-fsnd-capstone.herokuapp.com/](https://sky-fsnd-capstone.herokuapp.com/)

### Getting access tokens for TESTING

For testing the RBAC controls, there is  an postman_collection JSON file. You can import it in your postman and find the authorization tokens. Also valid tokens included into tets_app.py for testing purposes.

## Roles description
API requires authentication. There are 3 available roles:
1. Viewer:
  Can view housing list, housing data, search housing.
2. Manager
  Can do all view operations
  Can create new housing
  Can update housing information
3. Administrator
  Can do all described above operations
  Can delete housing

## Endpoints
### GET '/localities'
- Fetches an array of localities
- Request Arguments: None
- Returns: An object with array of localities objects, total localities length.
```
{
    "localities": [
        {
            "id": 1,
            "name": "London"
        },
        {
            "id": 2,
            "name": "New York"
        }
    ],
    "success": true,
    "total_localities": 2
}
```
### GET '/localities/{locality_id}/housing'
- Fetches an array of housing based on locality
- Request Arguments: locality ID
- Returns: An object with array of housing objects, total housing length,
        requested locality id, locality name
```
{
    "housing": [
        {

            "id": 2,
            "locality": "London",
            ...
        }
        ...
    ],
    "locality_id": 1,
    "locality_name": "London",
    "success": true,
    "total_housing": 1
}
```
### GET '/housing'
- Fetches an array of housing
- Request Arguments: None
- Returns: An object with object of housing objects in format 'id': housing,
      total housing length
```
{
  {
  "housing": {
      "2": {
          "category": "Guest house",
          "id": 2,
          "name": "test hotel with contacts",
          ...
      }
  },
  "success": true,
  "total_housing": 1
  }
}
```
### POST '/housing'
- Creates new housing using provided housing object
- Request Arguments: housing object including:
            name, description, locality_id, cathegory_id,
            photos, room_types, contacts
- Returns: created housing object
```
{
    "housing": {
        "category": "Guest house",
        "contacts": {
            "adress": "street line 1",
            "email": "test@test.kg",
            "facebook": "http://facebook.com/somehotel",
            "instagram": "@somehotel",
            "tel_number": "123456"
        },
        "description": "test description 2",
        "id": 3,
        "locality": "London",
        "name": "test 2",
        "photos": [
            "https://placeimg.com/640/480/any",
            "https://placeimg.com/640/480/any"
        ],
        "room_types": [
            {
                "id": 7,
                "name": "Single",
                "price": 100
            },
            {
                "id": 8,
                "name": "Double",
                "price": 200
            }
        ]
    },
    "success": true
}
```
### GET '/housing/{housing_id}'
- Fetches housing object if ID exists
- Request Arguments: housing ID
- Returns: A housing object
```
{
    "housing": {
        "category": "Guest house",
        "contacts": {
            "adress": "street line 1",
            "email": "test@test.kg",
            "facebook": "http://facebook.com/somehotel",
            "instagram": "@somehotel",
            "tel_number": "123456"
        },
        "description": "test description 2",
        "id": 3,
        "locality": "London",
        "name": "test 2",
        "photos": [
            "https://placeimg.com/640/480/any",
            "https://placeimg.com/640/480/any"
        ],
        "room_types": [
            {
                "id": 7,
                "name": "Single",
                "price": 100
            },
            {
                "id": 8,
                "name": "Double",
                "price": 200
            }
        ]
    },
    "success": true
}
```
### GET '/housing/search'
- Fetches an array of housing for whom the search term is a substring
  of the housing name or description
- Request Arguments: q - query term
- Returns: An object with object of housing objects in format 'id': housing,
      total housing length
```
{
    "housing": {
        "2": {
            "category": "Guest house",
            "name": "test hotel with contacts",
            ...
        }
    },
    "success": true,
    "total_housing": 1
}
```
### PATCH '/housing/{housing_id}'
- Update housing using provided housing object
- Request Arguments: housing object including:
            name, description, locality_id, cathegory_id,
            photos, room_types, contacts
- Returns: updated housing object
```
{
    "housing": {
        "description": "test description 2",
        "id": 3,
        "locality": "London",
        "name": "test 2",
        ...
    },
    "success": true
}
```
### DELETE '/housing/{housing_id}'
 - Deletes the housing of the given ID if it exists
 - Request Arguments: housing ID
```
 {
     'success': true,
     'housing_id': 3
 }
 ```

## Testing
To run the tests, run
```
createdb housing_test
export __ENV__=testing
python test_app.py
```
