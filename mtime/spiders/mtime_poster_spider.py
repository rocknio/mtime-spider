# -*- coding: utf-8 -*-
import scrapy
import os
import re
import json
from mtime.items import MtimePosterItem


class MtimePosterSpider(scrapy.Spider):
    name = "mtime_poster"
    movies_info_dir_name = 'movies_info'
    allowed_domains = ["mtime.com", "mtime.cn"]
    start_urls = []

    def __init__(self):
        super(MtimePosterSpider, self).__init__()
        for lists in os.listdir(self.movies_info_dir_name):
            path = os.path.join(self.movies_info_dir_name, lists)
            if os.path.isdir(path):
                self.start_urls.append('http://movie.mtime.com/{}/posters_and_images/posters/hot.html'.format(lists))

    def parse(self, response):
        if response.status != 200:
            return

        # 解析返回的html
        str_resp = response.body.decode("utf-8")
        posters = re.compile('\{"poster":\[\{"generalposter":(.*)}]},{"forecastposter"').findall(str_resp)
        if posters.__len__() == 0:
            # 没有图片，退出
            return

        posters_json_str = posters[0] + "}]"
        posters_list = json.loads(posters_json_str)

        image_urls = []
        for one_poster in posters_list:
            image_url = one_poster['img_1000']
            image_urls.append(image_url)

        mtime_poster_item = MtimePosterItem()
        mtime_poster_item['image_urls'] = image_urls
        yield mtime_poster_item
