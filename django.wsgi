#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cvmfs_web.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
