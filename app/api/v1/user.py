import arrow
import yagmail
from flask import request
from flask_restful import Resource

from app import app, api_root, db
from app.models.user import UserModel


@api_root.resource('/v1/account')
class CreateAccount(Resource):
    def post(self):
        request_body = request.get_json()

        # password must be bcrypt.generate_password_hashed
        new_user = UserModel(
            username=request_body['username'],
            name=request_body['name'],
            password=request_body['password'],
            nickname=request_body['nickname'],
            email=request_body['email'],
            type='unregistered',
            created_date=arrow.utcnow().datetime
        )

        # TODO: 이메일 발송 처리
        # CreateAccount.SendAuthMail(email=request_body['email'], subject=,contents=)

        db.session.add(new_user)
        db.session.commit()

        return {
            'success': True
        }

    @staticmethod
    def SendAuthMail(email, subject, body):
        yagmail.SMTP(app.config['MAIL_USERNAME']).send(to=email, subject=subject, contents=body)


@api_root.resource('/v1/me')
class MyProfile(Resource):
    def get(self):
        my_profile_query = UserModel.query.filter(UserModel.id == 1)

        item = my_profile_query.first()

        return {
            'success': True,
            'item': item
        }

# @api_root.resource('/v1/me/verify')
# class VerifyMe(Resource):
