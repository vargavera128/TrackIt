# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class OpenFoodItem(scrapy.Item):
    item_name = scrapy.Field()
    image_url = scrapy.Field()
