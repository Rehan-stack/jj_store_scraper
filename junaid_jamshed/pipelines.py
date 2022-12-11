# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from store_scraper.models import j_clothes

import logging, coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)

class JunaidJamshedPipeline:
    def process_item(self, item, spider):
        try:
            j_clothes.objects.create(name=item['name'], price=item['price'])
            print("\n")
            logger.warn("Loaded name {}".format(item['name']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error("\nFailed to load name, Reason For Failure:{}".format(e))
            print(item)
        return item
    
