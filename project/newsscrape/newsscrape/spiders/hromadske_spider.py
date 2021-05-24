from newsscrape.spiders.news_spider import NewsSpider
from datetime import datetime


class HromadskeSpider(NewsSpider):
    name = "HromadskeSpider"
    allowed_domains = ["hromadske.ua"]
    start_urls = ["https://hromadske.ua"]

    media = "Hromadske"
    get_links_pattern = '//*[@class="NewsBlock-news"]//a/@href'
    get_title_pattern = '//h1[contains(@class, "PostHeader-title")]/text()'
    get_news_text_pattern = '//div[contains(@class, "PostContent-leadText")]//text() | ' \
                            '//div[contains(@class, "PostPublication")]//p//text()'
    get_tags_pattern = '//a[contains(@class, "TagButton")]//div/text()'

    get_date_pattern = '//div[contains(@class, "PostHeader-published")]/text()'

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
