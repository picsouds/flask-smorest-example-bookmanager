![CI](https://github.com/picsouds/flask-smorest-example-bookmanager/actions/workflows/ci.yml/badge.svg)

# flask-smorest-example

Flask application example using the awesome [flask-smorest: Flask/Marshmallow-based REST API framework](https://flask-smorest.readthedocs.io/en/latest/)    
Widely inspired by https://github.com/lafrech/flask-smorest-sqlalchemy-example

![Capture-d-cran-du-2020-08-03-20-28-16.png](https://i.postimg.cc/nrH1SHZP/Capture-d-cran-du-2020-08-03-20-28-16.png)

## Packages

* Flask 3.1
* flask-smorest 0.46 with Marshmallow 4
* Flask-SQLAlchemy 3 + SQLAlchemy 2.0
* flask-jwt-extended 4.7 

## Database

Sqlite with delete cascade (relation an author - many book)

## Running locally

Set up Python environment with [Poetry](https://python-poetry.org/):

```shell
poetry install
cp .env.example .env  # adjust secrets as needed
```

Run a development server:

```shell
poetry run flask --app book_manager --debug run
```

Run the test suite:

```shell
poetry run pytest
```

Play with API

* Open http://127.0.0.1:5000/swagger-ui in your favorit browser
* /auth 
   * Get un JWT token for the protected endpoint
* /authors with a valid JWT token for POST / PUT / DELETE
   * PUT (need a valid etag in the If-Match HTTP request header)
   * DELETE (need a valid etag and delete cascade books)  
* /books with a valid JWT token for POST / PUT / DELETE
   * PUT (need a valid etag in the If-Match HTTP request header)
   * DELETE (need a valid etag)

Have Fun.
