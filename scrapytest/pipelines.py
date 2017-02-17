# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs

class ScrapytestPipeline(object):

    def __init__(self):
        self.file = codecs.open('lianjia_utf8.json', 'w', encoding='utf-8')
        self.totalPerPrice = 0
        self.totalHouse = 0

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        self.totalHouse+=1
        self.totalPerPrice += item["perPrice"]
        return item

    def spider_closed(self, spider):
    	print "Avg house price from",self.totalHouse,".Is :",totalPerPrice / totalHouse
        self.file.close()