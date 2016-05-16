# gdg_web_v3
python과 flask,Semantic-ui등을 이용해서 개발한 페이지

# GDG_Web의 세번째 페이지

 - Php가 아닌 `Python`을 이용해서 개발해 보자!
 - 일일히 다 개발하기는 어려우니 `flask` 프레임워크를 이용하자
* `flask`가 마이크로 프레임워크라 해서 학습곡선이 짧다고는 하지만.. 어렵다!!
* ~~이해를 위해 `django`를 공부하고 나서야 `flask`를 이해하게 된건 안비밀!~~ 
 - `flask` 프레임워크 이용과 `DB ORM (SQLAlchemy)`, `WTForms` 이용.

## 백엔드 개발 방식

- flask를 이용해서 개발 해 보자!

##### Route (Controller)
flask에서는 
```python
@app.route('/index')
def index():
    return "Hello World!"
```
처럼 `@` 을 `데코레이터`라고 하는데 이를 이용해 메서드의 접근 주소 (endpoint?) 를 지정해준다.

##### Model 
SQLAlchemy 를 이용해서 모델을 선언해 준다.

```python
from app import db
from sqlalchemy.dialects.mysql import INTEGER, TEXT, TIMESTAMP
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(
        INTEGER(10, unsigned=True),
        primary_key=True,
        index=True
    )
    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )
    password = db.Column(
        TEXT,
        nullable=False
    )
    name = db.Column(
        db.String(80),
        nullable=False
    )
```

flask app이 model 관련 파일을 import 및 정의한다.
테이블이 존재하지 않으면 새 테이블을 생성해 준다.

DB 관련해서 새로운 항목을 생성한다던가 제거할 때 

```python
import UserModel

new_user = UserModel(
    username = form.username.data,
    password = form.password.data,
    name = form.name.data
)

if action=="add":
    db.session.add(new_user)
    
elif action=="delete":
    db.session.delete(new_user)
    
db.session.commit()
```

이런 식으로 데이터모델과 SQLAlchemy의 session 등을 이용해 데이터를 처리한다.

##### View (template)
- flask에서 사용하는 `Jinja2` 템플릿을 사용함으로써 뷰 구현을 매우 쉽게 할 수 있게 되었다.
- Jinja는 매우 강력한 템플릿 엔진이라서 굉장히 많은 기능을 구현할 수 있다.
- 특히 template_filter 와 같이 직접 사용자가 템플릿 필터를 만들어서 적용할 수도 있다.

ex) DatetimeObject를 template 단에서 처리 할 수 있게 됨으로 코드가 깔끔해진다.
(route 밑의 메서드에 따로 구현하지 않아도 된다.)
```python
import arrow

@app.add_template_filter
def humanize(time):
    time = arrow.get(time)
    return time.humanize(locale='ko')
```

html에서 Jinja 템플릿 변수 옆에 사용자 지정 필터를 명시해 주면 된다.
```html
<h2 class="ui header">
      {{ document.title }}
      <div class="sub header">{{ document.user_id | id_to_nickname }}</div>
      <div class="sub header">{{ document.created_date | humanize }}</div>
</h2>
```

##### Forms `(WTForms)`
- 일단 가장 신기했던 건 CSRF 보호가 된다!
- 수동으로 form을 만들때 input 태그 관련 값들을 직접 적어 주어야 했다. ((ex) id="name")
- 더 이상 그럴 필요가 없다!
- 심지어 form validation 까지 가능하다!!
- 매우 유용함!

```python
'''
WTForms 관련 import
해당 테이블 관련 모델 import
'''
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
```
```html
<form action="{{ request.url }}" method="POST" class="ui form{% if form.errors %} error{% endif %}">
        {{ form.csrf_token }}
    <div class="ui big fluid input{% if form.errors['username'] %} error{% endif %}">
        {{ form.title(placeholder="제목을 입력해주세요") }}
    </div>
    <div class="field{% if form.errors['content'] %} error{% endif %}">
        {{ form.content(placeholder="내용을 입력해주세요") }}
    </div>
</form>
```
이런 식으로 input 태그도 모두 알아서 해준다!
