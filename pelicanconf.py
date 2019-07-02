#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bulrush

AUTHOR = 'dJabber'
SITENAME = 'AnnaBake'
THEME=bulrush.PATH
JINJA_ENVIRONMENT=bulrush.ENVIRONMENT
JINJA_FILTERS=bulrush.FILTERS

PLUGIN_PATHS=['pelican-plugins','../pelican-plugins']
PLUGINS=['assets','peligram']

OUTPUT_PATH='output'
PATH = 'content'
STATIC_PATHS=['static','extra/CNAME']
INSTAGRAM_DATA_PATH='data'
PELIGRAM_OUTPUT_MARKDOWN_DIR='blog'
PELIGRAM_OUTPUT_IMAGES_DIR='blog/images'
PELIGRAM_CATEGORY='Instagram'
PELIGRAM_MEDIA_PATTERNS=['*.jpg', '*.mp4']



EXTRA_PATH_METADATA={'extra/CNAME':{'path':'CNAME'}}

ARTICLE_PATHS=['blog']
ARTICLE_SAVE_AS='{date:%Y}/{slug}.html'
ARTICLE_URL='{date:%Y}/{slug}.html'

HEADER_COVER='static/img/cover.jpg'

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