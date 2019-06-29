#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bulrush

AUTHOR = 'dJabber'
SITENAME = 'AnnaBake'
THEME=bulrush.PATH
JINJA_ENVIRONMENT=bulrush.ENVIRONMENT
JINJA_FILTERS=bulrush.FILTERS

PLUGIN_PATHS=['../pelican-plugins']
PLUGINS=['assets']

PATH = 'content'

TIMEZONE = 'Europe/Moscow'
SITEURL='https://anna.ozuevo.top'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

LOAD_CONTENT_CACHE=False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True