import requests
import redis
import lxml.html
from pymongo import MongoClient

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
	chapter_name = selector.xpath('//div[@class="hltitle"]/hl/text()')
	content = selector.xpath('div[@class=htmlContent]/p/text()')
	content_list.append({'title': chapter_name, 'content': '\n'.join(content)})

# Insert the content_list[] into mongodb 
for a in content_list:
	dbc.insert(a)
