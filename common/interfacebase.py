#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests

class InterfaceBase():
    '''接口测试工具类'''

    def post_main(self,url,data,header=None):
        '''post请求'''
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def get_main(self,url,data=None,header=None):
        '''get请求'''
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url, data=data).json()
        return res

    def run_main(self,method,url,data=None,header=None):
        '''自定义请求'''
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        elif method == 'get':
            res = self.get_main(url,data,header)
        else:
            print("该方式暂未支持")
        return res

