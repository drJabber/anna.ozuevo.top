import os 
import os.path as path
import shutil
import time
import re
import json
from jinja2 import Markup
from pelican import signals
from pelican.writers import Writer
from pelican.generators import ArticlesGenerator
from pelican.utils import (get_relative_path, is_selected_for_writing,
                           path_to_url, sanitised_join, set_date_tzinfo,order_content)
from .yafeedgenerator import YandexTurboRssFeed
from feedgenerator import get_tag_uri

import logging
logger = logging.getLogger(__name__)

try:
#import libraries here
    enabled = True
except ImportError:
    logging.warning("Unable to load libraries, disabling yafeed")
    enabled = False

class YaWriter(Writer):
    def __init__(self, *args, **kwargs):
        """Class initializer"""
        super(YaWriter, self).__init__(*args, **kwargs)

    def _create_new_feed(self, *args):
        """Helper function (called by the super Writer class) which will initialize
        the YaFeed object."""     
        if len(args) == 2:
            # we are on pelican <2.7
            feed_type, context = args
        elif len(args) == 3:
            # we are on Pelican >=2.7
            feed_type, feed_title, context = args
        else:
            # this is not expected, let's provide a useful message
            raise Exception(
                'The Writer._create_new_feed signature has changed, check the '
                'current Pelican source for the updated signature'
            )     

        self.context = context      

        if feed_title:
            feed_title = context['SITENAME'] + ' - ' + feed_title
        else:
            feed_title = context['SITENAME']

        feed=YandexTurboRssFeed(
            title=Markup(feed_title).striptags(),
            link=("{0}/".format(self.site_url)),
            feed_url=self.feed_url,
            description=context.get('SITESUBTITLE', ''),
            subtitle=context.get('SITESUBTITLE', None),
            yandex_turbo_analytics=str(context.get('YANDEX_METRICA',0)),
            google_turbo_analytics=context.get('GOOGLE_ANALYTICS','')
            )
        
        feed.set_settings(self.settings)

        return feed    

    def _add_item_to_the_feed(self, feed, item):
        title = Markup(item.title).striptags()
        link = self.urljoiner(self.site_url, item.url)

        description = item.summary

        feed.add_item(
            title=title,
            link=link,
            unique_id=get_tag_uri(link, item.date),
            description=description,
            turbo_content="<![CDATA[{}]]>".format(item.get_content(self.site_url)),
            categories=item.tags if hasattr(item, 'tags') else None,
            author_name=getattr(item, 'author', ''),
            pubdate=set_date_tzinfo(
                item.date, self.settings.get('TIMEZONE', None)),
            updateddate=set_date_tzinfo(
                item.modified, self.settings.get('TIMEZONE', None)
                ) if hasattr(item, 'modified') else None        
        )

class YaFeedGenerator(ArticlesGenerator):

    def generate_yafeeds(self, writer):
        """Generate the feeds from the current context, and output files."""

        if self.settings.get('YA_FEED_RSS'):
            writer.write_feed(
                self.articles,
                self.context,
                self.settings['YA_FEED_RSS'],
                self.settings.get('YA_FEED_RSS_URL', self.settings['YA_FEED_RSS']),
                feed_type='rss'
                )

        if (self.settings.get('YA_FEED_ALL_RSS')):
            all_articles = list(self.articles)
            order_content(all_articles,
                          order_by=self.settings['ARTICLE_ORDER_BY'])

            if self.settings.get('YA_FEED_ALL_RSS'):
                writer.write_feed(
                    all_articles,
                    self.context,
                    self.settings['YA_FEED_ALL_RSS'],
                    self.settings.get('YA_FEED_ALL_RSS_URL',self.settings['YA_FEED_ALL_RSS']),
                    feed_type='rss'
                    )

        for cat, arts in self.categories:
            if self.settings.get('YA_CATEGORY_FEED_RSS'):
                writer.write_feed(
                    arts,
                    self.context,
                    self.settings['YA_CATEGORY_FEED_RSS'].format(slug=cat.slug),
                    self.settings.get('CATEGORY_FEED_RSS_URL',self.settings['YA_CATEGORY_FEED_RSS']).format(slug=cat.slug),
                    feed_title=cat.name,
                    feed_type='rss'
                    )

        for auth, arts in self.authors:
            if self.settings.get('YA_AUTHOR_FEED_RSS'):
                writer.write_feed(
                    arts,
                    self.context,
                    self.settings['YA_AUTHOR_FEED_RSS'].format(slug=auth.slug),
                    self.settings.get('YA_AUTHOR_FEED_RSS_URL',self.settings['YA_AUTHOR_FEED_RSS']).format(slug=auth.slug),
                    feed_title=auth.name,
                    feed_type='rss'
                    )

        if (self.settings.get('YA_TAG_FEED_RSS') ):
            for tag, arts in self.tags.items():
                if self.settings.get('YA_TAG_FEED_RSS'):
                    writer.write_feed(
                        arts,
                        self.context,
                        self.settings['YA_TAG_FEED_RSS'].format(slug=tag.slug),
                        self.settings.get('YA_TAG_FEED_RSS_URL',self.settings['YA_TAG_FEED_RSS']).format(slug=tag.slug),
                        feed_title=tag.name,
                        feed_type='rss'
                        )


    def generate_output(self, writer):
        writer=YaWriter(self.output_path,self.settings)
        self.generate_yafeeds(writer)

def get_generators(generators):
    """Module function invoked by the signal 'get_generators'."""
    return YaFeedGenerator


def register():
    """Registers the module function `get_generators`."""
    signals.get_generators.connect(get_generators)        
