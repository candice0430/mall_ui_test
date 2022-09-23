from audioop import add
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

    def add_address(self,name,phone,province,city,district,address):
        self.get_url(self.URL)
        self.click(self.ADD_ADDRESS_BTN)
        self.input(self.NAME_INPUT,name)
        self.input(self.MOBILE_INPUT,phone)
        self.select_by_text(self.PROVINCE_SEL,province)
        self.select_by_text(self.CITY_SEL,city)
        self.select_by_text(self.DISRTICT_SEL,district)
        self.input(self.ADDRESS_INPUT,address)
        self.click(self.ADDRESS_SUMBIT)         

    def expect_address(self,name,address,timeout):
        name_ele = self.SPAN_TXT.format(name)
        address_ele = self.SPAN_TXT.format(address)
        self.wait_until(name_ele,timeout)
        self.wait_until(address_ele,timeout)
        