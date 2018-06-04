#!/usr/bin/env python3
'''
you will need to do all (or most) of the following to get this to work:
export PGUSER=<USERNAME>
export PGPASSWORD=<PASSWORD>
export PGHOST=<HOSTNAME>
export DJANGO_SETTINGS_MODULE=<APPNAME>.settings
pipenv run ./django_count_all_objects_in_all_models.py
'''
import django
django.setup()

for m in django.apps.apps.get_models():
    print('{}:{}'.format(m.__name__,m.objects.count()))
