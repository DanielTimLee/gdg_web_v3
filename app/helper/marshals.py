from flask_restful import fields

class_fields = {
    'id': fields.Integer(attribute='id'),
    '과목번호': fields.String(attribute='과목번호'),
    '이수구분_주': fields.String(attribute='이수구분_주'),
    '이수구분_다': fields.String(attribute='이수구분_다'),
    '교과영역': fields.String(attribute='교과영역'),
    '과목명': fields.String(attribute='과목명'),
    '분반': fields.String(attribute='분반'),
    '교수명': fields.String(attribute='교수명'),
    '개설학과': fields.String(attribute='개설학과'),
    '시간': fields.String(attribute='시간'),
    '학점_설계': fields.String(attribute='학점_설계'),
    '강의시간_강의실': fields.String(attribute='강의시간_강의실'),
    '과정': fields.String(attribute='과정'),
    '수강대상': fields.String(attribute='수강대상')
}
