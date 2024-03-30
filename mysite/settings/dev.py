from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition

INSTALLED_APPS += [
    "debug_toolbar",
]

INTERNAL_IPS = [ "127.0.0.1", "192.168.1.6", "*"]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y%kw1=k&)-=u6$x1m9(cjvi*7+!$hwy)ir!u%ge$r!5kjs^njg"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass


print("dev file; DEBUG =",DEBUG)