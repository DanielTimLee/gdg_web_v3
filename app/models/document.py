import datetime

from app import db
from sqlalchemy.dialects.mysql import TIMESTAMP, INTEGER, TINYTEXT, LONGTEXT
from sqlalchemy.sql.expression import text


class DocumentModel(db.Model):
    __tablename__ = 'documents'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = db.Column(
        INTEGER(10, unsigned=True),
        primary_key=True,
        index=True
    )
    board = db.Column(
        TINYTEXT
    )
    title = db.Column(
        TINYTEXT,
        nullable=False
    )
    content = db.Column(
        LONGTEXT,
        nullable=False
    )
    read_count = db.Column(
        INTEGER(10, unsigned=True),
        default=0
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
