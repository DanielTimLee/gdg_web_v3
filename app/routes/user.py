from app import app, db
from app.forms.user import SignUpForm, LoginForm, ModifyPasswordForm, ModifyProfileForm
from app.helper.util import Validation, login_required, Document_Per_Page, pagination
from app.models.document import DocumentModel
from app.models.user import UserModel
from flask import request, redirect, render_template, flash, url_for, session


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('pages/user/dashboard.html')


@app.route("/<int:page>", methods=['GET', 'POST'])
@login_required
def my_document_list(page):
    board = 'mypage'

    document_list = DocumentModel.query. \
        filter_by(user_id=session['id']). \
        order_by(DocumentModel.id.desc()). \
        offset((page - 1) * Document_Per_Page). \
        limit(Document_Per_Page). \
        all()

    data = dict()
    data['board'] = board

    return render_template('pages/component/list.html',
                           document_list=document_list,
                           pagination=pagination(board, page),
                           data=data)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm(request.form)

    if Validation(form):
        new_user = UserModel(
            username=form.username.data,
            password=form.password.data,
            name=form.name.data,
            nickname=form.nickname.data,
            email=form.email.data,
        )
        db.session.add(new_user)
        db.session.commit()

        flash('회원가입이 성공적으로 처리되었습니다.')
        return redirect(url_for('index'))

    return render_template('pages/user/signup.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if Validation(form):
        try:
            user_data = UserModel.query. \
                filter_by(username=form.username.data). \
                one()
        except:
            flash('회원정보가 올바르지 않습니다.')
            return render_template('pages/user/login.html', form=form)

        if user_data.password == form.password.data:
            session['username'] = request.form['username']
            session['id'] = user_data.id
            flash('성공적으로 로그인 되었습니다.')
            return redirect(url_for('index'))

        else:
            flash('회원정보가 올바르지 않습니다.')
            return render_template('pages/user/login.html', form=form)

    return render_template('pages/user/login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash('성공적으로 로그아웃 되었습니다.')
    return redirect(url_for('index'))


@app.route('/modify_pass', methods=['GET', 'POST'])
@login_required
def modify_pass():
    form = ModifyPasswordForm(request.form)

    if Validation(form):
        mod_user = UserModel.query.filter_by(username=session['username']).one()
        mod_user.password = form.name.new_password

        db.session.commit()

    return render_template('pages/user/modify_password.html', form=form)


@app.route('/modify_profile', methods=['GET', 'POST'])
@login_required
def modify_profile():
    mod_user = UserModel.query.filter_by(username=session['username']).one()

    form = ModifyProfileForm(request.form)
    form.username.data = mod_user.username
    form.name.data = mod_user.name
    if Validation(form):
        mod_user.name = form.name.data
        mod_user.nickname = form.nickname.data
        mod_user.email = form.email.data

        db.session.commit()

        flash('회원 정보 수정이 성공적으로 처리되었습니다.')
        return redirect(url_for('index'))

    return render_template('pages/user/modify_profile.html', form=form)
