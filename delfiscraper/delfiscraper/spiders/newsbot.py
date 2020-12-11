import scrapy


class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    #allowed_domains = ['www.delfi.ee']
    start_urls = ['https://www.delfi.ee/archive/?tod=03.12.2020&fromd=01.01.2020&channel=1&category=13&query=']
    #start_urls = ['https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=14&category=19350036&query=teadus',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=21&category=0&query=majandus',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=1&category=13&query=uudised',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=47&category=67583634&query=poliitika',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=47&category=67583610&query=',
                 #'https://www.delfi.ee/archive/?tod=08.12.2020&fromd=01.01.2020&channel=1&category=0&query=koroona']

    def parse(self, response):
        HL_SELECTOR = '.headline'
        for news in response.css(HL_SELECTOR): 
            LINK_SELECTOR = 'h1 a ::attr(href)'
            yield {
                'link': news.css(LINK_SELECTOR).extract_first(),
            }
        next_page = response.xpath('.//a[@class="item item-next"]/@href').extract()
        if next_page:
            next_href = next_page[0]
            next_page_url = 'http://www.delfi.ee' + next_href.strip()
            request = scrapy.Request(url=next_page_url)
            yield request
