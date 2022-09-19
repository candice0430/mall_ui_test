import re

s = ' 订单号：  202209191858389687    |     付款金额（元）：100元'
d = re.findall('\d{18}',s)[0]
print(d)