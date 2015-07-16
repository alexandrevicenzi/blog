#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Alexandre Vicenzi'
SITENAME = u"Alexandre's Blog"
SITEURL = ''
TAGLINE = 'Systems Analyst - Maker'
USER_LOGO_URL = '//alexandrevicenzi.com/img/profile.png'

THEME = './pelican-svbhack'

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True

# Blogroll
LINKS = (('About', '//alexandrevicenzi.com/'),
         ('Buteco Open Source', '//butecopensource.org/'),)

# Social widget
SOCIAL = (('Linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
          ('GitHub', 'https://github.com/alexandrevicenzi'),)

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
