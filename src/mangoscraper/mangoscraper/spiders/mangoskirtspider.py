import scrapy


class MangoSkirtSpider(scrapy.Spider):
    name = 'mangoskirt'

    def start_requests(self):
        url = 'https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99'
        yield scrapy.Request(url, meta={'playwright': True})

    def parse(self, response):
        yield {
            'name': response.css('h1.product-name::text').get(),
            'price': float(response.css('span.S5XGZ.text-title-xl::text').get().replace('£ ', '').replace('лв. ', '')),
            'color': response.css('span.colors-info-name::text').get(),
            'size': response.css('span.text-title-m.gk2V5::text').getall()
        }
