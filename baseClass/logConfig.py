# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/13
version:1.0.1
discription:初始化日志文件
'''
import logging,os,time
from yidaCloud.configs import setting
from yidaCloud.configs.constants import logPath
class loggingComdat():
    def __init__(self):

        self.logger = logging.getLogger(setting.logger_name)  #初始化日志对象
        self.logger.setLevel(setting.logger_level) #设定日志的信息级别
        #设定控制台输出日志信息
        console_log = logging.StreamHandler() #初始化控制台信息
        console_log.setLevel(setting.console_level)
        simple_formatter = logging.Formatter(setting.simple_formatter) #初始化日志格式
        console_log.setFormatter(simple_formatter) #设定日志格式
        self.logger.addHandler(console_log)  #将控制台作为日志输出通道

        #设定日志输出到日志文件
        #设计日志文件的名字
        now = time.strftime('%y-%m-%d',time.localtime())
        file_name = 'test_result_%s.log'%now
        log_file_name = os.path.join(logPath,file_name)
        self.file_log = logging.FileHandler(log_file_name,encoding='utf-8')  #初始化日志文件
        self.file_log.setLevel(setting.file_level)
        normal_formatter = logging.Formatter(setting.normal_formatter) #初始化日志格式
        self.file_log.setFormatter(normal_formatter) #将日志格式应用到日志文件中
        self.logger.addHandler(self.file_log) #将日志文件作为日志输出通道

    def get_logger(self):
        return self.logger

    def close_log(self):
        self.logger.removeHandler(self.file_log)  #移除日志输出
        self.file_log.close()

do_logger = loggingComdat().get_logger()

if __name__ == '__main__':

    do_logger.error('这是一个错误')
    do_logger.info('这是一个正确的信息')

