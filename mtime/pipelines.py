# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os


class MtimePipeline(object):
    movies_info_dir_name = 'movies_info'

    def __init__(self):
        self.create_movie_base_dir()

    def create_movie_base_dir(self):
        if os.path.exists(self.movies_info_dir_name):
            return True

        os.mkdir(self.movies_info_dir_name)
        return True

    def create_movie_dir(self, dir_name):
        if dir_name is None or dir_name.strip() == "":
            return False

        if os.path.exists(self.movies_info_dir_name + '/' + dir_name):
            return True

        os.mkdir(self.movies_info_dir_name + '/' + dir_name)
        return True

    def process_item(self, item, spider):
        if spider.name == "mtime":
            if self.create_movie_dir(item['id']):
                with open('movies_info/' + item['id'] + '/' + item['id'] + '.nfo', 'w') as file:
                    movie_info = "ranking: {}, id: {}， title: {}, link: {}, directors: {}, actors: {}\n"\
                        .format(item['ranking'], item['id'], item['title'], item['link'],
                                item['directors'], item['actors'])
                    file.write(movie_info)
