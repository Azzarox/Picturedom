"""
WSGI config for Picturedom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

application = get_wsgi_application()

from django.contrib.auth.models import User


# Used to create super user if for deploy only if not access to deployed (render) shell; 
# Could be run once to create and then rerun with commented out

# ADMIN_USERNAME='admin'
# ADMIN_EMAIL="admin@gmail.com"
# ADMIN_PASSWORD="admin"

# if not User.objects.filter(username=ADMIN_USERNAME).exists():
#     User.objects.create_superuser(username=ADMIN_USERNAME, email=ADMIN_EMAIL, password=ADMIN_PASSWORD)