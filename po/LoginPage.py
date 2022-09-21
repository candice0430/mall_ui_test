from po.base_page import BasePage


class LoginPage(BasePage):
    URL = 'http://testingedu.com.cn:8000/Home/user/login.html'
    USERNAME_EDIT = 'username'
    PASSWORD_EDIT = 'password'
    CODE = 'verify_code'
    LOGIN_BTN = '//a[@class="J-login-submit"]'

    LOGIN_FAIL_HINT = 'layui-layer1'
    

    def login(self,username,pwd,code):
        self.get_url(self.URL)
        self.input(self.USERNAME_EDIT,username)
        self.input(self.PASSWORD_EDIT,pwd)
        self.input(self.CODE,code)
        self.click(self.LOGIN_BTN)

    def until_response(self,timeout):
        print(type(timeout))
        print(timeout)
        self.wait_until(self.LOGIN_FAIL_HINT,timeout)

    def expect_prompt_message(self,msg):
        if not self.ele_is_exist(self.LOGIN_FAIL_HINT):
            raise Exception("case failed")


# login_page = LoginPage()

