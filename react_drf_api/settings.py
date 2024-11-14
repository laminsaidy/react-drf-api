import django_heroku
import dj_database_url
import re
from pathlib import Path
import os
from datetime import timedelta
from django.core.management.utils import get_random_secret_key

# Secret key setup
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', get_random_secret_key())

# Cloudinary settings
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'

# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
JWT_AUTH_SECURE = True

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Django settings
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'my-react-drf-api.herokuapp.com',
    '8000-laminsaidy-reactdrfapi-hgzcukbglad.ws.codeinstitute-ide.net',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_filters',
    'rest_framework',
    'dj_rest_auth',
    'rest_framework.authtoken',
    'dj_rest_auth.registration',
    'corsheaders',
    'profiles',
    'posts',
    'comments',
    'likes',
    'followers',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# CORS settings
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # for local dev
    "https://blogify-react-d942246c204e.herokuapp.com",  # replace with your deployed React app URL
]

CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https://.*\.gitpod\.io$",  # If using Gitpod
    r"^https://my-react-drf-api.herokuapp.com",  # for Heroku
]

CORS_ALLOW_CREDENTIALS = True

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd8t85sppgtlb22',
        'USER': 'u7bop2kdbai70o',
        'PASSWORD': 'p038a6a1d0ce9b3de04e7fbda7ec9a5abf3d0686a9205c8d97380f5b5778f4772',
        'HOST': 'c3l5o0rb2a6o4l.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}



CSRF_TRUSTED_ORIGINS = [
    'https://my-react-drf-api.herokuapp.com',  # For your production URL
    'http://localhost',  # For local development
    'http://127.0.0.1',  
    'https://8001-laminsaidy-reactdrfapi-u83x66feewk.ws.codeinstitute-ide.net',  # Code Institute IDE
    'https://8000-laminsaidy-reactdrfapi-au2b3a5cu7m.ws.codeinstitute-ide.net',  # New IDE URL to fix CSRF error
]

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = BASE_DIR / 'staticfiles'   
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'react_drf_api.urls'  