#!/usr/bin/env python
import sys
import os

#PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#zip_packages_dir = os.path.join(PROJECT_DIR, 'zip-packages')
#for zip_package in os.listdir(zip_packages_dir):
#    sys.path.insert(0, os.path.join(zip_packages_dir, zip_package))

#from google.appengine.api import memcache
#sys.modules['memcache'] = memcache

from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
