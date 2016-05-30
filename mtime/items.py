# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtimeItem(scrapy.Item):
    ranking = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
