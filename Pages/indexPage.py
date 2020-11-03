# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:封装慧云首页
'''
from yidaCloud.baseClass.bassPage import Page

class IndexPage(Page):

    def click_door(self):
        '''
        点击首页中的门户
        :return:
        '''
        self.click_element('首页','门户')
    def click_business(self):
        '''
        点击首页中的招商
        :return:
        '''
        self.click_element('首页','招商')
    def click_operate(self):
        '''
        点击首页中的运营
        :return:
        '''
        self.click_element('首页','运营')
    def click_property(self):
        '''
        点击首页中的物业
        :return:
        '''
        self.click_element('首页','物业')

    def click_finance(self):
        '''
        点击首页中的财务
        :return:
        '''
        self.click_element('首页', '财务')
    def click_enterprise(self):
        '''
        点击首页中的企服
        :return:
        '''
        self.click_element('首页', '企服')
    def click_setting(self):
        '''
        点击首页中的企服
        :return:
        '''
        self.click_element('首页', '设置')
    def click_project(self):
        '''
        点击首页中的项目
        :return:
        '''
        self.click_element('首页', '项目')