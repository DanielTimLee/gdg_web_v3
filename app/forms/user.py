from app.models.user import UserModel
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, required, EqualTo, Email
from wtforms_alchemy import Unique
from wtforms_components import ModelForm


class SignUpForm(ModelForm):
    username = StringField('ID', [
        DataRequired(message='ID는 필수 항목입니다.'),
        Length(min=4, max=10, message='%(min)d글자 이상 %(max)d글자 이하로 입력해주세요.'),
        Unique(UserModel.username, message='이미 존재하는 아이디입니다.')
    ])
    password = PasswordField('Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    confirm_password = PasswordField('Confirm Password', [
        required(message='비밀번호 확인값은 필수 항목입니다.'),
        EqualTo('password', message='비밀번호와 비밀번호 확인값이 일치하지 않습니다.')
    ])
    name = StringField('Name', [
        required(message='이름은 필수 항목입니다.')
    ])
    nickname = StringField('Nickname', [
        required(message='닉네임은 필수 항목입니다.'),
        Length(min=4, max=16),
        Unique(UserModel.nickname, message='이미 존재하는 닉네임입니다.')
    ])
    email = EmailField('Email', [
        required(message='이메일은 필수 항목입니다.'),
        Email(message='올바른 이메일 형식이 아닙니다.'),
        Unique(UserModel.email, message='유효한 이메일 주소를 입력해주세요.')
    ])


class LoginForm(ModelForm):
    username = StringField('ID', [
        DataRequired(message='ID는 필수 항목입니다.'),
        Length(min=4, max=10, message='%(min)d글자 이상 %(max)d글자 이하로 입력해주세요.')
    ])
    password = PasswordField('Password', [
        DataRequired(message='PW는 필수 항목입니다.'),
        Length(min=4, max=10, message='%(min)d글자 이상 %(max)d글자 이하로 입력해주세요.')
    ])


class ModifyPasswordForm(ModelForm):
    password = PasswordField('Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    new_password = PasswordField('New Password', [
        required(message='비밀번호는 필수 항목입니다.'),
        Length(min=6, max=20, message='%(min)d 이상 %(max)d 이하로 입력해주세요.')
    ])
    new_confirm_password = PasswordField('New Confirm Password', [
        required(message='비밀번호 확인값은 필수 항목입니다.'),
        EqualTo('password', message='비밀번호와 비밀번호 확인값이 일치하지 않습니다.')
    ])


class ModifyProfileForm(ModelForm):
    username = StringField('ID', [])
    password = PasswordField('Password', [])
    confirm_password = PasswordField('Confirm Password', [])
    name = StringField('Name', [])
    nickname = StringField('Nickname', [
        Unique(UserModel.nickname, message='이미 존재하는 닉네임입니다.')
    ])
    email = EmailField('Email', [
        Unique(UserModel.email, message='유효한 이메일 주소를 입력해주세요.')
    ])
