# -*- coding: utf-8 -*-
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "exercise_1"
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/exercise_xpath_1.html']

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

        name_list = response.xpath('//li[@class="name"]/text()').extract()
        price_list = response.xpath('//li[@class="price"]/text()').extract()
        for i in range(len(name_list)):
            print('商品：{}，价格：{}'.format(name_list[i], price_list[i]))