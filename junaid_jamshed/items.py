# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import pathlib

class JunaidJamshedItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field()
     price = scrapy.Field()
     availability = scrapy.Field()

    
