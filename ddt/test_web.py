import pytest
import os
import sys
import allure
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
from utils.file_handle import FileHandle
import yaml
from po.base_page import BasePage


print("comein=======")
data_file_path = FileHandle.absolute_path('testcases','login.yaml')
print(data_file_path)
f = open(data_file_path,'r',encoding='utf-8')
logincases = yaml.safe_load(f)
print(logincases)

class TestLogin:

    def setup_class(self):
        self.web = BasePage()
        self.web.open_browser()

    @allure.step
    def run_steps(self,func,args):
        func(*args)

    def run_case(self,logincases:dict):
        allure.dynamic.title(logincases['title'])
        allure.dynamic.description(logincases['desc'])
        steps = logincases['steps']
        print("++++++++++++++++++")
        print(logincases.keys())
        if 'Page' in logincases.keys():
            page = logincases['Page']
            mod = 'po.%s'%page
            print("mod:",mod)
            dd = __import__(mod,fromlist = True)
            self.web = getattr(dd,page)
        try:
            for step in steps:
                func = self.web.__getattribute__(step['method'])
                caselists = list(step.values())
                with allure.step(step['name']):
                    self.run_steps(func,caselists[2:])
        except Exception as e:
            print(str(e))
            pytest.fail('用例不通过')

    @allure.story('登录')
    @pytest.mark.parametrize('logincases',logincases)
    def test_login(self,logincases):
        self.run_case(logincases)

    def teardown_class(self):
        self.web.quit()
            
if __name__ == '__main__':
    pytest.main(['-s','./testcases/test_login.py', '--alluredir','./temp'])
    os.system('allure generate ./temp -o ./report --clean')

