#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.insert(0,'./annatheme')
import annatheme


DELETE_OUTPUT_DIRECTORY=True

AUTHOR = 'dJabber'
SITENAME = 'AnnaBake'
THEME=annatheme.PATH
JINJA_ENVIRONMENT=annatheme.ENVIRONMENT
JINJA_FILTERS=annatheme.FILTERS

PLUGIN_PATHS=['plugins','pelican-plugins']
PLUGINS=['assets','amtag_cloud']#,'peligram']

OUTPUT_PATH='output'
PATH = 'content'
STATIC_PATHS=['extra']
# SITEURL='/'

INSTAGRAM_DATA_PATH='data'
PELIGRAM_OUTPUT_MARKDOWN_DIR='blog'
PELIGRAM_OUTPUT_IMAGES_DIR='blog/images'
PELIGRAM_CATEGORY='Инстаграм'
PELIGRAM_MEDIA_PATTERNS=['*.jpg', '*.mp4']



EXTRA_PATH_METADATA={'extra/CNAME':{'path':'CNAME'},
                    'extra/css/custom.css':{'path': 'css/custom.css'}, 
                    'extra/img/hero-bg.jpg':{'path': 'img/hero-bg.jpg'}, 
                    'extra/js/amtag_cloud.js':{'path': 'js/amtag_cloud.js'}, 
                    }

ARTICLE_PATHS=['blog']
ARTICLE_SAVE_AS='articles/{date:%Y}/{slug}.html'
ARTICLE_URL='articles/{date:%Y}/{slug}.html'
#ARTICLE_SAVE_AS='articles/{slug}.html'
#ARTICLE_URL='articles/{slug}.html'

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


# Social widget
SOCIAL = (('Инстаграм', 'https://www.instagram.com/anna.sutiagina'),
          )
SOCIAL_WIDGET_NAME='Социальные сети'          

#pagination config
PAGINATED_TEMPLATES = {'index': 12, 'tag': 12, 'category': 6, 'author': 6}
DEFAULT_PAGINATION = 6

LOAD_CONTENT_CACHE=False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


#tag cloud plugin config
AMTAG_CLOUD=True
AMTAG_CLOUD_MAX_ITEMS=50 #number of different tags that can appear in tag cloud


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'md_video':{},
    },
    'output_format': 'html5',
}
