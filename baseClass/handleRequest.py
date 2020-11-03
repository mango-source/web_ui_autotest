# -*-coding:utf-8-*-
'''
author:wangjvv
date:2020/7/16
version:1.0.1
discription:封装访问接口方法
'''
import requests,json
from yidaCloud.baseClass.logConfig import do_logger
class HandleRequest():
    def __init__(self):
        self.session = requests.session()  #新建请求对象

    def request(self,method,url,data=None,**args):
        '''
        封装接口请求访问方法
        :param method: 接口请求使用的访问方法
        :param url: 请求地址
        :param data: 请求参数，参数为字典格式
        :return:
        '''
        if method.upper() == 'GET':
            result = self.session.request(method='GET',url=url,params=data,**args)
        elif method.upper() == 'POST':
            result = self.session.request(method='POST',url=url,data=data,**args)
        elif method.upper() == 'OPTIONS':
            result = self.session.request(method='OPTIONS',url=url,data=data,**args)
        else:
            result  = None
            do_logger.error('暂不支持%s请求方法，请确认后重试'%method)
        return json.loads(result.text)
    def close_session(self):
        self.session.close()  #关闭当前请求

Request = HandleRequest()

if __name__ == '__main__':
    data = {'username':'test',
            'password':123456,
            'grant_type':'password'}
    url = 'https://uat.yidayuntu.cn:9982/oauthep/uaa/oauth/token'
    method = 'post'
    res = Request.request(method=method,url=url,data=data)
    print(res['access_token'])
    print()
