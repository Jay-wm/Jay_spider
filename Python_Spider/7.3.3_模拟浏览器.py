'''模拟浏览器'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from  selenium.webdriver.support import expected_conditions as EC

# Initializing
driver = webdriver.Chrome(r'C:\Users\Administrator.DESKTOP-74UB6TU\PycharmProjects\Jay_spider\Python_Spider'
                          r'\chromedriver.exe')

# Open the web
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
try:
    # two are accessible
    # WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content")))
    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通过'))
except Exception as _:
    print('网页加载太慢，不想等了')

'''获取网页中元素'''
'''类似于BeautifulSoup4语句'''
# 有多个符合结果，返回第一个
element1 = driver.find_element_by_id("passwd-id")
element2 = driver.find_element_by_name("passwd")

# 返回结果列表
element_list1 = driver.find_elements_by_id("passwd-id")
element_list2 = driver.find_elements_by_name("passwd")

'''类似于XPath'''
# 返回第一个符合的结果
element3 = driver.find_element_by_xpath("//input[@id = 'passwd-id]")

# 返回结果列表
element_list3 = driver.find_elements_by_xpath("//input[@id = 'passwd-id]")