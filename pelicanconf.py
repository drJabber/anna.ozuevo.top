#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.insert(0,'./annatheme')
import annatheme


# DELETE_OUTPUT_DIRECTORY=True

AUTHOR = 'dJabber'
SITENAME = 'Анна. Домашний кондитер'

CONTACTS_PERSON='Анна'
CONTACTS_PHONE='+7(926)220-1610'
CONTACTS_ADDRESS='Орехово-Зуево'
CUSTOM_KEYWORDS=' Анна Торты Капкейки Трайфлы Кондитер Кэнди-бар Орехово-Зуево'

THEME=annatheme.PATH
JINJA_ENVIRONMENT=annatheme.ENVIRONMENT
JINJA_FILTERS=annatheme.FILTERS
# DISPLAY_CATEGORIES_ON_MENU=True

LOCALE='ru_RU.utf8'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ru': '%a, %d %B %Y',
    'ru_RU.utf8': '%a, %d %B %Y',
}


PLUGIN_PATHS=['plugins','pelican-plugins']
PLUGINS=['assets','amtag_cloud','sitemap','thumbnailer','jinja2content','peligram','pelican_extra']

OUTPUT_PATH='output'
PATH = 'content'
STATIC_PATHS=['extra']

INSTAGRAM_DATA_PATH='data'
PELIGRAM_OUTPUT_MARKDOWN_DIR='blog'
PELIGRAM_OUTPUT_IMAGES_DIR='blog/images'
PELIGRAM_CATEGORY='Инстаграм'
PELIGRAM_MEDIA_PATTERNS=['*.jpg', '*.mp4']

IMAGE_PATH='blog/images'
THUMBNAIL_DIR='img/thumbs'
THUMBNAIL_SIZES = {
    'tnsq': '100',
    'tnwd': '100x?',
    'tntl': '?x100',
}


EXTRA_DIRECTORIES={
    'extra/fonts/gotham':{'path':'fonts'}, 
    'extra/fonts/circe':{'path':'fonts'}, 
}

EXTRA_PATH_METADATA={'extra/CNAME':{'path':'CNAME'},
                    'extra/robots.txt':{'path':'robots.txt'},
                    'extra/css/custom.css':{'path': 'css/custom.css'}, 
                    'extra/img/favicon.ico':{'path': 'favicon.ico'}, 
                    'extra/img/banner-005.jpg':{'path': 'img/banner-005.jpg'}, 
                    'extra/img/banner-006.jpg':{'path': 'img/banner-006.jpg'}, 
                    'extra/img/banner-011.png':{'path': 'img/banner-011.png'}, 
                    'extra/img/hero-bg.jpg':{'path': 'img/hero-bg.jpg'}, 
                    'extra/img/main-bg-001.jpg':{'path': 'img/main-bg-001.jpg'}, 
                    'extra/img/main-bg-002.jpg':{'path': 'img/main-bg-002.jpg'}, 
                    'extra/img/main-bg-003.jpg':{'path': 'img/main-bg-003.jpg'}, 
                    'extra/img/main-bg-004.jpg':{'path': 'img/main-bg-004.jpg'}, 
                    'extra/js/amtag_cloud.js':{'path': 'js/amtag_cloud.js'}, 
                    }

ARTICLE_PATHS=['blog']
PAGE_PATHS=['pages','menu','other']
ARTICLE_SAVE_AS='articles/{date:%Y}/{slug}.html'
ARTICLE_URL='articles/{date:%Y}/{slug}.html'
#ARTICLE_SAVE_AS='articles/{slug}.html'
#ARTICLE_URL='articles/{slug}.html'

HEADER_COVER='static/img/cover.jpg'

TIMEZONE = 'Europe/Moscow'
SITEURL=''


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
    # 'extensions':['markdown.extensions.codehilite','markdown.extensions.extra','markdown.extensions.meta','md_video'],
    'extension_configs': {
        'codehilite': {'css_class': 'highlight'},
        'meta': {},
        'extra': {},
        'md_video':{},
    },
    'output_format': 'html5',
}

MENUITEMS = [('Заказать','pages/order.html')]


YANDEX_METRICA=54428389
YANDEX_VERIFICATION='b6a6b827587b30e8'
GOOGLE_ANALYTICS = "UA-143756815-1"
GOOGLE_VERIFICATION_META='bx7hlv70iBp8SsKAqjSo4swTvC1iIaUir7rXQPGNCSs'

META_DESCRIPTION='Сайт о домашней кондитерской Анны в г.Орехово-Зуево Московской области'

