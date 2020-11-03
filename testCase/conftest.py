# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:测试用例前置步骤
'''

import pytest
from yidaCloud.baseClass.logConfig import do_logger
from yidaCloud.Pages.loginPage import LoginPage
from yidaCloud.baseClass.browserEngine import BrowserEngine

@pytest.fixture()
def login():
    do_logger.info('执行登录步骤')
    driver = BrowserEngine().init_browser()
    LoginPage(driver).cookie_login()