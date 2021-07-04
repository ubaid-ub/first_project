# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class QuotesSpider(scrapy.Spider):
	name="tags"
	
	def start_requests(self):
		url = 'http://quotes.toscrape.com/'
		tag = getattr(self, 'tag', None)
		if tag is not None:
			url=url+ 'tag/'+ tag
		yield scrapy.Request(url, self.parse)
	
	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
				'text' : quote.css('span.text::text').get(),
				'author' : quote.css('small.author::text').get(),
				}
		next_page = response.css('li.next a::attr(href)').get()
		if next_page is not None:
			yield response.follow(next_page, self.parse)
