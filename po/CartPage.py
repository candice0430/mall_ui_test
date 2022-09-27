from time import time
from po.base_page import BasePage
    

class CartPage(BasePage):
    MY_CART_TXT = '//span[text()="我的购物车"]'


    def checkout(self,timeout=10):
        self.move_to_ele(self.MY_CART_TXT)
        self.wait_until('//a[contains(text(),"去购物车结算")]',timeout)
        self.click('//a[contains(text(),"去购物车结算")]')
        self.click('//a[@class="paytotal"]')
        self.wait_until('//button[@class="checkout-submit"]')
        self.click('//button[@class="checkout-submit"]')
        self.wait_until('//p[@class="succ-p"]',timeout)
        order_number = self.get_order_number('//p[@class="succ-p"]','\d{18}')
        return order_number

