# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/13
version:1.0.1
discription:封装页面基础方法
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from yidaCloud.configs.setting import ui_wait_time
from yidaCloud.configs.getIniValue import do_config
from yidaCloud.baseClass.logConfig import do_logger  #日志模块
import time,os,shutil
from random import Random
class Page():
    def __init__(self,driver):
        self.driver = driver
    def get_url(self,url):
        '''
        打开网址
        :param url: 网址信息
        :return:
        '''
        self.driver.get(url)
        self.driver.maximize_window()
        # return url
    def getElementInfo(self,section,option):
        '''
        获取ini文件中的元素定位信息
        :param section:一级标签，例如:登录
        :param option:二级标签，例如：username
        :return:
        '''
        local_info = do_config.get_value(section,option)
        localInfo = local_info.split(':')
        return localInfo  #返回元素信息

    def findElement(self,by,value):
        '''
        定位元素，并返回元素对象
        :param by: 定位方式
        :param value: 定位方式对应的值
        :return: 元素对象
        '''
        try:
            if by == 'id':
                return WebDriverWait(self.driver,ui_wait_time,0.5).until(
                    EC.presence_of_element_located((By.ID,value))
                )
            elif by == 'name':
                return WebDriverWait(self.driver,ui_wait_time,0.5).until(
                    EC.presence_of_element_located((By.NAME,value))
                )
            elif by == 'xpath':
                return WebDriverWait(self.driver, ui_wait_time, 0.5).until(
                    EC.presence_of_element_located((By.XPATH, value))
                )
            elif by == 'css_selector':
                return WebDriverWait(self.driver, ui_wait_time, 0.5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, value))
                )
            elif by == 'link_text':
                return WebDriverWait(self.driver, ui_wait_time, 0.5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, value))
                )
            else:
                do_logger.error('定位方式错误，请选择其他定位方式')

        except:
            do_logger.error('元素定位失败<%s::%s>'%(by,value))

    def findElements(self,by,value):
        '''
        定位一组元素，并返回元素对象列表
        :param by: 定位方式
        :param value: 定位方式对应的值
        :return: 元素对象列表
        '''
        try:
            if by == 'id':
                return WebDriverWait(self.driver,ui_wait_time,0.5).until(
                    EC.presence_of_all_elements_located((By.ID,value))
                )
            elif by == 'name':
                return WebDriverWait(self.driver,ui_wait_time,0.5).until(
                    EC.presence_of_all_elements_located((By.NAME,value))
                )
            elif by == 'xpath':
                return WebDriverWait(self.driver, ui_wait_time, 0.5).until(
                    EC.presence_of_all_elements_located((By.XPATH, value))
                )
            elif by == 'css_selector':
                return WebDriverWait(self.driver, ui_wait_time, 0.5).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, value))
                )
            elif by == 'link_text':
                return WebDriverWait(self.driver, ui_wait_time, 0.5).until(
                    EC.presence_of_all_elements_located((By.LINK_TEXT, value))
                )
            else:
                do_logger.error('元素定位方式选择错误，请更换')


        except:
            do_logger.error('元素定位失败<%s::%s>'%(by,value))



    def input_text(self,section,option,text,clear=True):
        '''
        输入文本
        :param section:localElement.ini文件中的一级标签
        :param option:二级标签
        :return:
        '''

        by,value = self.getElementInfo(section,option)
        if clear:
            self.findElement(by,value).clear()
            self.findElement(by,value).send_keys(text)
        else:
            self.findElement(by, value).send_keys(text)
        do_logger.info('输入文本正常 : %s : %s : %s'%(section,option,text))
    def click_element(self,section,option):
        '''
        点击元素
        :param section:localElement.ini文件中的一级标签
        :param option:二级标签
        :return:
        '''
        by,value = self.getElementInfo(section,option)
        self.findElement(by,value).click()
        do_logger.info('点击元素正常 : %s : %s'%(section,option))
    def get_text(self,section,option):
        '''
        获取元素中的文本
        :param section: localElement.ini文件中的一级标签
        :param option: 二级标签
        :return:
        '''
        by,value = self.getElementInfo(section,option)
        message = self.findElement(by,value).text
        do_logger.info('获取文本正常 : %s : %s : %s'%(section,option,message))
        return message

    def close_browser(self):
        '''
        关闭浏览器
        :return:
        '''
        self.driver.close()

    def get_errorMsg(self):
        '''
        获取错误提示信息
        :return:
        '''
        try:
            time.sleep(1)
            msg = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/p').text
            do_logger.info('获取提示信息成功 : %s' %msg)
            return msg
        except:
            do_logger.error('无法获取提示信息')
    def get_successMsg(self):
        '''
        获取错误提示信息
        :return:
        '''
        try:
            time.sleep(1)
            msg = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/p').text
            do_logger.info('获取提示信息成功 : %s' %msg)
            return msg
        except:
            do_logger.error('无法获取提示信息')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://uat.yidayuntu.cn/login?from=%2F')
    p = Page(driver)
    # print(p.get_text('登录','登录按钮'))
    # driver.implicitly_wait()
    # p.clear_dir(r'D:\Projects\webTest\yidaCloud\allure')