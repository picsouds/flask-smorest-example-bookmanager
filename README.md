# flask-smorest-example-bookmanager

Flask application example using then awesome [flask-smorest: Flask/Marshmallow-based REST API framework](https://flask-smorest.readthedocs.io/en/latest/)    
Widely inspired by https://github.com/lafrech/flask-smorest-sqlalchemy-example

## Packages

* flask-smorest 
* flask-marshmallow / Flask-SQLAlchemy and marshmallow-sqlalchemy.
* flask-jwt-extended  

## Database

Sqlite with delete cascade (a user - many book)

## Running locally

Set up Python environment:

```shell
$ pipenv install
```

To create a virtual environment you just execute the `$ pipenv shell`.

Run a development server:

```shell
$ FLASK RUN
```

Runs tests:

```shell
$ pipenv run python -m pytest tests/test_api.py::TestApi
```

Play with API

* Open http://127.0.0.1:5000/swagger-ui in your favorit browser
* Get un JWT token /Auth for the protected endpoint 
* Create a /author with the JWT token 
* Create a /book with the JWT token with a author id

Have Fun.