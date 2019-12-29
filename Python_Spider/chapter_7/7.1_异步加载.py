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


# 7.1.5
# the html
# url = 'http://exercise.kingname.info/exercise_ajax_3.html'
# first_ajax_url = 'http://exercise.kingname.info/ajax_3_backend'
# secend_ajax_url = 'http://exercise.kingname.info/ajax_3_postbackend'
#
# page_html = requests.get(url).content.decode()
# secret_2 = re.search("secret_2 = '(.*?)'", page_html).group(1)
#
# ajax_1_json = requests.get(first_ajax_url).content.decode()
# ajax_1_dict = json.loads(ajax_1_json)
# secret_1 = ajax_1_dict['code']
#
# ajax_2_json = requests.post(secend_ajax_url, json = {
#     'name': "青南",
#     'age': 24,
#     'secret1': secret_1,
#     'secret2': secret_2}).content.decode()
# ajax_2_dict = json.loads(ajax_2_json)
# code = ajax_2_dict['code']
# print(f'最终页面显示的内容：{code}')


# 7.1.6
url = 'http://exercise.kingname.info/ajax_4_backend'
code_json = requests.post(url, json={'username': 'kingname', 'password': 'genius'}).content.decode()
code_dict = json.loads(code_json)
print(code_dict['code'])

