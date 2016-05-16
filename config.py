import os

basedir = os.path.abspath(os.path.dirname(__file__))

LOCALHOST = 'http://127.0.0.1:8000'

# flask
SECRET_KEY = '\x9c\xf2\xd1\x90G\xd9\x15\xc2\xb0Z\xc9\xb4I\xf4B\xb8I\x94\xf4\xc9&\xd9\xe7\x1e'

# db
DATABASE_HOST = 'localhost:3306'
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = ''
DEFAULT_DATABASE = 'gdg_web'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}/{3}".format(DATABASE_USERNAME,
                                                                   DATABASE_PASSWORD,
                                                                   DATABASE_HOST,
                                                                   DEFAULT_DATABASE)
