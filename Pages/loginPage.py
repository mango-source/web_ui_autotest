# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:封装登录页面
'''
from selenium import webdriver
from yidaCloud.baseClass.bassPage import Page
from yidaCloud.baseClass.browserEngine import BrowserEngine
from yidaCloud.configs.constants import url,username,passsword
import time
class LoginPage(Page):
    def cookie_login(self):
        '''
        执行登录操作
        :return:
        '''
        self.get_url(url)
        time.sleep(3)
        self.login(username,passsword)

    def input_username(self,username=None):
        '''
        输入用户名
        :param username: 用户名
        :return:
        '''
        self.input_text('登录','用户名',username)
    def input_password(self,password=None):
        '''
        输入密码
        :param password: 密码
        :return:
        '''
        self.input_text('登录','密码',password)
    def submit(self):
        '''
        点击登录按钮
        :return: 无
        '''
        self.click_element('登录','登录按钮')
    def login(self,username=None,password=None):
        '''
        登录方法
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        self.input_username(username)
        self.input_password(password)
        self.submit()
    def get_index_username(self):
        '''
        获取登录后首页的用户名
        :return:
        '''
        name = self.get_text('首页','用户名')
        return name
    def get_error_message(self):
        '''
        获取登录错误时的提示信息
        :return:
        '''
        time.sleep(1)
        msg = self.get_text('登录','错误提示')
        return msg

if __name__ == '__main__':
    be = BrowserEngine()
    driver = be.init_browser()
    Login = LoginPage(driver)
    Login.get_url('https://uat.yidayuntu.cn/login')
    Login.login('test','1234567')
    msg = Login.get_error_message()
    print(msg)
