#!/usr/bin/python
# -*- coding:utf-8 -*-

import yaml
import os


def readyml(yamlPath):
    '''读取yaml文件内容
    realPath: 文件的真实绝对路径 '''
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    # open方法打开直接读出来
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg)
    # 用load方法转字典
    print("读取的测试文件数据：%s"%d)
    return d

if __name__ == '__main__':
    data = readyml("E:\\PyProject\\pytestStudy\\case\\test_data.yml")