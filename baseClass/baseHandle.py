# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/13
version:1.0.1
discription:封装页面基础方法
'''
from random import Random
import time,os,shutil
from yidaCloud.baseClass.logConfig import do_logger
class BaseHandle():
    def __init__(self):
        pass
    def randomChoice(self,scope):
        '''
        从指定的范围中随机选择一个值
        :param scope: 随机选择的范围
        :return: 随机选择的值
        '''
        ran = Random()
        return ran.choice(scope)
    def clear_dir(self,path):
        '''
        清空文件夹
        :param path: 需要被清空的文件夹
        :return:
        '''
        filelist = os.listdir(path)  #获取文件夹下的所有文件
        for file in filelist:
            fullfile = os.path.join(path,file)
            if os.path.isfile(fullfile):
                os.remove(fullfile)
            elif os.path.isdir(fullfile):
                shutil.rmtree(fullfile)
        do_logger.info('已清空文件夹%s'%path)
    def mkdir(self):
        pass


handle = BaseHandle()
if __name__ == '__main__':
    handle.clear_dir(r'D:\Projects\webTest\yidaCloud\report')