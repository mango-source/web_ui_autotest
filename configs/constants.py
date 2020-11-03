# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/10
version:1.0.1
discription:定义脚本执行过程中使用到的常量
'''

import os
'''项目路径相关常量'''

#获取当前项目路径
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(projectPath)

#浏览器驱动路径
driverPath = os.path.join(projectPath,'drivers')

#测试用例所在的路径
casePase = os.path.join(projectPath,'testCase')

#元素定位文件所在的路径
localInfo = os.path.join(projectPath,'configs\localElement.ini')

#日志文件所在的路径
logPath = os.path.join(projectPath,'log')

'''项目用户相关常量'''
url = 'https://uat.yidayuntu.cn/login'
username = 'test'
passsword = '123456'