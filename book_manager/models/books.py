"""Books model"""

import uuid

import sqlalchemy_utils
from sqlalchemy.orm import backref

from book_manager.extensions.database import db


class Book(db.Model):
    """Book model class"""

    __tablename__ = "books"

    id = db.Column(
        sqlalchemy_utils.types.uuid.UUIDType(binary=False), primary_key=True, default=uuid.uuid4
    )
    title = db.Column(db.String(length=40), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp()
    )
    # https://stackoverflow.com/questions/5033547/sqlalchemy-cascade-delete
    author_id = db.Column(
        sqlalchemy_utils.types.uuid.UUIDType(binary=False),
        db.ForeignKey("authors.id", ondelete="CASCADE"),
    )
    author = db.relationship("Author", backref=backref("books", passive_deletes=True))
