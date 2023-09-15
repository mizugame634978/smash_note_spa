from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import os
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+)hqa4=iz91hdid8@%hn%7##$khgh^-9e515xh(vw38c#y&x@i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

MEDIA_URL = '/images/'#ブラウザからアクセスする際のアドレス
#MEDIA_URL = '/smash_proj/'
MEDIA_ROOT = BASE_DIR #画像ファイルを読み込みに行く先のフォルダ,
#↑DBのカラムのimage_urlが{images/mario.jpg}となっているので、BASE_DIRの後ろに/とフォルダ名をつけなくてもよい

INSTALLED_APPS = [
    'smash_note.apps.SmashNoteConfig',#そのままフォルダを辿ってるだけ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',#ログイン機能のためのアプリ
    'django.contrib.sites', # 追加
    'allauth', # 追加
    'allauth.account', # 追加
    'allauth.socialaccount', # 追加
    'allauth.socialaccount.providers.google', # 追加
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smash_proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'smash_proj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
#STATICFILES_DIRS = os.path.join(BASE_DIR/'static')
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build','static')#vercel

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'#追加

# グーグルログイン #
SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',#all-authニ関係なく、ユーザー名でログインする必要があります
    'allauth.account.auth_backends.AuthenticationBackend',
]
#カスタムしたUserでall-authを使う際に必要#
ACCOUNT_AUTHENTICATION_METHOD = 'email' # 認証方法をメールアドレスにする
ACCOUNT_USER_MODEL_USERNAME_FIELD = None # Userモデルにusernameは無い
ACCOUNT_EMAIL_REQUIRED = True # メールアドレスを要求する
ACCOUNT_USERNAME_REQUIRED = False# ユーザー名を要求しない

LOGIN_REDIRECT_URL = 'smash_note:character_index'#追加

#ACCOUNT_DEFAULT_HTTP_PROTOCOL='https'#これがあると逆にhttpでの通信が許可されない

SOCIALACCOUNT_PROVIDERS = {
     'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}