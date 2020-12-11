import scrapy


class TelebotSpider(scrapy.Spider):
    name = 'telebot'
    #allowed_domains = ['www.telegram.ee/2020/11']
    #start_urls = ['https://www.telegram.ee/2020/01']
    #allowed_domains = ['www.telegram.ee/2020/01', 'www.telegram.ee/2020/02', 'www.telegram.ee/2020/03','www.telegram.ee/2020/04',
    #                  'www.telegram.ee/2020/05', 'www.telegram.ee/2020/06', 'www.telegram.ee/2020/07', 'www.telegram.ee/2020/08',
    #                 'www.telegram.ee/2020/09', 'www.telegram.ee/2020/10', 'www.telegram.ee/2020/11','www.telegram.ee/2020/12',]
    start_urls = ['https://www.telegram.ee/arvamus', 'https://www.telegram.ee/eesti','https://www.telegram.ee/maailm', 'https://www.telegram.ee/nwo', 'https://www.telegram.ee/teadus-ja-tulevik']
    #start_urls = ['https://www.telegram.ee/2020/01', 'https://www.telegram.ee/2020/02','https://www.telegram.ee/2020/03',                   #'https://www.telegram.ee/2020/04', 'https://www.telegram.ee/2020/05','https://www.telegram.ee/2020/06', 
#'https://www.telegram.ee/2020/07', 'https://www.telegram.ee/2020/08','https://www.telegram.ee/2020/09', 
#'https://www.telegram.ee/2020/10', 'https://www.telegram.ee/2020/11','https://www.telegram.ee/2020/12']

    def parse(self, response):
        HL_SELECTOR = '.grid-item'
        for news in response.css(HL_SELECTOR): 
            LINK_SELECTOR = 'div ::attr(href)'
            yield {
                'link': news.css(LINK_SELECTOR).extract_first(),
            }
        next_page = response.xpath('.//a[@class="next page-numbers"]/@href').extract_first()
        print("Järgmine lehekülg on: ", next_page)
        #print("URL " + response.urljoin(next_page))

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)