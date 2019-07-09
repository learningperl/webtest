# coding:utf8
from web.webcase import Web
from inter.intercase import Http


# 打开浏览器
web = Web()

#上传文件
web.upload()

web.close()

#接口自动化
http = Http()
http.login()


