import re
import csv

with open('刺客教条.txt', 'r', encoding ='GBK') as f:
    source = f.read()

result_list = []
username_list = re.findall('title="主题作者:(.*?)"', source, re.S)
content_list = re.findall('target="_blank" class="j_th_tit ">(.*?)</a>', source, re.S)

for i in range(len(username_list)):
    result = {'username': username_list[i],
              'content': content_list[i]}
    result_list.append(result)


with open('tieba_data.csv', 'w', encoding ='UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames = ['username', 'content'])
    writer.writeheader()
    writer.writerows(result_list)
    
