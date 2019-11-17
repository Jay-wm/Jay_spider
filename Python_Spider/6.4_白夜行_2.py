import requests
import redis
import lxml.html
from pymongo import MongoClient

# Innitialize 
client_1 = redis.StrictRedis()
client_2 = MongoClient()
db = client_2.Fiction
dbc = db.book

content_list = []
# data = []

while client_1.llen('url_quene') > 0:
	url = client_1.lpop('url_quene')
	source = requests.get(url).content
	# source = "\'\'\'" + "\n" + source + "\n" + "\'\'\'"
	# print(source)
	selector = lxml.html.fromstring(source)
	chapter_name = selector.xpath('//div[@class="hltitle"]/hl/text()')
	t = chapter_name
	print(t)
	
	# content = selector.xpath('div[@class=htmlContent]/p/text()')
	# # content_list.append({'title': chapter_name, 'content': '\n'.join(content)})
	# print(content)
	break
# print(content_list)
# for a in content_list:
# 	dbc.insert(a)
