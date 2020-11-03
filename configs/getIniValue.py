# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/13
version:1.0.1
discription:读取ini文件中的内容
'''
from configparser import ConfigParser  #读取ini文件的包
from yidaCloud.configs.constants import localInfo   #ini文件所在的路径

class GetIniValue():
    def __init__(self,filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename,encoding='utf-8')  #读取ini文件
    def get_value(self,section,option):
        return self.config.get(section,option)  #通过section、option读取参数值

    def get_IntValue(self,section,option):
        return self.config.getint(section,option)

    def get_FloatValue(self,section,option):
        return self.config.getfloat(section,option)

    def get_BooleanValue(self,section,option):
        return self.config.getboolean(section,option)

do_config = GetIniValue(localInfo)

if __name__ == '__main__':
    element  = do_config.get_value('登录','username')
    print(element)
    elements = element.split(':')
    print(elements)