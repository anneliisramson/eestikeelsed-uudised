import scrapy


class UueduudisedSpider(scrapy.Spider):
    name = 'uueduudised'
    #allowed_domains = ['uueduudised.ee/arhiiv']
    start_urls = ['https://uueduudised.ee/rubriik/arvamus/','https://uueduudised.ee/rubriik/uudis/eesti/', 'https://uueduudised.ee/rubriik/uudis/maailm/', 'https://uueduudised.ee/rubriik/majandus/']

    def parse(self, response):
        HL_SELECTOR = '.news_box_item_content'
        for news in response.css(HL_SELECTOR): 
            LINK_SELECTOR = 'h3 a ::attr(href)'
            yield {
                'link': news.css(LINK_SELECTOR).extract_first(),
            }
        #next_page = response.css('.next page-numbers a ::attr(href)').extract_first()
        next_page = response.xpath('.//a[@class="next page-numbers"]/@href').extract_first()
        print("Järgmine lehekülg on: ", next_page)
        #print("URL " + response.urljoin(next_page))

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
