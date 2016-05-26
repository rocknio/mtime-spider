# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class MtimeWallpaperSpider(scrapy.Spider):
    name = "mtime_wallpapers"
    allowed_domains = ["mtime.com", "mtime.cn"]
    start_urls = []

    def add_url(self, url):
        if url is None or url.strip() == "":
            return

        self.start_urls.append(url)

    def reset_urls(self):
        self.start_urls.clear()

    def start_crawl(self):
        if self.start_urls is not None:
            self.start_requests()

    def parse(self, response):
        if response.status != 200:
            return

        # 解析返回的html
        soup = BeautifulSoup(response.body, "lxml")
        wallpaper_list = soup.findAll('script', id='desktop')
        print(wallpaper_list)
