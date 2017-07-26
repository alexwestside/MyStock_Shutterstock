# bin/user/python

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://submit.shutterstock.com/earnings/daily?page=1&date=2017-07-06&language=en&category=25_a_day&sort=desc&sorted_by=count&per_page=20',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'submit.shutterstock-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)