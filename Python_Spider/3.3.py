import re
import csv

with open('source2.txt', 'r', encoding = 'GBK') as f:
    source = f.read()

every_reply = re.findall('class="l_post l_post_bright j_l_post clearfix  "(.*?)</div></div></div></div>', source, re.S)
result_list = []


for each_reply in every_reply:
    result = {}
    result['username'] = re.findall('author="(.*?)"' or '" ><br><br><br><br><br>(.*?)<br><img class="', each_reply, re.S)
    result['content'] = re.findall('class="d_post_content j_d_post_content " style="display:;"> (.*?)<br>', each_reply, re.S)
    result['image'] = re.findall('src="(.*?)" >', each_reply, re.S)
    result['reply_time'] = re.findall('</span><span class="tail-info">(2019.*?)</span>', each_reply, re.S)
    result_list.append(result)


with open('tieba_data2.csv', 'w', encoding = 'UTF-8') as f:
    writer = csv.DictWriter(f, fieldnames = ['username', 'content', 'image', 'reply_time'])
    writer.writeheader()
    writer.writerows(result_list)
    
