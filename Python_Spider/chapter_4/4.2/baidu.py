import requests
import time
from multiprocessing.dummy import Pool


def query(url):
    requests.get(url)

start =time.time()
for i in range(100):
    query('https://baidu.com')

end = time.time()
print(f'单线程循环访问100次百度时间，耗时：{end - start}')


start =time.time()
url_list = []
for i in range(100):
    url_list.append('https://baidu.com')
pool = Pool(10)
pool.map(query, url_list)
end = time.time()
print(f'多线程循环访问100次百度时间，耗时：{end - start}')
