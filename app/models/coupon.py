import datetime

from app import db
from sqlalchemy.dialects.mysql import INTEGER, TINYTEXT,TEXT, TIMESTAMP
from sqlalchemy.sql.expression import text


class CouponModel(db.Model):
    __tablename__ = 'coupon'
    __table_args__ = {
        'mysql_charset': 'utf8',
    }

    id = db.Column(
        INTEGER(10, unsigned=True),
        primary_key=True,
        index=True
    )
    company_type = db.Column(
        TINYTEXT,
        nullable=False
    )
    company = db.Column(
        TINYTEXT,
        nullable=False
    )
    company_desc = db.Column(
        TEXT,
        nullable=False
    )
    company_addr = db.Column(
        TINYTEXT,
        nullable=False
    )
    company_phone = db.Column(
        TINYTEXT,
        nullable=False
    )
    company_open_hour = db.Column(
        TINYTEXT,
        nullable=False
    )
    company_thumb = db.Column(
        TINYTEXT
    )
    company_menu = db.Column(
        TINYTEXT
    )
    coupon_content = db.Column(
        TINYTEXT,
        nullable=False
    )
    coupon_price = db.Column(
        INTEGER(10, unsigned=True),
        nullable=False
    )
    created_date = db.Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )
