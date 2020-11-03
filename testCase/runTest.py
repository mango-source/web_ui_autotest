# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:执行测试用例
'''

import pytest,os
# 1.执行所有测试用例

pytest.main(['-s',r'D:\Projects\webTest\yidaCloud\testCase','--alluredir','../allure/'])
os.chdir(r'D:\Projects\webTest\yidaCloud\testCase')
os.system('allure generate ../allure/ -o ../report/ --clean')
