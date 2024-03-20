from __future__ import absolute_import, unicode_literals

from .base import *
import os

import dj_database_url

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'


try:
    from .local import *
except ImportError:
    pass
