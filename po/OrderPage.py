from po.base_page import BasePage

class OrderPage(BasePage):
    URL = 'http://testingedu.com.cn:8000/index.php/Home/Order/order_list.html'

    def cancel_order(self):
            
        self.get_url(self.URL)
        self.sleep(2)
        print("self.order_no:",self.driver.order_no)
        locator = '//em[text()="%s"]/../..//a[text()="取消订单"]'%self.driver.order_no
        self.click(locator)
        self.click('//a[text()="确定"]')
        self.sleep(5)
