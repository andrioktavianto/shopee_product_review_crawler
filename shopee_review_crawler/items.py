# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class ShopeeReviewCrawlerItem(scrapy.Item):
    item_id = Field()
    shop_id = Field()
    cat_id = Field()
    product_title = Field(serializer=str)
    rating_star = Field()
    rating_count0 = Field()
    rating_count1 = Field()
    rating_count2 = Field()
    rating_count3 = Field()
    rating_count4 = Field()
    rating_count5 = Field()
    count_rating_with_image = Field()
    count_with_context = Field()
    sold_quantity = Field()
    sold = Field()
    view_count = Field()
    author_username = Field(serializer=str)
    rating = Field()
    rating_star = Field()
    author_shopid = Field()
    userid = Field()
    comment = Field(serializer=str)
    orderid = Field()
    cmtid = Field()
    editable = Field()
    anonymous = Field()
    ctime = Field()
    mtime = Field()

class ShopeeProductCrawlerItem(scrapy.Item):
    item_id = Field()
    shop_id = Field()
    cat_id = Field()
    product_title = Field(serializer=str)
    rating_star = Field()
    rating_count0 = Field()
    rating_count1 = Field()
    rating_count2 = Field()
    rating_count3 = Field()
    rating_count4 = Field()
    rating_count5 = Field()
    count_rating_with_image = Field()
    count_with_context = Field()
    sold_quantity = Field()
    sold = Field()
    view_count = Field()
