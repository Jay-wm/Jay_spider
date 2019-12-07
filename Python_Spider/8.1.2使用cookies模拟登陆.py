import requests

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '_zap=b30505a3-d0e8-44a0-a282-4cc4f78245a5; ' \
              '_xsrf=p7CRpEElR2GbYrQxhjB1ko7nhYA7wSOC; d_c0="AMCgHxxNcBCPTviFcrPgepjAYPZjol1rWfU=|1575194313"; tst=r;' \
              ' Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1575195133,1575465107,1575470846,1575703003; ' \
              'tgw_l7_route=e5422eddfa4a8c2269da8eb93eb319b1; ' \
              'capsion_ticket="2|1:0|10:1575705956|14:capsion_ticket|44:ODZiZjQxMTg4ODQ5NGQ5ZjgwMGVmMTQ3Mzk3ZWYzNjA=|eb1af24945c49fbaff794ce2ba2d57ba0f32836a28d9175774db062d9f19b10e"; ' \
              'z_c0="2|1:0|10:1575705968|4:z_c0|92:Mi4xRVpGQ0JnQUFBQUFBd0tBZkhFMXdFQ1lBQUFCZ0FsVk5jS3ZZWGdDTnpuZzFrSHBVSXB1Vmt4ZUxBMGhXb3JaRmdR|54edd33718ef4cc5f3edc19a41160fcff5d6306760b2741b14941b03d1569a4d"; ' \
              'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1575705971',
    'referer': 'https://www.zhihu.com/signin?next=%2F',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

source = requests.Session()
code = source.get('https://www.zhihu.com/', headers = HEADERS, verify = False).content.decode('gbk')
print(code)