import requests
import redis
import lxml.html
import re
from pymongo import MongoClient


'''Get BaiYeXing '''
# Innitialize 
client_1 = redis.StrictRedis()
client_2 = MongoClient()
db = client_2.Fiction
dbc = db.book

# Creat a empty list
content_list = []

# Get the title and content of every capter 
while client_1.llen('url_quene') > 0:
	url = client_1.lpop('url_quene')
	source = requests.get(url).content.decode()
	selector = lxml.html.fromstring(source)
	# 此处h1的'1'均为数字1
	chapter_name = selector.xpath('//div[@class="h1title"]/h1/text()')
	
	# 正则表达式法
	#chapter_name = re.search('<div class="h1title"><h1>(.*?)</h1>', source, re.S).group(1)

	# XPath法获取，此处'l'均为小写字母'l'
	content = selector.xpath('//div[starts-with(@id, "htmlContent")]/p/text()')
	content_list.append({'title': chapter_name, 'content': '\n'.join(content)})

# Insert the content_list[] into mongodb 
for a in content_list:
	dbc.insert(a)
