
'''接口测试'''
import requests

params = {'username':'张三'}
url = 'https://www.baidu.com'
response = requests.get(url=url,params=params)

