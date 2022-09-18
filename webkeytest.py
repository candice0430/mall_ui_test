# -*- coding: utf-8 -*-
import mywebkeys

web = mywebkeys.WebKeys()
web.driver.implicitly_wait(10)


# 登录
web.get_url('http://testingedu.com.cn:8000/Home/user/login.html')
web.input('username','13800138006')
web.input('password','123456')
web.input('verify_code','123456')
web.click('//a[@class="J-login-submit"]')


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
# web.click('province')
web.select_by_text('province','广东省')
# web.click('city')
web.select_by_text('city','深圳市')
# web.click('district')
web.select_by_text('district','南山区')
web.input('//input[@name="address"]','哈哈哈哈哈地址来了')
web.click('address_submit')

web.sleep(3)

# 删除地址
web.click('//span[text()="雪儿"]/../..//a[text()="删除"]')



web.quit()