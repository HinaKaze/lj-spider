import scrapy

from scrapytest.items import DmozItem

class DomzSpider(scrapy.Spider):
	name = "domz"
	allowed_domains = ["dmoz.org"]
	start_urls = ["http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"]

	def parse(self, response):
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['title'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			yield item
