import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': '1592648',
        'NAME': 'students_db',
    }
}