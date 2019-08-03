from feedgenerator import Rss201rev2Feed
import logging
logger = logging.getLogger(__name__)

class YandexTurboRssFeed(Rss201rev2Feed):
    def __init__(self, *args, **kwargs):
        super(Rss201rev2Feed, self).__init__(*args, **kwargs)

    def set_settings(self, settings):
        self.settings = settings

    def rss_attributes(self):
        return {'version': self._version, 
                'xmlns:yandex':'http://news.yandex.ru', 
                'xmlns:media':'http://search.yahoo.com/mrss/',
                'xmlns:turbo':'http://turbo.yandex.ru',
                }

    def item_attributes(self,item):
        return {'turbo':'true'}


    def add_root_elements(self, handler):
        super(YandexTurboRssFeed,self).add_root_elements(handler)

        if self.feed['yandex_turbo_analytics'] is not None:
            handler.addQuickElement("turbo:analytics", '',{'type':'Yandex','id':self.feed['yandex_turbo_analytics']})

        if self.feed['google_turbo_analytics'] is not None:
            handler.addQuickElement("turbo:analytics", '',{'type':'Google','id':self.feed['google_turbo_analytics']})

    def add_item_elements(self, handler, item):
        super(YandexTurboRssFeed,self).add_item_elements(handler,item)

        if item['turbo_content'] is not None:
            handler.startElement("turbo:content",{})
            handler.ignorableWhitespace(item['turbo_content'])
            handler.endElement("turbo:content")


