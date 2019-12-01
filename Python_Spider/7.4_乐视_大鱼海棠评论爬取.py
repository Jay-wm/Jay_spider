import requests
import re
import json

class LetvSpider(object):

    COMMENT_URL = 'http://api.my.le.com/vcm/api/list?jsonp=jQuery19106596654532269319_1575164258089&type=video&rows=20&page=1&sort=&cid=1&source=1&xid={xid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1&_=1575164258095'

    HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh; q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'tj_lc = 32696bb81587f2e7258c350f8518994e; tj_uuid = -_15751637970179369968;tj_env = 1; ark_uuid = ck-d3092f27-687d-457f-b1c6-ba3ac90877c4-1201-092959;bd_xid = 32696bb81587f2e7258c350f8518994e; ssoCookieSynced = 1; language = zh-cn; sso_curr_country = CN; tj_v2c = -26680567_1',
        'Host': 'api.my.le.com',
        'Referer': 'http://www.le.com/ptv/vplay/26680567.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    def __init__(self, url):
        self.necessary_info = {}
        self.url = url
        self.get_necessary_id()
        self.get_comment()

    def get_source(self, url, headers):
        return requests.get(url, headers).content.decode()

    def get_necessary_id(self):
        '''获取请求URL所需参数ID'''
        source = self.get_source(self.url, self.HEADERS)
        vid = re.search('vid:(\d+)', source).group(1)
        pid = re.search('pid:(\d+)', source).group(1)
        self.necessary_info['xid'] = vid
        self.necessary_info['pid'] = pid

    def get_comment(self):
        url = self.COMMENT_URL.format(xid = self.necessary_info['xid'], pid = self.necessary_info['pid'])
        source = self.get_source(url, self.HEADERS)
        source_json = re.findall('({".*?})\)', source)[0]
        # print(source_json)
        source_dict = json.loads(source_json)
        # print(source_dict)
        comments = source_dict['data']
        # print(comments)
        for comment in comments:
            print(f'发帖人：{comment["user"]["username"]}, 评论内容: {comment["content"]}')

if __name__ == '__main__':
    spider = LetvSpider('http://www.le.com/ptv/vplay/26680567.html')