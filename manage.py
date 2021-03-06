#!/usr/bin/env python
from os.path import abspath, dirname, join
from site import addsitedir
import sys

# updating python sys path to include project applications.
sys.path.insert(0, abspath(join(dirname(__file__), 'external_libs')))
sys.path.insert(0, abspath(join(dirname(__file__), 'libs')))
from django.core.management import execute_manager
try:
    import vimeo_assignment.settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(vimeo_assignment.settings)