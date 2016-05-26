# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from mtime.items import MtimeItem
from mtime.spiders.mtime_wallpapers_spider import MtimeWallpaperSpider


class MtimeSpider(scrapy.Spider):
    name = "mtime"
    allowed_domains = ["mtime.com"]
    start_urls = ["http://www.mtime.com/hotest/", ]

    def parse(self, response):
        if response.status != 200:
            return

        # 解析返回的html
        soup = BeautifulSoup(response.body, "lxml")

        # 获取本页的电影信息html列表
        movies_node = soup.findAll(attrs={"class": "mtiplist"})

        # 解析每一个电影的内容
        i = 1
        for movie in movies_node:
            if i <= 3:
                tag1 = "num n0{}".format(i)
            else:
                tag1 = ""

            tag2 = "num"
            # 前三名 class 名称不一致，现判断前三名，获取不到，获取其他排名的数据
            try:
                ranking = int(movie.find(attrs={"class": tag1}).contents[0])
            except Exception:
                ranking = int(movie.find(attrs={"class": tag2}).contents[0])

            title_info = movie.find("dl").find("dt").find("a")

            title = title_info.contents[0].strip()
            link = title_info["href"]
            director_content = movie.find("dl").findAll("li")[0].find('a').contents[0].strip()
            actors_list = [actor.contents[0].strip() for actor in
                           movie.find("dl").findAll("li")[1].findAll('a')]

            i += 1

            movie_info_item = MtimeItem()
            movie_info_item['title'] = title
            movie_info_item['id'] = link.split('/')[-2]
            movie_info_item['link'] = link
            movie_info_item['ranking'] = ranking
            movie_info_item['directors'] = director_content
            movie_info_item['actors'] = actors_list
            yield movie_info_item

        # 处理下一页的情况
        next_page = soup.find(id='key_nextpage')
        if next_page is not None:
            url = response.urljoin(next_page['href'])
            yield scrapy.Request(url, self.parse)
