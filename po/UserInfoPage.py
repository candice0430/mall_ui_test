from po.base_page import BasePage
from utils.file_handle import FileHandle


class UserInfoPage(BasePage):

    URL = "http://testingedu.com.cn:8000/Home/User/info.html"

    data_file_path = FileHandle.absolute_path('','images.jpeg')

    def upload_avtar(self,file_path=data_file_path):
        self.get_url("http://testingedu.com.cn:8000/Home/User/info.html")
        self.click_js('preview')
        self.sleep(1)

        self.into_iframe('//*[@id="layui-layer-iframe1"]')
        self.sleep(1)
        self.input('//*[@id="filePicker"]/div[2]/input',file_path)
        self.wait_until('//span[text()="100%"]')
        self.click('//div[@class="saveBtn"]')
        self.out_to_iframe()
        self.click('//*[@value="确认保存"]')