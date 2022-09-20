# mall_ui_test
1、selenium.common.exceptions.WebDriverException: Message: Can not connect to the Service chromedriver
https://blog.csdn.net/qq_32151639/article/details/78457921
2、遇到有iframe时，需要切换iframe
3、元素定位调试方法：https://cloud.tencent.com/developer/article/2014328
    - 在html页面中点击f12
    - 选中元素
    - 切换到console控制台
    - 输入$x('//div[@class="btns"]/div[3]')--->查找div中class为btns下的第三个div元素
      输入$x('//*[@id="username"]')
4、select选择练习:
    - select_by_value：通过value值选中元素
    - select_by_index:通过下标选中元素，下标从0开始
    - select_by_visibile_text：通过值选中元素

5、ModuleNotFoundError: No module named 'util'：
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(BASE_PATH)
6、allure使用：
    - pytest --alluredir=./allure-results 只是帮助我们将测试结果创建出来，但是无法生成HTML格式且生成的测试数据不会清空，而是以追加的形式
    - 安装allure 生成html报告：https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/
    allure generate 生成测试结果数据 -o 生成报告的路径 --clean
    # --clean表示：如果已经存在生成报告路径文件夹时，再次使用会提示添加--clean参数来重写
    # 如以下编写用例命令
      allure generate report/ -o report/html --clean
7、allure 报告展示loading和404

7、po
https://selenium-python.readthedocs.io/page-objects.html

