# -*- coding: utf-8 -*-
import mywebkeys

web = mywebkeys.WebKeys()
web.driver.implicitly_wait(10)
web.driver.maximize_window()

# 登录
web.get_url('http://testingedu.com.cn:8000/Home/user/login.html')
web.input('username','13800138006')
web.input('password','123456')
web.input('verify_code','123456')
web.click('//a[@class="J-login-submit"]')
web.sleep(1)

# 修改头像
web.sleep(1)
web.get_url("http://testingedu.com.cn:8000/Home/User/info.html")
web.click_js('preview')
web.sleep(1)


web.into_iframe('//*[@id="layui-layer-iframe1"]')
web.sleep(1)
web.input('//*[@id="filePicker"]/div[2]/input',r"/Users/mac/Downloads/images.jpeg")
web.wait_until('//span[text()="100%"]')
web.click('//div[@class="saveBtn"]')
web.out_to_iframe()
web.click('//*[@value="确认保存"]')


# 新增地址
web.get_url('http://testingedu.com.cn:8000/Home/User/address_list.html')
web.click('//span[text()="增加新地址"]')
web.input('//input[@name="consignee"]','雪儿')
web.input('//input[@name="mobile"]','13322932002')
web.select_by_text('province','广东省')
web.select_by_text('city','深圳市')
web.select_by_text('district','南山区')
web.input('//input[@name="address"]','哈哈哈哈哈地址来了')
web.click('address_submit')

web.sleep(3)

# 删除地址
web.click('//span[text()="雪儿"]/../..//a[text()="删除"]')
web.sleep(1)

# 搜索手机
web.get_url('http://testingedu.com.cn:8000/Home/Goods/search.html')
web.sleep(1)
web.input('q','手机')
web.sleep(1)
web.click('//button[@class="ecsc-search-button"]')
web.sleep(2)

#获取所有商品名字

# 添加购物车
web.click('//a[contains(text(),"Huawei/华为 nova 2s")]')
web.sleep(1)
web.click('join_cart')
# 关闭弹窗
web.sleep(1)
web.click('//span[@class="layui-layer-setwin"]/a')
#去结算
web.move_to_ele('//span[text()="我的购物车"]')
web.sleep(1)
web.click('//a[contains(text(),"去购物车结算")]')
web.click('//a[@class="paytotal"]')
web.sleep(1)
web.click('//button[@class="checkout-submit"]')
web.sleep(1)
order_number = web.get_order_number('//p[@class="succ-p"]','\d{18}')

#取消订单
web.get_url('http://testingedu.com.cn:8000/index.php/Home/Order/order_list.html')
web.sleep(2)
locator = '//em[text()="%s"]/../..//a[text()="取消订单"]'%order_number
web.click(locator)
web.click('//a[text()="确定"]')
web.sleep(3)
web.quit()