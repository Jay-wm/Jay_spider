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
    WebDriverWait(driver, 35).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通过'))
except Exception as _:
    print('网页加载太慢，不想等了')

element = driver.find_element_by_xpath('//div[@class = "content"]')
print(f'异步加载的内容为: {element.text}')

driver.quit()