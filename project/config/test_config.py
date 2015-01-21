# project/config/test_config.py


TESTING = True
SECRET_KEY = 'my_precious'
DEBUG = True
BCRYPT_LOG_ROUNDS = 1
WTF_CSRF_ENABLED = False
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_DATABASE_URI = 'sqlite://'
