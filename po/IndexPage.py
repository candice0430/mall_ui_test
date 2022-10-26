from po.base_page import BasePage

class IndexPage(BasePage):
    URL = 'http://testingedu.com.cn:8000/'

    SEARCH_INPUT = 'q'
    SEARCH_BTN = '//button[@class="ecsc-search-button"]'
    SEARCH_RESULT = '//a[text()="搜索结果"]'
    GOOD_NAME_TXT = '//a[contains(text(),"{}")]'
    JOIN_CART_BTN = 'join_cart'
    JOIN_CART_WIN = '//span[@class="layui-layer-setwin"]/a'

    def search(self,text):
        self.get_url(self.URL)
        self.input(self.SEARCH_INPUT,text)
        self.click(self.SEARCH_BTN)

    def expect_search_result(self,timeout):
        self.wait_until(self.SEARCH_RESULT,timeout)

    
    def add_to_cart(self,search_text,timeout,name='Huawei/华为 nova 2s'):
        self.search(search_text)
        self.expect_search_result(timeout)
        good_name_ele = self.GOOD_NAME_TXT.format(name)
        self.click(good_name_ele)
        self.sleep(1)
        self.click(self.JOIN_CART_BTN)
        # 关闭弹窗
        self.sleep(1)
        self.click(self.JOIN_CART_WIN)