# -*- coding: utf-8 -*-
import scrapy
from baidu.items import PersonInfoItem

class ExampleSpider(scrapy.Spider):
    name = "exercise_3"
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/exercise_xpath_3.html']

    def parse(self, response):
        # title = response.xpath('//title/text()').extract()
        # search_button_text = response.xpath('//input[@class="bg s_btn"]/@value').extract()
        # print(title)
        # print(search_button_text)

        # title_example = response.xpath('//title/text()')
        # title_example_1 = title_example.extract()[0]
        # title_example_2 = title_example[0].extract()
        # print("先读取下表为0的元素，再extract():{}".format(title_example_1))
        # print("先extract，再读取下标为0的元素：{}".format(title_example_2))

        # item_list = response.xpath('//ul[@class="item"]')
        # for item in item_list:
        #     name = item.xpath('li[@class="name"]/text()').extract()
        #     price = item.xpath('li[@class="price"]/text()').extract()
        #     name = name[0] if name else 'N/A'
        #     price = price[0] if price else 'N/A'
        #     print('商品：{}，价格：{}'.format(name[0], price[0]))

        person_list = response.xpath('//div[@class="person_table"]/table/tbody/tr')
        for person in person_list:
            item = PersonInfoItem()
            person_info = person.xpath('td/text()')
            item['name'] = person_info[0]
            item['age'] = person_info[1]
            item['salary'] = person_info[2]
            item['phone'] = person_info[3]
            yield item