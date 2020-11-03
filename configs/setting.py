# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/13
version:1.0.1
discription:配置信息
'''


#浏览器初始化
default_browser = 'Chrome'   #默认浏览器
ui_wait_time = 5  #最长等待时间

#登录信息
url = 'http://120.79.45.137:81/login'
username = 'test'
password = 123456

#日志信息
logger_name = 'testCase'
logger_level = 'DEBUG'
console_level = 'ERROR'
file_level = 'INFO'
log_filename = 'testcase.log'
simple_formatter = '%(asctime)s-[%(levelname)s]-msg:%(message)s'
normal_formatter = '%(asctime)s %(levelname)s %(filename)s-%(lineno)s msg:%(message)s'


#接口相关信息
project_url = 'https://uat.yidayuntu.cn:9982'

