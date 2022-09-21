import pytest
import os
import sys
import allure
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
from utils.file_handle import FileHandle
import yaml
from mywebkeys import WebKeys

data_file_path = FileHandle.absolute_path('testdatas','login.yaml')
f = open(data_file_path,'r',encoding='utf-8')
logincases = yaml.safe_load(f)
print(logincases)

class TestLogin:

    def setup_class(self):
        self.web = WebKeys()
        self.web.open_browser()

    @allure.step
    def run_steps(self,func,args):
        func(*args)

    def run_case(self,logincases):
        allure.dynamic.title(logincases['title'])
        allure.dynamic.description(logincases['desc'])
        steps = logincases['steps']
        try:
            for step in steps:
                func = self.web.__getattribute__(step['method'])
                caselists = list(step.values())
                with allure.step(step['name']):
                    self.run_steps(func,caselists[2:])
        except Exception as e:
            allure.attach(self.web.driver.get_screenshot_as_png(),'用例报错图',allure.attachment_type.PNG)
            print(str(e))
            pytest.fail('用例不通过')
        allure.attach(self.web.driver.get_screenshot_as_png(),'用例结果图',allure.attachment_type.PNG)

    @allure.feature('登录')
    @pytest.mark.parametrize('logincases',logincases)
    def test_login(self,logincases):
        self.run_case(logincases)

    def teardown_class(self):
        self.web.quit()
            
if __name__ == '__main__':
    pytest.main(['-s','./testcases/test_login.py', '--alluredir','./temp'])
    os.system('allure generate ./temp -o ./report --clean')

