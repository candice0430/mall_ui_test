from ast import arg
import pytest
import os
import sys
import allure
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
from utils.file_handle import FileHandle
import yaml
from po.base_page import BasePage
from po.driver_factory import DriverFactory


data_file_path = FileHandle.absolute_path('testcases','case.yaml')
print(data_file_path)
f = open(data_file_path,'r',encoding='utf-8')
logincases = yaml.safe_load(f)
print(logincases)

class TestLogin:

    def setup_class(self):
        self.driver = DriverFactory.get_driver()
        self.driver.maximize_window()
        self.web = BasePage(self.driver)


    @allure.step
    def run_steps(self,func,args={}):
        res = func(*args)
        if res == False:
            pytest.fail('用例不通过')


    def run_case(self,logincases:dict):
        allure.dynamic.title(logincases['usecase'])
        allure.dynamic.description(logincases['desc'])
        steps = logincases['steps']

        if 'page' in logincases.keys():
            page = logincases['page']
            mod = 'po.%s'%page
            dd = __import__(mod,fromlist = True)
            page_class = getattr(dd,page)
            self.web = page_class(self.driver)
        try:
            for step in steps:
                func = self.web.__getattribute__(step['method'])
                with allure.step(step['name']):
                    if 'params' in step.keys():
                        self.run_steps(func,step['params'].values())
                    else:
                        self.run_steps(func)
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

