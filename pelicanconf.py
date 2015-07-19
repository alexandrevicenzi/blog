#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

SITEURL = 'http://localhost:8000'
SITENAME = u"Alexandre Vicenzi's Blog"
AUTHOR = u'Alexandre Vicenzi'
AUTHOR_SHORT_DESC = 'Web Developer - Maker'
AUTHOR_IMG_URL = '//alexandrevicenzi.com/img/profile.png'

THEME = '../flex'
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'en'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

LINKS = (('Portfolio', '//alexandrevicenzi.com'),)

SOCIAL = (('linkedin', 'https://br.linkedin.com/in/alexandrevicenzi/en'),
          ('github', 'https://github.com/alexandrevicenzi'),
          ('google', 'https://google.com/+AlexandreVicenzi'),
          ('rss', '//blog.alexandrevicenzi.com/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2015

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

STATUSCAKE = {
    'trackid': 'SL0UAgrsYP',
    'days': 7
}

USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
