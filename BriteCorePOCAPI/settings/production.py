from .base import *
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    "default": dj_database_url.config(default='sqlite:///db.sqlite3'),
}