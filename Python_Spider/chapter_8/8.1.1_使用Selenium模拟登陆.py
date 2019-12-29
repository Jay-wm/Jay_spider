'''
    初始化Chromedriver
    打开知乎登录界面
    找到用户名输入框，输入用户名
    找到密码输入框，输入密码
    手动点击验证码
    按下登陆键
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 初始化Chromedriver
driver = webdriver.Chrome(r'/Python_Spider/chromedriver.exe')
driver.get("https://www.zhihu.com/signin?next=%2F")

# 切换登陆方式
# cd = driver.find_element_by_xpath()

# 找到用户名输入框
elem = driver.find_element_by_name("username")
elem.clear()

# 输入用户名
elem.send_keys("13277193523")

# 找到密码输入框
password = driver.find_element_by_name("password")
password.clear()

# 输入密码
password.send_keys("wm052311")

input("请在网页上点击倒立的文字，完成以后回到这里按任意键继续")

# 模拟键盘回车键
elem.send_keys(Keys.RETURN)

time.sleep(10)
print(driver.page_source)
driver.quit()