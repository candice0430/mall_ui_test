from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time

# 登录
driver = webdriver.Chrome()
url = "http://testingedu.com.cn:8000/Home/user/login.html"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

# driver.find_element_by_id('username').send_keys("13800138006")
driver.find_element_by_xpath('//*[@id="username"]').send_keys("13800138006")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
driver.find_element(by=By.ID,value="verify_code").send_keys("123456")
driver.find_element_by_xpath('//a[@class="J-login-submit"]').click()
time.sleep(1)

# 头像上传
ele = driver.find_element_by_xpath('//div[@class="u-dt"]')
ActionChains.move_to_element(ele)

driver.get("")

