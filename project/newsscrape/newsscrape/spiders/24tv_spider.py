from newsscrape.spiders.news_spider import NewsSpider
from datetime import datetime


class TwentyFourTvSpider(NewsSpider):
    name = "TwentyFourTvSpider"
    allowed_domains = ["24tv.ua"]
    start_urls = ["https://24tv.ua/"]

    media = "24tv"
    get_links_pattern = '//ul[contains(@class, "clear-list") and contains(@class, "news-list")]//li//a/@href'
    get_title_pattern = '//h1[contains(@class, "article-title")]/text()'
    get_news_text_pattern = '//div[contains(@class, "news-text-wrap")]//p[not (contains(@class, "read-also"))]//text() | ' \
                            '//div[contains(@class, "news-text-wrap")]//li//text() | ' \
                            '//div[contains(@class, "news-text-wrap")]//a[not (contains(@class, "more-link"))]//text()'
    get_tags_pattern = '//nav[@class="tags-item-list"]//a/text()'
    get_date_pattern = '//div[contains(@class, "top-news-info")]//time//span//text()'

    def parse_date(self, date):

        d = date.split()
        time = d[-1].split(":")
        month = datetime.now().month
        if month < 10:
            month = "0%s" % month
        year = datetime.now().year
        day = d[0]
        hours = time[0]
        mins = time[1]
        return '%s-%s-%sT%s:%s:00+03:00' % (year, month, day, hours, mins)
