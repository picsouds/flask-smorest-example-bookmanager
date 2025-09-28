"""Author model"""

import uuid

import sqlalchemy_utils

from book_manager.extensions.database import db


class Author(db.Model):
    """Author model class"""

    __tablename__ = "authors"

    id = db.Column(
        sqlalchemy_utils.types.uuid.UUIDType(binary=False), primary_key=True, default=uuid.uuid4
    )
    first_name = db.Column(db.String(length=40), nullable=False)
    last_name = db.Column(db.String(length=40), nullable=False)
    birth_date = db.Column(db.Date(), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()
    )
