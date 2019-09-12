from .dev import *

DEBUG = False
ALLOWED_HOSTS = ['www.feldman.space']
TEMPLATES[0]['DIRS'] = ['PersonalWebsite/templates/']
DATABASES['default']['NAME'] = 'PersonalWebsite/Alex_site.db'
