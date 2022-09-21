import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
from po.login_page import login_page
if __name__ == '__main__':
    print("aaa")
    c = input('请输入想导入的模块名:')
    m = "po.%s"%c
    d = __import__(m,fromlist=True)
    getattr(d,"login_page")