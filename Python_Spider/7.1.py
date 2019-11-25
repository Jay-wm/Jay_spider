'''new file, section 7.1'''
import json
import requests
import re

# person = \
#     {
#       'basic_info': {
#           'name': 'kingname',
#           'age': 24,
#           'sex': '男',
#           'merry': False
#       },
#       'work_info':{
#           'salary': 99999,
#           'position': 'engineer',
#           'department': None
#       }
#     }
#
# person_json = json.dumps(person, indent = 4)
# print(person_json)


#7.1.4.1
# html_json = '{"code": "\u884c\u52a8\u4ee3\u53f7\uff1a\u5929\u738b\u76d6\u5730\u864e"}'
# html_dict = json.loads(html_json)
# print(html_dict)

# 7.1.4.2
# url = 'http://exercise.kingname.info/exercise_ajax_2.html'
# html = requests.get(url).content.decode()
# code_json = re.search("secret = '(.*?)'", html, re.S).group(1)
# code_dict = json.loads(code_json)
# print(code_dict['code'])

# 7.1.5.1
# json = {"name": "xx"', "age": "24", "secret1" = "123", secret2 = "456"}
url1 = 'http://http://exercise.kingname.info/exercise_ajax_3.html'
url2 = 'http://exercise.kingname.info/ajax_3_postbackend'
json1 = requests.get(url1).content.decode()
secret2 =
html1 = requests.post(url, json= {"name": "xx", "age": "24", "secret1": "123", "secret2": "456"})
html2 = requests.post(url, json= {"name": "xx", "age": "24"})
print(json.loads(html1.content.decode()))
print(json.loads(html2.content.decode()))
