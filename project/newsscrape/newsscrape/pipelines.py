# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class NewsPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient("localhost", 50000)
        db = self.conn["MyDb"]
        self.data_coll = db['news']

    def insert(self, news_item):
        print("Before insertion")
        self.data_coll.insert_one({"media": news_item["media"],
                                   "title": news_item["title"],
                                   "page_url": news_item["page_url"],
                                   "news_text": news_item["news_text"],
                                   "tags": news_item["tags"],
                                   "date": news_item["date"],
                                   "part_of_day": news_item["part_of_day"]})
        print("After insertion")

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.insert(item)
        return item

