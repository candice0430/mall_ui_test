from ssl import OPENSSL_VERSION_INFO
import pytest
import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
from utils.file_handle import FileHandle
import yaml
from mywebkeys import WebKeys

data_file_path = FileHandle.absolute_path('testdatas','login.yaml')
f = open(data_file_path,'r')
logincases = yaml.safe_load(f)
print(logincases)

class TestLogin:

    def setup_class(self):
        self.web = WebKeys()
        self.web.open_browser()

    def run_steps(self,func,args):
        func(*args)

    def run_case(self,logincases):
        steps = logincases['steps']
        try:
            for step in steps:
                func = self.web.__getattribute__(step['method'])
                caselists = list(step.values())
                self.run_steps(func,caselists[2:])
        except Exception as e:
            pytest.fail('用例不通过')

    @pytest.mark.parametrize('logincases',logincases)
    def test_login(self,logincases):
        self.run_case(logincases)
            

