# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MtimePipeline(object):
    def __init__(self):
        self.file = open("movies.txt", "wb")

    def close_spider(self, spider):
        if spider.name == "mtime":
            self.file.close()

    def process_item(self, item, spider):
        if spider.name == "mtime":
            movie_info = "ranking: {}, title: {}, directors: {}, actors: {}\n".format(item['ranking'], item['title'],
                                                                                      item['directors'], item['actors'])
            self.file.write(movie_info.encode())
