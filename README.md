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


## Endpoints
