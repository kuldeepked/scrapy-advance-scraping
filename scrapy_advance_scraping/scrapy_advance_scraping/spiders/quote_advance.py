# -*- coding: utf-8 -*-
import scrapy


class QuoteAdvanceSpider(scrapy.Spider):
    name = 'quote_advance'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath("//*[@class = 'quote']")
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract() 
            author = quote.xpath('.//*[@class="author"]/text()').extract()   
            tags = quote.xpath(".//*[@class = 'tag']/text()").extract()  

            print(text)
            print(author)
            print(tags)

