# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HfUsercrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    user_meta = scrapy.Field()
    team = scrapy.Field()
    follower_amount = scrapy.Field()
    following_meta = scrapy.Field()
    following_amount = scrapy.Field()
    following_meta = scrapy.Field()
    pass
