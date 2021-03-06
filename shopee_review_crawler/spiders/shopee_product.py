# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from shopee_review_crawler.items import ShopeeProductCrawlerItem

class ShopeeProductSpider(scrapy.Spider):
    name = "shopee_product"
    allowed_domains = ['shopee.co.id']

    # Variable setting
    keywords_ = "skin care";

    BASE_URL = r"https://shopee.co.id/api/v2/search_items/?by=relevancy&keyword={keywords}&limit=50&newest={start}&order=desc&page_type=search&version=2"
    start_urls = [BASE_URL.format(keywords=keywords_, start=0)]

    def parse(self, response):
        return self.parse_search(response=response)

    def parse_search(self, response):
        items = json.loads(response.body_as_unicode())
        total_data = 200 #total_data = items['total_count']
        self.logger.debug('Jumlah data: ' + str(total_data))
        total_pages = int(round(total_data / 50.0))

        for item in items['items']:
            product = ShopeeProductCrawlerItem()
            product['item_id'] = item['itemid']
            product['shop_id'] = item['shopid']
            product['cat_id'] = item['catid']
            product['product_title'] = item['name']
            product['rating_star'] = item['item_rating']['rating_star']
            product['rating_count0'] = item['item_rating']['rating_count'][0]
            product['rating_count1'] = item['item_rating']['rating_count'][1]
            product['rating_count2'] = item['item_rating']['rating_count'][2]
            product['rating_count3'] = item['item_rating']['rating_count'][3]
            product['rating_count4'] = item['item_rating']['rating_count'][4]
            product['rating_count5'] = item['item_rating']['rating_count'][5]
            product['count_rating_with_image'] = item['item_rating']['rcount_with_image']
            product['count_with_context'] = item['item_rating']['rcount_with_context']
            product['sold_quantity'] = item['historical_sold']
            product['sold'] = item['sold']
            product['view_count'] = item['view_count']
            yield product

        for i in range(1, total_pages + 1):
        	self.logger.debug('SCRAPING HALAMAN-' + str(i))
        	yield Request(self.BASE_URL.format(keywords=self.keywords_, start=i*50), callback=self.parse_search)