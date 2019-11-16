import requests
import lxml.html
import redis
from pymongo import MongoClient


connection = MongoClient()
db = connection.Fiction
dbc = db.book

client = redis.StrictRedis(host = '127.0.0.1', port = 6379)
selector = lxml.html.fromstring('http://dongyeguiwu.zuopinj.com/5525/')
url_list = selector.xpath('//div[@class="book_list"]/ul/li/a/@href')

for url in url_list:
	client.rpush('url_quene', url)

content_list = []
while client.llen('url_quene') > 0:
	url = client.lpop('url_quene').docode()
	source = requests.get(url).content
	selector = html.fromstring(source)
	chapter_name = selector.xpath('//div[@class="hltitle]/hl/text()"')[0]
	content = selector.xpath('div[@class=htmlContent]/p/text()')
	content_list.append({'title': chapter_name, 'content': '\n'.join(content)})

for a in content_list:
	dbc.insert(a)
