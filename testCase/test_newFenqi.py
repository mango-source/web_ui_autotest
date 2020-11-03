# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:新建分期测试用例
'''
from yidaCloud.baseClass.browserEngine import BrowserEngine
from yidaCloud.Pages.indexPage import IndexPage
from yidaCloud.Pages.loginPage import LoginPage
from yidaCloud.Pages.资源管理.资源配置 import ResourcePage
from yidaCloud.baseClass.logConfig import do_logger
from yidaCloud.yidaCloudApi.business import buinessApi
import pytest,allure
from time import sleep
@allure.feature('新建分期')
class TestNewFenqi():
    def setup_class(self):
        do_logger.info('开始执行新建分期测试用例')
        self.driver = BrowserEngine().init_browser()  #打开浏览器
        LoginPage(self.driver).cookie_login()  #登录
        self.index = IndexPage(self.driver)
        self.resource = ResourcePage(self.driver)
    def setup_method(self):
        #执行用例前刷新页面
        self.index.click_business() #点击招商

        sleep(2)
    @allure.story('正常新建分期')
    def test_newFenqi_nromal(self):
        self.resource.newFenqi() #点击新建分期
        self.resource.fenqiNum(20)
        self.resource.fenqiName('2020新建分期')
        self.resource.fenqiArea(100000)
        self.resource.fenqiRate(20)
        self.resource.clickSubmit()
        assert 20 in self.resource.get_fenqiNum(130) and self.resource.get_successMsg() == '数据保存成功！'
    @allure.story('分期数已存在')
    def test_newFenqi_exist(self):
        self.resource.newFenqi()  # 点击新建分期
        num = self.resource.randomFenqi(130)
        self.resource.fenqiNum(num)
        self.resource.fenqiName('2020新建分期')
        self.resource.fenqiArea(100000)
        self.resource.fenqiRate(20)
        self.resource.clickSubmit()
        assert self.resource.get_errorMsg() == '项目分期已存在'

    def teardown_method(self):
        sleep(1)
        self.driver.refresh()
    def teardown_class(self):
        self.driver.close()
        do_logger.info('新建分期测试用例执行结束')

if __name__ == '__main__':
    pytest.main(['-s','test_newFenqi.py','--alluredir','../allure/'])

