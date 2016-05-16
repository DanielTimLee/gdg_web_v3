from flask_wtf import Form
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class CommentForm(Form):
    content = TextAreaField('Content', [
        DataRequired(message='Content는 필수 항목입니다.')])
