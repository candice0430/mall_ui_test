from telnetlib import SE
from po.base_page import BasePage


class LoginPage(BasePage):
    URL = 'http://testingedu.com.cn:8000/Home/user/login.html'
    USERNAME_EDIT = 'username'
    PASSWORD_EDIT = 'password'
    CODE = 'verify_code'
    LOGIN_BTN = '//a[@class="J-login-submit"]'

    LOGIN_FAIL_HINT = 'layui-layer1'
    PHONE_NOT_EXIST_DIV = '//div[text()="{}"]'
    ACCOUNT_MSG_DIV = '//span[text()="账户余额"]'
    

    def login(self,username,password,code):
        print("username:",username)
        self.get_url(self.URL)
        self.input(self.USERNAME_EDIT,username)
        self.input(self.PASSWORD_EDIT,password)
        self.input(self.CODE,code)
        self.click(self.LOGIN_BTN)

    def until_response_fail(self,timeout):
        self.wait_until(self.LOGIN_FAIL_HINT,timeout)

    def until_response_suc(self,timeout):
        self.wait_until(self.ACCOUNT_MSG_DIV,timeout)

    def expect_prompt_message(self,text):
        msg_div = self.PHONE_NOT_EXIST_DIV.format(text)
        if not self.ele_is_exist(msg_div):
            raise Exception("case failed")
    


# login_page = LoginPage()

