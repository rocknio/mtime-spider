# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class MtimeItem(scrapy.Item):
    ranking = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()


class MtimePosterItem(scrapy.Item):
    id = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
