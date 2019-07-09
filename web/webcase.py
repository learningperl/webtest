# coding:utf8
from selenium import webdriver
import time


class Web:

    def __init__(self):
        #打开浏览器
        self.drvier = webdriver.Chrome(executable_path='lib/chromedriver.exe')

    #上传文件
    def upload(self):
        self.drvier.implicitly_wait(20)
        self.drvier.get('https://www.baidu.com/')
        self.drvier.find_element_by_xpath('//*[@id="form"]/span[1]/span').click()
        self.drvier.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys('F:/git/webtest/lib/1.png')
        time.sleep(5)


    def close(self):
        # 等待3秒然后退出
        time.sleep(3)
        self.drvier.quit()