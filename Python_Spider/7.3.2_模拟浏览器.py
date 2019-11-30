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
    '''Four ways are accessible，By.CLASS_NAME, By.ID, By.NAME, or By.XPATH'''
    '''By.CLASS_NAME'''
    # 期望某个元素
    # WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "content")))
    # # 期望某个元素的text里面的文本
    # WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通过'))

    '''By.XPATH'''
    WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH, '//div[@class="content"]'), '通过'))

except Exception as _:
    print('网页加载太慢，不想等了')
print(driver.page_source)