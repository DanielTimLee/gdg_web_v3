from app import db, app
from app.helper.util import login_required
from app.models.comment import CommentModel
from flask import redirect, session, url_for


def comment_list(document_id):
    return CommentModel.query. \
        filter_by(document_id=document_id). \
        all()


@login_required
def comment_write(board, document_id, form):
    new_comment = CommentModel(
        document_id=document_id,
        content=form.content.data,
        user_id=session['id']
    )

    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('document_view', board=board, document_id=document_id))


@app.route("/<string:board>/<int:document_id>/comment/<int:comment_id>")
@login_required
def comment_delete(board, document_id, comment_id):
    delete_comment = CommentModel.query. \
        filter_by(id=comment_id). \
        one()

    db.session.delete(delete_comment)
    db.session.commit()

    return redirect(url_for('document_view', board=board, document_id=document_id))
