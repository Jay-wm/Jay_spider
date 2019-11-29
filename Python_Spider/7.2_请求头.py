# Headers
import requests
import json

url = 'http://exercise.kingname.info/exercise_headers_backend'
Headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh; q=0.9',
    'anhao': 'kingname',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=utf-8',
    'Cookie': '__cfduid=de224b8ae0b4c97ca610745fd749648c61573977679',
    'Host': 'exercise.kingname.info',
    'Referer': 'http://exercise.kingname.info/exercise_headers.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
html_json = requests.get(url, headers = Headers).content.decode()
html_dict = json.loads(html_json)

print(html_dict)
