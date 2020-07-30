"""Relational database"""

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # pylint: disable=invalid-name
ma = Marshmallow()


def init_app(app):
    """Initialize relational database extension"""
    db.init_app(app)

    # Ensure FOREIGN KEY for sqlite3 for cascade delete
    if 'sqlite' in app.config['SQLALCHEMY_DATABASE_URI']:
        def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
            dbapi_con.execute('pragma foreign_keys=ON')

        with app.app_context():
            from sqlalchemy import event
            event.listen(db.engine, 'connect', _fk_pragma_on_connect)

    db.create_all(app=app)
