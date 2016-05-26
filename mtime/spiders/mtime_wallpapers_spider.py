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

    def parse(self, response):
        if response.status != 200:
            return

