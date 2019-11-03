#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

LOAD_CONTENT_CACHE=True

PLUGINS=['assets','amtag_cloud','sitemap','peligram','jinja2content','thumbnailer','yafeeds_plugin']

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://anna.ozuevo.top'
RELATIVE_URLS = False

YANDEX_METRICA=54428389
YANDEX_VERIFICATION='b6a6b827587b30e8'
GOOGLE_ANALYTICS = "UA-143756815-1"

# FEED_DOMAIN=SITEURL
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_RSS='feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
# CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
# TAG_FEED_RSS = 'feeds/tag_{slug}.rss.xml'
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

FEED_DOMAIN=SITEURL
YA_FEED_ALL_RSS='yafeeds/all.rss.xml'
YA_CATEGORY_FEED_RSS = 'yafeeds/{slug}.rss.xml'
YA_TAG_FEED_RSS = 'yafeeds/tag_{slug}.rss.xml'
YA_AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}


