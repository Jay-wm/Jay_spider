'''模拟浏览器'''
import time
from selenium import webdriver

'''7.3.1'''
# url = 'http://exercise.kingname.info/ajax_5_backend'
# html_json = requests.post(url, headers={'ReqTime': str(int(time.time()*1000))}, json={'sum': '6'}).content.decode()
# html_dict = json.loads(html_json)

# Initializing
driver = webdriver.Chrome(r'C:\Users\Administrator.DESKTOP-74UB6TU\PycharmProjects\Jay_spider\Python_Spider\chromedriver.exe')

# Open the web
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
time.sleep(10)

# Get code of the web
html = driver.page_source

# print the code
print(html)
