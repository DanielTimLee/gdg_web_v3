import datetime

from app import db
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TIMESTAMP
from sqlalchemy.sql.expression import text


class CommentModel(db.Model):
    __tablename__ = 'comments'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    id = db.Column(
        INTEGER(10, unsigned=True),
        primary_key=True,
        index=True
    )
    document_id = db.Column(
        INTEGER(10, unsigned=True),
        db.ForeignKey('documents.id'),
        nullable=False
    )
    content = db.Column(
        LONGTEXT,
        nullable=False
    )
    user_id = db.Column(
        INTEGER(10, unsigned=True),
        db.ForeignKey('users.id'),
        nullable=False
    )
    created_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )
