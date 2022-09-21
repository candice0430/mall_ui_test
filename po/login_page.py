from po.base_page import BasePage


class LoginPage(BasePage):
    URL = 'http://testingedu.com.cn:8000/Home/user/login.html'
    USERNAME_EDIT = 'username'
    PASSWORD_EDIT = 'password'
    CODE = 'verify_code'
    LOGIN_BTN = '//a[@class="J-login-submit"]'

    LOGIN_FAIL_HINT = '//div[@class="layui-layer-title"]'

    def login(self,username,pwd,code):
        self.get_url(self.URL)
        self.input(self.USERNAME_EDIT,username)
        self.input(self.PASSWORD_EDIT,pwd)
        self.input(self.CODE,code)
        self.click(self.LOGIN_BTN)

    def assert_login_fail(self):
        return self.__find_ele(self.LOGIN_FAIL_HINT)

login_page = LoginPage()

