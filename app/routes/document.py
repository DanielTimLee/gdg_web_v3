from app import app, db
from app.forms.comment import CommentForm
from app.forms.document import DocumentForm
from app.helper.util import Validation, login_required, Document_Per_Page, pagination, board_check
from app.models.document import DocumentModel
from app.routes.comment import comment_write, comment_list
from flask import render_template, request, redirect, url_for, abort, session, flash


@app.route("/<string:board>/<int:page>", methods=['GET', 'POST'])
def document_list(board, page):
    board_check(board)

    document_list = DocumentModel.query. \
        filter_by(board=board). \
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


@app.route("/<string:board>/<int:document_id>/read", methods=['GET', 'POST'])
def document_view(board, document_id):
    board_check(board)

    form = CommentForm(request.form)

    try:
        document = DocumentModel.query. \
            filter_by(board=board). \
            filter_by(id=document_id). \
            one()
    except:
        abort(404)

    document.read_count += 1
    db.session.commit()

    if Validation(form):
        comment_write(board, document_id, form)

    data = dict()
    data['board'] = board

    return render_template('pages/component/view.html',
                           document=document,
                           comments=comment_list(document_id),
                           data=data,
                           form=form)


@app.route("/<string:board>/write", methods=['GET', 'POST'])
@login_required
def document_write(board):
    board_check(board)

    form = DocumentForm(request.form)

    if Validation(form):
        new_document = DocumentModel(
            board=board,
            title=form.title.data,
            content=form.content.data,
            user_id=session['id']
        )

        db.session.add(new_document)
        db.session.commit()

        flash('글이 성공적으로 작성되었습니다.')
        return redirect(url_for('document_list', board=board, page=1))

    data = dict()
    data['board'] = board

    return render_template('pages/component/write.html',
                           form=form,
                           data=data)


@app.route("/<string:board>/<int:document_id>/modify", methods=['GET', 'POST'])
@login_required
def document_modify(board, document_id):
    board_check(board)

    form = DocumentForm(request.form)

    try:
        modify_document = DocumentModel.query. \
            filter_by(board=board). \
            filter_by(id=document_id). \
            one()
    except:
        abort(404)

    if Validation(form):
        modify_document.title = form.title.data
        modify_document.content = form.content.data,

        db.session.commit()

        flash('글이 성공적으로 수정되었습니다.')
        return redirect(url_for('document_list', board=board, page=1))

    else:
        form.title.default = modify_document.title
        form.content.default = modify_document.content
        form.process()

    data = dict()
    data['board'] = board

    return render_template('pages/component/write.html',
                           form=form,
                           data=data)


@app.route("/<string:board>/<int:document_id>/delete", methods=['GET', 'POST'])
@login_required
def document_delete(board, document_id):
    board_check(board)

    try:
        delete_document = DocumentModel.query. \
            filter_by(board=board). \
            filter_by(id=document_id). \
            one()
    except:
        abort(404)

    db.session.delete(delete_document)
    db.session.commit()

    data = dict()
    data['board'] = board

    flash('글이 성공적으로 삭제되었습니다.')
    return redirect(url_for('document_list', board=board, page=1))
