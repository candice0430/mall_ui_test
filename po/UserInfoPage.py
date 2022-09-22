from po.base_page import BasePage
from utils.file_handle import FileHandle


class UserInfoPage(BasePage):

    URL = "http://testingedu.com.cn:8000/Home/User/info.html"
    PRIVIEW_IMG = 'preview'
    AVTAR_IFRAME1 = '//*[@id="layui-layer-iframe1"]'
    FILE_INPUT = '//*[@id="filePicker"]/div[2]/input'
    FILE_UPLOAD_SUC_TXT = '//span[text()="100%"]'
    FILE_SAVE_BTN = '//div[@class="saveBtn"]'
    RE_UPLOAD = '//a[text()="重新上传"]'
    CONFIRM_BTN = '//*[@value="确认保存"]'


    data_file_path = FileHandle.absolute_path('','images.jpeg')

    def upload_avtar(self,file_path=data_file_path):
        self.get_url(self.URL)
        self.click_js(self.PRIVIEW_IMG)
        self.wait_until(self.AVTAR_IFRAME1,10)

        self.into_iframe(self.AVTAR_IFRAME1)
        self.input(self.FILE_INPUT,file_path)
    
    def expect_upload_suc(self):
        self.wait_until(self.FILE_SAVE_BTN,10)

    def save_upload(self):
        self.click(self.FILE_SAVE_BTN)
        self.out_to_iframe()
        self.click(self.CONFIRM_BTN)

    def expect_upload_fail(self,timeout=10):
        self.wait_until(self.RE_UPLOAD,timeout)



