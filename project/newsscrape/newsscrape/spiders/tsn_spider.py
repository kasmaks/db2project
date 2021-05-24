from newsscrape.spiders.news_spider import NewsSpider


class TsnSpider(NewsSpider):
    name = "TsnSpider"
    allowed_domains = ["tsn.ua"]
    start_urls = ["https://tsn.ua/"]

    media = "TSN"
    get_links_pattern = '//*[@class="c-sidebar"]//h3//a/@href'
    get_title_pattern = '//header[contains(@class, "c-card__box") and contains(@class, "c-card__head")]//h1//text()'
    get_news_text_pattern = '//div[contains(@class, "c-card__box") and contains(@class, "c-card__body")]//p/text() | ' \
                            '//div[contains(@class, "c-card__box") and contains(@class, "c-card__body")]//p//strong/text() | ' \
                            '//div[contains(@class, "c-card__box") and contains(@class, "c-card__body")]//p//a[not (contains(@class, "js-is-without-preview"))]/text() | ' \
                            '//div[contains(@class, "c-card__box") and contains(@class, "c-card__body")]//h2/text()'
    get_tags_pattern = '//ul[@class="c-tag-list"]//li/a//text()'
    get_date_pattern = '//footer[contains(@class, "c-card__box") and contains(@class, "c-card__foot")]//time/@datetime'
