from audioop import add
from time import time
from po.base_page import BasePage


class AddressPage(BasePage):
    URL = 'http://testingedu.com.cn:8000/Home/User/address_list.html'
    ADD_ADDRESS_BTN = '//span[text()="增加新地址"]'
    NAME_INPUT = '//input[@name="consignee"]'
    MOBILE_INPUT = '//input[@name="mobile"]'
    PROVINCE_SEL = 'province'
    CITY_SEL = 'city'
    DISRTICT_SEL = 'district'
    ADDRESS_INPUT = '//input[@name="address"]'
    ADDRESS_SUMBIT = 'address_submit'
    
    SPAN_TXT = '//span[text()="{}"]'
    ADDRESS_SPAN_DEL = '//span[text()="{}"]/../..//a[text()="删除"]'

    def add_address(self,name,phone,province,city,district,address):
        self.get_url(self.URL)
        self.click(self.ADD_ADDRESS_BTN)
        self.input(self.NAME_INPUT,name)
        self.input(self.MOBILE_INPUT,phone)
        self.select_by_text(self.PROVINCE_SEL,province)
        self.sleep(0.5)
        self.select_by_text(self.CITY_SEL,city)
        self.sleep(0.5)
        self.select_by_text(self.DISRTICT_SEL,district)
        self.input(self.ADDRESS_INPUT,address)
        self.click(self.ADDRESS_SUMBIT)      
        

    def expect_address(self,name,address,timeout,is_exist=True):
        name_ele = self.SPAN_TXT.format(name)
        address_ele = self.SPAN_TXT.format(address)
        if is_exist:
            self.wait_until(name_ele,timeout)
            self.wait_until(address_ele,timeout)
        else:
            return not self.ele_is_exist(address_ele)

    def del_address(self,address,timeout):
        del_ele = self.ADDRESS_SPAN_DEL.format(address)
        self.wait_click_until(del_ele,timeout)
        print("del_ele:",del_ele)
        self.click(del_ele)
        self.sleep(2)
        



        