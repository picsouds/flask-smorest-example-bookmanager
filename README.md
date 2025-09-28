![CI](https://github.com/picsouds/flask-smorest-example-bookmanager/actions/workflows/ci.yml/badge.svg)

# flask-smorest-example

Flask application example using the awesome [flask-smorest: Flask/Marshmallow-based REST API framework](https://flask-smorest.readthedocs.io/en/latest/)    
Widely inspired by https://github.com/lafrech/flask-smorest-sqlalchemy-example

[![Capture-d-cran-du-2025-09-28.png](https://i.postimg.cc/DZStyMjL/Capture-d-cran-du-2025-09-28.png)](https://postimg.cc/gXPMgNP2)

## Packages

* Flask 3.1
* flask-smorest 0.46
* flask-sqlalchemy 3.1 / sqlalchemy 2.0 / marshmallow-sqlalchemy 1.4
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

## ✨ Play with API

* Open http://127.0.0.1:5000/swagger-ui in your favorite browser
* /auth/login 
   * Get un JWT token (access_token) for the protected endpoint {"username":"admin","password":"secret"} 
* /authors with a valid JWT token for POST / PUT / DELETE
   * PUT (need a valid etag in the If-Match HTTP request header)
   * DELETE (need a valid etag and delete cascade books)  
* /books with a valid JWT token for POST / PUT / DELETE
   * PUT (need a valid etag in the If-Match HTTP request header)
   * DELETE (need a valid etag)

Have Fun.

## 🧹 Code Style & Linting

Install the formatting and linting tools with Poetry:

```shell
poetry add --group dev black flake8
```

Run them locally before committing:

```shell
poetry run black .
poetry run flake8 .
```

Both tools respect settings defined in `pyproject.toml`: max line length is 100 and Flake8 ignores `E203` and `W503` to align with Black's formatting. Keep your virtual environment up to date, run Black to auto-format, then use Flake8 to catch issues Black does not cover (imports, unused code, complexity). Running both ensures consistent style across contributors and keeps the CI lint checks green.
