import requests

HEADERS = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'BAIDUID=7DAF2FBDA9A0C79F54F2C89FC45F4C0D:FG=1; BIDUPSID=7DAF2FBDA9A0C79F54F2C89FC45F4C0D; ' \
    #           'PSTM=1574519669; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; HMACCOUNT=5DF3B45ABD9B9AEC; ' \
    #           'H_PS_PSSID=1430_21104_30211_26350; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1575188957|; delPer=0; PSINO=7',
    # 'Host': 'hm.baidu.com',
    # 'If-None-Match': '47d6f3f3d5db9e216ee580b218c7b7de',
    # 'Referer': 'https://www.zhihu.com/signin?next=%2F',
    # 'Sec-Fetch-Mode': 'no-cors',
    # 'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                  'Chrome/78.0.3904.108 Safari/537.36'
}

source = requests.get('https://www.zhihu.com', headers = HEADERS).content.decode()
print(source)