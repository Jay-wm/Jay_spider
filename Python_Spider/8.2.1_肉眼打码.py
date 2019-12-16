import requests
import lxml.html

url = 'http://exercise.kingname.info/exercise_captcha.html'
url_check = 'http://exercise.kingname.info/exercise_captcha_check'

session = requests.Session()
html = session.get(url).content
selector = lxml.html.fromstring(html)
captcha_html = selector.xpath('//img/@src')[0]

image = requests.get('http://exercise.kingname.info/'+ captcha_html).content
with open('captcha.png', 'wb') as f:
    f.write(image)

captcha = input('请查看captcha.png文件，并输入')
login = session.post(url_check, data = {'captcha': captcha}).content.decode()

print(f'输入验证码后，网站返回：{login}')