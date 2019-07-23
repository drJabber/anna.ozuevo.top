''' 
tag_cloud
===================================

This plugin generates a tag cloud from available tags
'''
from __future__ import unicode_literals

from collections import defaultdict
from operator import itemgetter

import logging
import math
import random

from pelican import signals

logger = logging.getLogger(__name__)


def set_default_settings(settings):
    settings.setdefault('AMTAG_CLOUD_MAX_ITEMS', 100)


def init_default_config(pelican):
    from pelican.settings import DEFAULT_CONFIG
    set_default_settings(DEFAULT_CONFIG)
    if pelican:
        set_default_settings(pelican.settings)


def generate_tag_cloud(generator):
    tag_cloud = defaultdict(int)
    for article in generator.articles:
        for tag in getattr(article, 'tags', []):
            tag_cloud[tag] += 1

    tag_cloud = sorted(tag_cloud.items(), key=itemgetter(1))#sort list of tuples (tag,count) by count 
    tag_cloud=list(map(lambda e: (e[1][0],e[1][1], e[0]*e[0]*e[0]), enumerate(tag_cloud)))#make list of tuples (tag,count,index)
    # logger.debug(f"{len(tag_cloud)}")

    tag_cloud = tag_cloud[len(tag_cloud):len(tag_cloud)-min(generator.settings.get('AMTAG_CLOUD_MAX_ITEMS')-1,len(tag_cloud)):-1]#slice MAX_ITMES elements
    
    # logger.debug(f"{len(tag_cloud)}  of {generator.settings.get('AMTAG_CLOUD_MAX_ITEMS')}")

    #generate list of dicts (tag, count, index) to create json in html
    def generate_am_tag(tag, count,index):
        logger.debug(f"{tag.name}, {count}, {index}")
        return {"tag":tag.name, "count":count, "index":index, "url":tag.url} 

    tag_cloud = [
        generate_am_tag(tag, count, index)
        for tag, count,index in tag_cloud
    ]

    generator.tag_cloud = tag_cloud
    generator._update_context(['tag_cloud'])


def register():
    signals.initialized.connect(init_default_config)
    signals.article_generator_finalized.connect(generate_tag_cloud)
