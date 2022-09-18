import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class WebKeys:

    def __init__(self,dr=''):
        self.open_browser(dr)

    def open_browser(self,dr=''):
        if dr == None or dr == '' or dr == 'chrome':
            self.driver = webdriver.Chrome()
        elif dr == 'ie':
            self.driver = webdriver.Ie()
        elif dr == 'safari':
            self.driver = webdriver.Safari()

    def get_url(self,url):
        self.driver.get(url)

    def sleep(self,sec):
        time.sleep(sec)

    def __find_ele(self,locator:str):
        """
        locator:支持通过xpath、css_selector、id查找元素
        return:返回找到的元素
        """
        
        if locator.startswith('/'):
            return self.driver.find_element_by_xpath(locator)
        elif locator.startswith('#') or locator.find('>') != -1:
            return self.driver.find_element_by_css_selector(locator)
        else:
            return self.driver.find_element_by_id(locator)
        
        
    def input(self,locator,text):
        ele = self.__find_ele(locator)
        if ele:
            ele.send_keys(text)

    def click(self,locator):
        ele = self.__find_ele(locator)
        if ele:
            ele.click()

    def hover(self,locator):
        ele = self.__find_ele(locator)
        if ele:
            action = ActionChains(self.driver)
            action.move_to_element(ele)

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

    def wait_until(self,locator):
        # WebDriverWait(self.driver,1).until(EC.visibility_of_element_located(locator))
        ele = self.__find_ele(locator)
        print(EC.visibility_of(ele))
        WebDriverWait(self.driver,1).until(EC.visibility_of(self.__find_ele(locator)))

    
    def select_by_text(self,locator,text):
        ele = Select(self.__find_ele(locator))
        ele.select_by_visible_text(text)

    def quit(self):
        self.driver.quit()