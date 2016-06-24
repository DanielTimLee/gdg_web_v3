import arrow
from app import app
from app.models.document import DocumentModel
from app.models.user import UserModel
from flask import session, request, redirect, url_for, flash, abort
from functools import wraps

Document_Per_Page = 10


def Validation(form):
    if request.method == 'POST' and form.validate():
        return True

    return False


def board_check(board):
    board_list = ['free', 'notice']

    if board not in board_list:
        return abort(404)

    return


def pagination(board, page):
    if board == 'mypage':
        total_document = DocumentModel.query.filter_by(user_id=session['id']).count()
    else:
        total_document = DocumentModel.query.filter_by(board=board).count()

    data = dict()
    data['page'] = round((total_document / Document_Per_Page) + 0.5)
    data['start_index'] = total_document - (page - 1) * Document_Per_Page

    return data


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session:
            flash('로그인이 필요합니다. 로그인을 먼저 해주세요.')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.add_template_filter
def humanize(time):
    now=arrow.utcnow()
    time = arrow.get(time)
    return now.humanize(time,locale='ko')


@app.add_template_filter
def id_to_nickname(user_id):
    user = UserModel.query.filter_by(id=user_id).one()
    return user.nickname
