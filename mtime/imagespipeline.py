# -*- coding: utf-8 -*-

import scrapy
from scrapy.pipelines.images import ImagesPipeline
# from scrapy.exceptions import DropItem


class MtimeImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item is None:
            return

        if 'image_urls' in item.keys():
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url, meta={'item': item})

    # def item_completed(self, results, item, info):
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     if not image_paths:
    #         raise DropItem("Item contains no images, id = {}".format(item['id']))
    #
    #     return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_uuid = request.url.split('/')[-1]
        filename = 'movies_info/{}/{}'.format(item['title'].strip('x\a0'), image_uuid)
        return filename
