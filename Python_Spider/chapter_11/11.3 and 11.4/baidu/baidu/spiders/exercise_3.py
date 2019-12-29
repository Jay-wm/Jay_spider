# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append(r"C:\Users\Administrator.DESKTOP-74UB6TU\PycharmProjects\Jay_spider\Python_Spider\chapter_11\11.2.2_using  xpath in scrapy\baidu\baidu")
from items import PersonInfoItem

class ExampleSpider(scrapy.Spider):
    name = "exercise_3"
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/exercise_xpath_3.html']

    def parse(self, response):
        person_list = response.xpath('//div[@class="person_table"]/table/tbody/tr')
        for person in person_list:
            item = PersonInfoItem()
            person_info = person.xpath('td/text()').extract()
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            yield item