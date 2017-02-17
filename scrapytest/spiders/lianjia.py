import scrapy

from scrapytest.items import HouseItem

class LianjiaSpider(scrapy.Spider):
	name = "lianjia"
	allowed_domains = ["lianjia.com"]
	start_urls = ["http://nj.lianjia.com/ershoufang/rs/"]

	def parse(self,resp):
		for entity in resp.css("div .info.clear"):
			item = HouseItem()
			item["title"] = entity.css("div .title a::text").extract()
			item["price"] = entity.css(".totalPrice span::text").extract()
			yield item
