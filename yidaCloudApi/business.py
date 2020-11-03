# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:封装自动化测试过程中使用到的招商模块接口访问方法
'''
from yidaCloud.baseClass.handleRequest import Request
from yidaCloud.configs.setting import username,password,project_url
from yidaCloud.baseClass.logConfig import do_logger
class BuinessApi():
    # def __init__(self):
    #     self.pro_url = project_url
    def token(self,username,password):
        '''
        登录接口
        :param username: 用户名
        :param password: 密码
        :return: 登录接口返回的数据
        '''
        try:
            data = {'username':username,'password':password,'grant_type':'password'}
            login_url = project_url+'/oauthep/uaa/oauth/token'
            res = Request.request('post',login_url,data)
            return res
        except:
            do_logger.error('登录接口访问失败')
    def listBuilding(self,projectId):
        '''
        通过项目ID获取项目详情
        :param projectId: 项目ID
        :return: 项目详情
        '''

        url = project_url+'/resource/building/listBuildingByProjectId?'
        data = {'projectId':projectId}

        header = {'Authorization':'Bearer '+self.token(username,password)['access_token']}
        res = Request.request('get',url,data,headers=header)
        return res
    def listBuildingBySubProjectId(self,subprojectId):
        '''
        通过分期id获取分期详情
        :param subprojectId: 分期id
        :return: 分期详情
        '''
        url = project_url+'/resource/building/listBuildingBySubProjectId?'
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        data = {'subProjectId':subprojectId,'buildingName':''}
        res = Request.request('get',url,data=data,headers=header)
        return res
    def listByProjectId(self,projectId):
        '''
        通过项目id获取项目详情，并获取第一个分期的建筑列表
        :param projectid:项目Id
        :return:项目详情
        '''
        url = project_url + '/resource/resource/ParkProjectSub/listByProjectId?'
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        data = {'projectId': projectId, 'buildingName':''}
        res = Request.request('get', url, data=data, headers=header)
        return res

    def projects(self):
        '''
        获取当前账号下的项目以及项目列表
        :return:
        '''
        url = project_url + '/customerQuery/security_v2/user/projects'
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        res = Request.request('get', url, headers=header)
        return res

    def list_unread(self,projectId):
        '''
        获取当前项目下的所有未读消息
        :param projectId:项目id
        :return:
        '''
        url = project_url + '/customerQuery/index/list_unread?'
        data = {'projectId':projectId,'pageSize':20,'pageNo':1}
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        res = Request.request('get', url,data=data,headers=header)
        return res
    def addFenqi(self,stage,stageName,projectId):
        '''
        新建分期
        :param stage:分期数 不可重复
        :param stageName: 分期名
        :return:
        '''
        url = project_url + '/resource/resource/projectStage/add'
        data = {'projectStage': stage, 'projectStageName': stageName, 'projectId': projectId,
                'planArchitectureArea':5000,'capacityRate':20}
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        res = Request.request('post', url, data=data, headers=header)
        return res
    def modifyFenqi(self,id,projectStage,projectStageName,projectId=130):
        '''
        修改分期接口
        :param id: 分期id 仅支持当前数据库中存在的
        :param projectStage:分期数 不可重复
        :param projectStageName:分期名
        :param projectId:项目id
        :return:
        '''
        url = project_url + '/resource/resource/projectStage/modify'
        data = {'id':id,'projectStage': projectStage, 'projectStageName': projectStageName, 'projectId': projectId,
                'planArchitectureArea': 5000, 'capacityRate': 20}
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        res = Request.request('post', url, data=data, headers=header)
        return res
    def deleteFenqi(self,projectSubId):
        '''
        删除分期
        :param projectSubId: 分期id
        :return:
        '''
        url = project_url + '/resource/resource/ParkProjectSub/project_sub/delete?'
        data = {'projectSubId': projectSubId,}
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        res = Request.request('options', url, data=data, headers=header)
        return res
    def addBuilding(self,subPorjectId,buildingName,upFloor,underFloor,liftNum):
        '''
        添加楼栋
        :param subPorjectId: 分期id
        :param buildingName: 楼栋名
        :param upFloor: 地上楼层数
        :param underFloor: 地下楼层数
        :param liftNum: 电梯数量
        :return:
        '''
        url = project_url + '/resource/building/add'
        data = {'subPorjectId': subPorjectId,'buildingName':buildingName,'upFloorLevel':upFloor,
                'undefFloorLevel':underFloor,'liftNum':liftNum}
        header = {'Authorization': 'Bearer ' + self.token(username, password)['access_token']}
        res = Request.request('options', url, data=data, headers=header)
        return res

buinessApi = BuinessApi()

if __name__ == '__main__':
    # ba = BuinessApi()
    # result = ba.listBuilding(130)
    # fenqiNum = []
    # res = result['data']['parkProjectSubList']
    # for i in res:
    #     fenqiNum.append(i['projectStage'])
    # print(fenqiNum)
    res = buinessApi.addFenqi(21,'2020新建分期',130)
    print(res)