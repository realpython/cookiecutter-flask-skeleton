# project/config/development_config.py

import os
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


SECRET_KEY = 'my_precious'
DEBUG = True
BCRYPT_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = False
DEBUG_TB_ENABLED = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')
