# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:登录页面测试用例
'''
import pytest,allure,os
from yidaCloud.Pages.loginPage import LoginPage
from yidaCloud.baseClass.logConfig import do_logger,loggingComdat
from yidaCloud.baseClass.browserEngine import BrowserEngine
from yidaCloud.baseClass.bassPage import Page
from yidaCloud.configs.constants import url
@allure.feature('登录页面用例')
class TestLogin():
    def setup_class(self):

        do_logger.info('开始执行登录页面测试用例')

    def setup(self):
        #准备工作
        self.driver = BrowserEngine().init_browser()
        self.Login = LoginPage(self.driver)
        self.page = Page(self.driver)
        self.page.get_url(url)

    @allure.story('正常登录')
    def test_login_normal(self):
        self.Login.login('test','123456')
        username = self.Login.get_index_username()
        assert username == '测试专用'

    @allure.story('登录时密码错误')
    def test_login_error(self):
        self.Login.login('test','12345')
        message = self.Login.get_error_message()
        assert message == '用户名或者密码不正确，请重试！'

    @allure.story('登录时用户名错误')
    def test_login_error_2(self):
        self.Login.login('test123','123456')
        message = self.Login.get_error_message()
        print(message)
        assert message == '用户名或者密码不正确，请重试！'


    def teardown(self):
        self.page.close_browser()

    def teardown_class(self):
        do_logger.info('登录页面测试用例执行结束')
        loggingComdat().close_log()
if __name__ == '__main__':
    pytest.main(['test_login.py','--alluredir','../allure/'])
    os.system('allure generate D:\\Projects\\webTest\\yidaCloud\\allure\\ '
              '-o D:\\Projects\\webTest\\yidaCloud\\report\\ --clean')