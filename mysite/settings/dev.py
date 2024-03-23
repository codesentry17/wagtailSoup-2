from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# COMPRESS_OFFLINE = True
# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.css_default.CssAbsoluteFilter',
#     'compressor.filters.cssmin.CSSMinFilter',
# ]
# COMPRESS_CSS_HASHING_METHOD = 'content'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y%kw1=k&)-=u6$x1m9(cjvi*7+!$hwy)ir!u%ge$r!5kjs^njg"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass


print("DEBUG =",DEBUG)