# hng_profile_project/settings.py


from pathlib import Path
from datetime import timedelta
from environs import Env
import os

import sys
import logging.config # For logging

# Initialize Env for reading .env file
env = Env()
env.read_env() # Reads the .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Get SECRET_KEY from environment variable
SECRET_KEY = env("SECRET_KEY", default='django-insecure-b*tuoe%^o+=^35$0fufrm=oamh^(o0tabn39(7ni12(i-oup+4') # Fallback for local, but ensure it's set in .env for production


# SECURITY WARNING: don't run with debug turned on in production!
# Get DEBUG from environment variable
DEBUG = env.bool("DEBUG", default=True) # Default to True for local, set to False in .env for production


# Site URL
SITE_URL = env("SITE_URL", default="http://127.0.0.1:8000")

DJANGO_SECRET_ADMIN_URL=env("DJANGO_SECRET_ADMIN_URL", default="admin/")

# ALLOWED_HOSTS from environment variable, split by comma
# For production, specify your Render URL and any other hostnames.
# For local, '127.0.0.1' and 'localhost' are usually sufficient.
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["127.0.0.1", "localhost", "localhost:8000", "localhost:3001"])
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=['http://localhost:3000', 'http://localhost:8000'])
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'



INSTALLED_APPS = [
    # Default Django Apps (Order can matter, keep admin near the top)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'drf_yasg',  # Add this line for Swagger UI
    
    
    # Your local apps
    'profile_api.apps.ProfileApiConfig', # Or just 'profile_api'
]

# ... rest of your settings

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hng_profile_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'hng_profile_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'


# ... at the bottom of the file, near STATIC_URL
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Add this line

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'







# LOGGING CONFIGURATION
# This setup provides detailed logging to the console.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # Formatters define the layout of your log messages
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    # Handlers determine what happens to the log messages (e.g., print to console, save to file)
    'handlers': {
        'console': {
            'level': 'DEBUG', # Capture all levels of logs from DEBUG upwards
            'class': 'logging.StreamHandler',
            'formatter': 'simple', # Use the 'simple' formatter for console output
        },
        # You could add a file handler here to log to a file
        # 'file': {
        #     'level': 'INFO',
        #     'class': 'logging.FileHandler',
        #     'filename': 'debug.log',
        #     'formatter': 'verbose',
        # },
    },
    # Loggers are the entry point to the logging system
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO', # Log Django's own messages at INFO level
            'propagate': True,
        },
        'profile_api': { # A specific logger for our app
            'handlers': ['console'],
            'level': 'DEBUG', # Log our app's messages at DEBUG level
            'propagate': False, # Don't pass these messages to the root logger
        },
    },
}







