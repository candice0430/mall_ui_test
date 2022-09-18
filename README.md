# mall_ui_test
1、selenium.common.exceptions.WebDriverException: Message: Can not connect to the Service chromedriver
https://blog.csdn.net/qq_32151639/article/details/78457921
2、遇到有iframe时，需要切换iframe
3、元素定位调试方法：
    - 在html页面中点击f12
    - 选中元素
    - 切换到console控制台
    - 输入$x('//div[@class="btns"]/div[3]')--->查找div中class为btns下的第三个div元素
      输入$x('//*[@id="username"]')
4、select选择练习:
    - select_by_value：通过value值选中元素
    - select_by_index:通过下标选中元素，下标从0开始
    - select_by_visibile_text：通过值选中元素
