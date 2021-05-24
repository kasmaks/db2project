# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    media = scrapy.Field()
    title = scrapy.Field()
    page_url = scrapy.Field()
    news_text = scrapy.Field()
    tags = scrapy.Field()
    date = scrapy.Field()
    part_of_day = scrapy.Field()
