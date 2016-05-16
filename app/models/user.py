import datetime

from app import db
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TIMESTAMP
from sqlalchemy.sql.expression import text


class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    type_enums = ('unregistered', 'registered', 'manager', 'graduate')

    id = db.Column(
        INTEGER(10, unsigned=True),
        primary_key=True,
        index=True
    )
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    password = db.Column(
        TEXT,
        nullable=False
    )
    name = db.Column(
        db.String(80),
        nullable=False
    )
    nickname = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    type = db.Column(
        db.Enum(*type_enums),
        default=type_enums[0],
        server_default=type_enums[0]
    )
    created_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )
