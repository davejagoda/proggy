#!/usr/bin/env python
'''
you will need to do all (or most) of the following to get this to work:
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=<APPNAME>.settings
export PGUSER=<USERNAME>
export PGPASSWORD=<PASSWORD>
export PGHOST=<HOSTNAME>
'''
import django
django.setup()

for m in django.apps.apps.get_models():
    print(('{}:{}'.format(m.__name__,m.objects.count())))
