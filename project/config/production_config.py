# project/config/production_config.py


SECRET_KEY = 'my_precious'
DEBUG = False
BCRYPT_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = True
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECTS = False
SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'
