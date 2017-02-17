import scrapy

from scrapytest.items import HouseItem

import re

class LianjiaSpider(scrapy.Spider):
	name = "lianjia"
	allowed_domains = ["lianjia.com"]
	start_urls = ["http://nj.lianjia.com/ershoufang/pg%s/" % nu for nu in xrange(1,5)]
	def parse(self,resp):
		for entity in resp.css("div .info.clear"):
			item = HouseItem()
			item["title"] = entity.css("div .title a::text").extract()
			item["price"] = entity.css(".totalPrice span::text").extract()
			item["size"] = entity.css(".houseInfo::text").extract()[0].split("|")[2]
			item["perPrice"] = float(item["price"][0]) / float(re.findall(r'\d+.\d+',item["size"])[0])
			yield item
