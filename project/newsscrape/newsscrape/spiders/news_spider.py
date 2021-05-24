import scrapy
from newsscrape.items import NewsItem
from datetime import datetime


def get_part_of_day_from_hour(hour):
    if hour <= 12:
        return "morning"
    if hour <= 17:
        return "afternoon"
    if hour <= 20:
        return "evening"
    return "night"


class NewsSpider(scrapy.Spider):
    name = "NewsSpider"
    allowed_domains = [""]
    start_urls = [""]

    media = ""
    get_links_pattern = ""
    get_title_pattern = ""
    get_news_text_pattern = ""
    get_tags_pattern = ""
    get_date_pattern = ""

    def parse_date(self, date):
        return date

    def get_part_of_day_from_date(self, date):
        hour = datetime.fromisoformat(date).hour
        return get_part_of_day_from_hour(hour)

    def parse_news_page(self, response):
        news_item = NewsItem()
        news_item["media"] = self.media
        news_item["title"] = response.xpath(self.get_title_pattern).extract()[0].strip()
        news_item['page_url'] = response.request.url
        news_item['news_text'] = ""
        news_item["tags"] = []
        date = ""
        for t in response.xpath(self.get_date_pattern).extract():
            date += t
        news_item["date"] = date

        for text in response.xpath(self.get_news_text_pattern):
            if len(text.extract().strip()) > 0:
                news_item['news_text'] += " " + (text.extract().strip())
        for tag in response.xpath(self.get_tags_pattern):
            news_item["tags"].append(tag.extract())
        # change date
        news_item["date"] = self.parse_date(news_item["date"])
        # get part of the day
        news_item["part_of_day"] = self.get_part_of_day_from_date(news_item["date"])
        return news_item

    def parse(self, response, **kwargs):
        for link in response.xpath(self.get_links_pattern):
            link = link.extract()
            if link.startswith("https://") is False:
                link = self.start_urls[0] + link
            print(link)
            request = scrapy.Request(link, callback=self.parse_news_page)
            yield request
