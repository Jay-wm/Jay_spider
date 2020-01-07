# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append(r"C:\Users\Administrator.DESKTOP-74UB6TU\PycharmProjects\Jay_spider\Python_Spider\chapter_11\11.5_阶段案例\baidu\baidu")
from items import BlogItem
from scrapy_redis.spiders import RedisSpider
from lxml import etree
from html import unescape


class Example114Spider(RedisSpider):
    name = "exercise11_5"
    redis_key = 'blogspider'
    allowed_domains = ["www.kingname.info"]
    start_urls = ['https://www.kingname.info/archives/']
    host = 'https://www.kingname.info'

    def parse(self, response):
        title_tag_list = response.xpath('//a[@class = "post-title-link"]')
        for title_tag in title_tag_list:
            article_title = title_tag.xpath('span/text()').extract_first()
            article_url = self.host + title_tag.xpath('@href').extract_first()
            item = BlogItem()
            item['title'] = article_title
            item['url'] = article_url
            yield scrapy.Request(article_url, headers=self.settings['HEADERS'], callback=self.parse_detail,
                                 meta= {'item': item})


    def parse_detail(self, response):
        item = response.meta['item']
        post_time = response.xpath('//*[@id="posts"]/article/div/header/div/span[1]/time[@datetime]').extract_first()
        caegory = response.xpath('//*[@id="posts"]/article/div/header/h1').extract_first()
        post_body = response.xpath('//*[@id="posts-body"]')
        body_html = unescape(etree.tostring(post_body[0]._root).decode())
        # post_body.xpath('string(.)')
        item['post_time'] = post_time
        item['caegory'] = caegory
        item['detail'] = body_html
        yield item

