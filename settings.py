# Django settings for schlief project.
import os

DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Vadim Chernysh', 'chernysh.vadim@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(DIRNAME, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(DIRNAME, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(DIRNAME, 'webstatic'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)
# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ixo1m_^x31rc6sckr0f-57=h=&5%3zkhm!mgs9p@8_z0xix#tx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(DIRNAME, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',
    'annoying',
    'tinymce',
    'filebrowser',
    'uploadify',

    'api',
    'portfolio',
    'blog',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#TinyMCE widget configuration
TINYMCE_JS_URL = "/static/tiny_mce/tiny_mce.js"
TINYMCE_JS_ROOT = STATIC_ROOT + "/tiny_mce"
TINYMCE_SPELLCHECKER=False
TINYMCE_PLUGINS = [
    'safari',
    'table',
    'advlink',
    'advimage',
    'iespell',
    'inlinepopups',
    'media',
    'searchreplace',
    'contextmenu',
    'paste',
    'wordcount']

TINYMCE_DEFAULT_CONFIG={
    'theme': "advanced",
    'plugins': ",".join(TINYMCE_PLUGINS), # django-cms

    'language': 'ru',
    'theme_advanced_buttons1': "bullist,numlist,|,link,unlink,anchor,image",
    'theme_advanced_buttons3': "table,|,delete_row,delete_table,|,row_after,row_before",
    'theme_advanced_buttons4': "styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "cut,copy,paste,pastetext,pasteword,|,search,replace,|,undo,redo,|,link,unlink,cleanup",
    'theme_advanced_buttons4': "",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'table_default_cellpadding': 2,
    'table_default_cellspacing': 2,
    'cleanup_on_startup': False,
    'cleanup': False,
    'paste_auto_cleanup_on_paste': False,
    'paste_block_drop': False,
    'paste_remove_spans': False,
    'paste_strip_class_attributes': False,
    'paste_retain_style_properties': "",
    'forced_root_block': False,
    'force_br_newlines': False,
    'force_p_newlines': False,
    'remove_linebreaks': False,
    'convert_newlines_to_brs': False,
    'inline_styles': False,
    'relative_urls': False,
    'formats': {
        'alignleft': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes': 'align-left'},
        'aligncenter': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes': 'align-center'},
        'alignright': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes': 'align-right'},
        'alignfull': {'selector': 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes': 'align-justify'},
        'strikethrough': {'inline': 'del'},
        'italic': {'inline': 'em'},
        'bold': {'inline': 'strong'},
        'underline': {'inline': 'u'}},
    'pagebreak_separator': ""}

#FILEBROWSER_URL_FILEBROWSER_MEDIA = STATIC_URL + 'filebrowser'
FILEBROWSER_DIRECTORY = 'filebrowser'

try:
    from local_settings import *
except ImportError:
    pass
