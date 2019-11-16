import requests

# html = requests.get('http://exercise.kingname.info/exercise_requests_get.html')#.content.decode()
# html_bytes = html.content
# html_str = html_bytes.decode() 
# print(html_str)

data = {'name': 'kingname', 'password': '1234567'}
# html_formdata = requests.post('http://exercise.kingname.info/exercise_requests_post', data = data)\
# .content.decode()
# print(html_formdata)
html_json = requests.post('http://exercise.kingname.info/exercise_requests_post', json = data)\
.content.decode()
print(html_json)

