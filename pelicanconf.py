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
PLUGINS=['assets']#,'peligram']

OUTPUT_PATH='output'
PATH = 'content'
STATIC_PATHS=['extra']

INSTAGRAM_DATA_PATH='data'
PELIGRAM_OUTPUT_MARKDOWN_DIR='blog'
PELIGRAM_OUTPUT_IMAGES_DIR='blog/images'
PELIGRAM_CATEGORY='Инстаграм'
PELIGRAM_MEDIA_PATTERNS=['*.jpg', '*.mp4']



EXTRA_PATH_METADATA={'extra/CNAME':{'path':'CNAME'},
                    'extra/css/custom.css':{'path': 'css/custom.css'}, 
                    'extra/img/hero-bg.jpg':{'path': 'img/hero-bg.jpg'}, 
                    }

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
LINKS_WIDGET_NAME='Ссылки'

OTHER_PAGES_WIDGET_NAME="Избранное"
OTHER_ARTICLES_WIDGET_NAME="Посты"

PAGINATED_TEMPLATES = {'index': 12, 'tag': 12, 'category': 6, 'author': 6}

# Social widget
SOCIAL = (('Инстаграм', 'https://www.instagram.com/anna.sutiagina'),
          )
SOCIAL_WIDGET_NAME='Социальные сети'          

DEFAULT_PAGINATION = 6

LOAD_CONTENT_CACHE=False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True