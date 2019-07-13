#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

PLUGINS=['assets','amtag_cloud','sitemap','peligram','thumbnailer']

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://anna.ozuevo.top'
RELATIVE_URLS = False

YANDEX_METRICA=54428389
YANDEX_VERIFICATION='b6a6b827587b30e8'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-143756815-1"

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
