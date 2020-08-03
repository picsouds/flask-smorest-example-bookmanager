[![Build Status](https://travis-ci.com/picsouds/flask-smorest-example-bookmanager.svg?branch=master)](https://travis-ci.com/picsouds/flask-smorest-example-bookmanager)
[![Coverage Status](https://coveralls.io/repos/github/picsouds/flask-smorest-example-bookmanager/badge.svg)](https://coveralls.io/github/picsouds/flask-smorest-example-bookmanager)

# flask-smorest-example-bookmanager

Flask application example using the awesome [flask-smorest: Flask/Marshmallow-based REST API framework](https://flask-smorest.readthedocs.io/en/latest/)    
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
* /auth 
   * Get un JWT token for the protected endpoint
* /authors a valid JWT token for POST / PUT / DELETE
   * PUT (need a valid etag in the If-Match HTTP request header)
   * DELETE (need a valid etag and delete cascade books)  
* /books with a valid JWT token for POST / PUT / DELETE
   * PUT (need a valid etag in the If-Match HTTP request header)

Have Fun.
