from newsscrape.spiders.news_spider import NewsSpider
from datetime import datetime


class UkrPravdaSpider(NewsSpider):
    name = "UkrPravdaSpider"
    allowed_domains = ["pravda.com.ua"]
    start_urls = ["https://www.pravda.com.ua"]

    media = "UkrPravda"
    get_links_pattern = '//div[contains(@class, "container_sub_news_wrapper")]' \
                        '//div[contains(@class, "article_header")]//a/@href'

    get_title_pattern = '//article//h1[contains(@class, "post_title")]/text()'
    get_news_text_pattern = '//div[contains(@class, "post_text")]//p//text()'
    get_tags_pattern = '//div[contains(@class, "post_tags")]//a//text()'
    get_date_pattern = '//div[contains(@class, "post_time")]/text()'

    def parse_date(self, date):
        d = date.split()
        time = d[-1].split(":")
        month = datetime.now().month
        if month < 10:
            month = "0%s" % month
        year = datetime.now().year
        day = d[1]
        hours = time[0]
        mins = time[1]
        return '%s-%s-%sT%s:%s:00+03:00' % (year, month, day, hours, mins)

