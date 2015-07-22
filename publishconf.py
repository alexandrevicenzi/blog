#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

import os
import sys

sys.path.append(os.curdir)

from pelicanconf import *

SITEURL = 'https://blog.alexandrevicenzi.com'
FAVICON = SITEURL + '/images/favicon.ico'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "alexandrevicenziblog"
GOOGLE_ANALYTICS = "UA-55543164-3"
ADD_THIS_ID = 'ra-55adbb025d4f7e55'

USE_LESS = False
