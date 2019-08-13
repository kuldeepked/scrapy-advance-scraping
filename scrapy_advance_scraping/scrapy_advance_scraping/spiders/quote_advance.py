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
            print (' ')
            print(text)
            print(author)
            print(tags)
            print (' ')

        next_page_url = response.xpath("//*[@class = 'next']/a/@href").extract_first()          
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)

