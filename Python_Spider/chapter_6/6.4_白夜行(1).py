import requests
import lxml.html
import redis
import re


# get the code of the html of byx
# html = requests.get('http://dongyeguiwu.zuopinj.com/5525/')
# html_bytes = html.content
# html_str = html_bytes.decode()
html = requests.get('http://dongyeguiwu.zuopinj.com/5525/').content.decode('UTF-8')

client_1 = redis.StrictRedis()
selector = lxml.html.fromstring(html)
url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')

for url in url_list:
	client_1.lpush('url_quene', url)
	