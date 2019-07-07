# coding:utf8
from selenium import webdriver
import time


class Web:

    def __init__(self):
        #打开浏览器
        self.drvier = webdriver.Chrome(executable_path='lib/chromedriver.exe')


    def close(self):
        # 等待3秒然后退出
        time.sleep(3)
        self.drvier.quit()