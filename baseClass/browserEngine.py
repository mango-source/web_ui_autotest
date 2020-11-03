# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/13
version:1.0.1
discription:初始化浏览器
'''
from selenium import webdriver
from yidaCloud.configs import setting
from yidaCloud.configs import constants
import os

class BrowserEngine(object):
    #浏览器驱动所在的路径
    CHROME = os.path.join(constants.driverPath,'chromedriver.exe')
    FIREFOX = os.path.join(constants.driverPath,'geckdriver.exe')
    IE = os.path.join(constants.driverPath,'IEdriver.exe')
    def __init__(self,driver=None):
        if driver is None:
            self.driver = setting.default_browser
        else:
            self.driver = driver
        self._driver = None
    def init_browser(self):
        #初始化浏览器
        if self.driver.lower() == 'chrome':
            self._driver = webdriver.Chrome(executable_path=self.CHROME)
        elif self.driver.lower() == 'firefox':
            self._driver = webdriver.Firefox(executable_path=self.FIREFOX)
        elif self.driver.lower() == 'ie':
            self._driver = webdriver.Ie(executable_path=self.IE)
        else:
            ValueError('浏览器类型错误，当前支持的浏览器为Chrome/Firefox/Ie')
        self._driver.implicitly_wait(1)

        return self._driver  #返回浏览器对象

if __name__ == '__main__':
    BE = BrowserEngine()
    driver = BE.init_browser()
    driver.get('https://www.baidu.com')
