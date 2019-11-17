import requests
import lxml.html
import redis
from pymongo import MongoClient


client_1 = MongoClient()
db = client_1.Fiction
dbc = db.book

client_2 = redis.StrictRedis()
selector = lxml.html.fromstring('http://dongyeguiwu.zuopinj.com/5525/')
url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')

for url in url_list:
	client_2.lpush('url_quene', url)

content_list = []
while client_2.llen('url_quene') > 0:
	url = client_2.lpop('url_quene').docode()
	source = requests.get(url).content
	selector = html.fromstring(source)
	chapter_name = selector.xpath('//div[@class="hltitle]/hl/text()"')[0]
	content = selector.xpath('div[@class=htmlContent]/p/text()')
	content_list.append({'title': chapter_name, 'content': '\n'.join(content)})

for a in content_list:
	dbc.insert(a)
