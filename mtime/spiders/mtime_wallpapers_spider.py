# -*- coding: utf-8 -*-
import scrapy
import os
import re
import json


class MtimeWallpaperSpider(scrapy.Spider):
    name = "mtime_wallpapers"
    movies_info_dir_name = 'movies_info'
    allowed_domains = ["mtime.com", "mtime.cn"]
    start_urls = []

    def __init__(self):
        super(MtimeWallpaperSpider, self).__init__()
        for lists in os.listdir(self.movies_info_dir_name):
            path = os.path.join(self.movies_info_dir_name, lists)
            if os.path.isdir(path):
                self.start_urls.append('http://movie.mtime.com/{}/posters_and_images/wallpapers/hot.html'.format(lists))

    def parse(self, response):
        if response.status != 200:
            return

        # 解析返回的html
        str_resp = response.body.decode("utf-8")
        wallpapers = re.compile('\{"desktop":(.*)}]}]},').findall(str_resp)
        if wallpapers.__len__() == 0:
            # 没有桌面图片，退出
            return

        wallpapers_json_str = wallpapers[0] + "}]}]"
        wallpapers_json = json.loads(wallpapers_json_str)
        wallpapers_list = wallpapers_json[0]['all']

        for one_wallpaper in wallpapers_list:
            image_url = one_wallpaper['img_1000']
            print(image_url)
