import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import re


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def get_url(self,url):
        self.driver.get(url)

    def sleep(self,sec):
        time.sleep(sec)

    def __find_ele(self,locator:str):
        """
        locator:支持通过xpath、css_selector、id查找元素
        return:返回找到的元素
        """
        loc = self.__get_locator(locator)
        return self.driver.find_element(*loc)

    def __get_locator(self,locator_str:str):
        if locator_str.startswith('/'):
            return (By.XPATH,locator_str)
        elif locator_str.startswith('#') or locator_str.find('>') != -1:
            return (By.XPATH,locator_str)
        else:
            return (By.ID,locator_str)



    def ele_is_exist(self,locator):
        return self.__find_ele(locator)
        
        
    def input(self,locator,text):
        ele = self.__find_ele(locator)
        if ele:
            ele.send_keys(text)

    def click(self,locator):
        ele = self.__find_ele(locator)
        if ele:
            ele.click()

    def move_to_ele(self,locator):
        ele = self.__find_ele(locator)
        if ele:
            action = ActionChains(self.driver)
            action.move_to_element(ele).perform()

    def cur_url(self,url):
        print("self.driver.current_url:",self.driver.current_url)
        return self.driver.current_url == url

    def click_js(self,locator):
        ele = self.__find_ele(locator)
        if ele:
            self.driver.execute_script("arguments[0].click();",ele)

    def into_iframe(self,locator):
        ele = self.__find_ele(locator)
        if ele:
            self.driver.switch_to.frame(ele)

    def out_to_iframe(self):
        self.driver.switch_to.default_content()

    def wait_until(self,locator,sec=1):
      WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.__get_locator(locator))
    )

    def wait(self,sec):
        self.driver.implicitly_wait(sec)
    
    def select_by_text(self,locator,text):
        ele = Select(self.__find_ele(locator))
        ele.select_by_visible_text(text)

    def get_order_number(self,locator,regstr):
        ele = self.__find_ele(locator)
        order_number = re.findall(regstr,ele.text)[0]
        return order_number

    def quit(self):
        self.driver.quit()

