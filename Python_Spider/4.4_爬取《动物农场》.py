# coding=GBK
import requests
import re
import csv
import os

def get_toc(html):
    toc_url_list = []
    toc_block = re.findall('����</strong></td>(.*?)</tbody>', html, re.S)[0]
    toc_url = re.findall('<a href="(.*?)"', toc_block, re.S)
    for url in toc_url:
        toc_url_list.append('http://www.kanunu8.com/book3/6879/'+url)
    return toc_url_list


def get_article(html):
    chapter_name = re.search('size="4"> (.*?)<', html, re.S).group(1)
    text_block = re.search('<p>(.*?)</p>', html, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    return chapter_name, text_block

def save(chapter, article):
    os.makedirs('����ũ��', exist_ok = True)
    with open(os.path.join('����ũ��', chapter+'.txt'), 'w', encoding = 'utf-8') as f:
        f.write(article)

# ���ȵõ�С˵Ŀ¼ҳԴ����
html = requests.get('http://www.kanunu8.com/book3/6879').content.decode('gbk')

# �õ�ÿһ�µ���ַ
toc_url_list = get_toc(html)


for url_list in toc_url_list:
    # �ֱ���ÿһ����ҳ��Դ����
    html = requests.get(str(url_list)).content.decode('gbk')
    # ÿ��ѭ�����һ�µı������½�����
    chapter_name = get_article(html)[0]
    article = get_article(html)[1]
    # ����С˵����
    save(chapter_name, article)
