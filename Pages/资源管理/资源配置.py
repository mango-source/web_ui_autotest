# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:封装资源配置页面
'''
from yidaCloud.baseClass.bassPage import Page
from yidaCloud.yidaCloudApi.business import buinessApi
from yidaCloud.baseClass.baseHandle import handle
from time import sleep
class ResourcePage(Page):
    def search(self,value):
        '''
        资源配置页面搜索功能
        :param value: 搜索的内容
        :return:
        '''
        self.input_text('资源配置','搜索',value)
    def newFenqi(self):
        '''
        点击新建分期
        :return:
        '''
        self.click_element('资源配置','新建分期')
    def newBuilding(self):
        '''
        点击新建楼宇
        :return:
        '''
        self.click_element('资源配置','新建楼宇')
    def fenqiNum(self,num):
        '''
        输入分期数
        :param num:分期数
        :return:
        '''
        self.input_text('资源配置','分期数',num)
    def fenqiName(self,name):
        '''
        输入分期别名
        :param name:分期名
        :return:
        '''
        self.input_text('资源配置','分期别名',name)
    def fenqiArea(self,area):
        '''
        输入分期面积
        :param area:面积
        :return:
        '''
        self.input_text('资源配置','建筑面积',area)
    def fenqiRate(self,rate):
        '''
        输入分期容积率
        :param rate: 容积率
        :return:
        '''
        self.input_text('资源配置','容积率',rate)
    def clickSubmit(self):
        '''
        创建分期时点击保存
        :return:
        '''
        self.click_element('资源配置','保存')
    def get_message(self):
        '''
        获取点击保存后的提示信息
        :return:
        '''
    def get_fenqiNum(self,projectId):
        '''
        获取当前项目所有的分期数
        :param projectId:项目ID,从数据库中查询
        :return: 当前项目所有的分期数
        '''
        res = buinessApi.listBuilding(projectId)  #查询分期详情接口
        fenqiNum = []
        for i in res['data']['parkProjectSubList']:
            fenqiNum.append(i['projectStage'])  #获取所有分期数
        return fenqiNum
    def randomFenqi(self,projectId):
        '''
        从指定项目中随机选择已经存在的分期数
        :param projectId: 项目id
        :return: 随机选择的分期数
        '''
        return handle.randomChoice(self.get_fenqiNum(projectId))


if __name__ == '__main__':
    pass
