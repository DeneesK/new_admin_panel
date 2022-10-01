import os
from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include

# Loading environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connecting components containing settings
include('components/database.py',
        'components/templates.py',
        'components/passwordvalidation.py',
        'components/installed_apps.py',
        'components/middlewares.py',
        )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '192.168.0.185']

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Collect for translation
LOCALE_PATHS = ['movies/locale']
