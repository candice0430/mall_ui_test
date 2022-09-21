import os
import sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
from po.driver_factory import DriverFactory

if __name__ == '__main__':
    print("aaa")
    c = input('请输入想导入的模块名:')
    m = "po.%s"%c
    print(m)
    d = __import__(m,fromlist=True)
    cc = getattr(d,c)
    cc(DriverFactory.get_driver())