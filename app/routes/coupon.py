import os
from app import app
from app.helper.util import login_required
from app.models.coupon import CouponModel
from flask import request, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/coupon')
def coupon_home():
    return render_template('coupon/pages/index.html')

@app.route('/coupon/list')
def coupon_list():
    type = request.args.get('type')

    coupons_query = CouponModel.query

    if type:
        coupons_query = coupons_query.filter(CouponModel.company_type == type)

    coupons = coupons_query.all()

    return render_template('coupon/pages/list.html', coupons=coupons)


@app.route('/coupon/add', methods=['GET','POST'])
@login_required
def coupon_add():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('coupon/pages/add_complete.html')

    return render_template('coupon/pages/add.html')


@app.route('/coupon/view/<int:coupon_id>')
def coupon_view(coupon_id):

    coupon = CouponModel.query.filter(CouponModel.id == coupon_id).one()
    
    return render_template('coupon/pages/view.html', coupon=coupon)

