import os
import json

def get_pic_info():
    picInfoPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config\\", "picInfo.json")
    with open(picInfoPath, 'r', encoding='utf-8') as f:
        picInfo = json.load(f)
    return picInfo

def get_locator_info():
    locatorPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config\\", "locatorInfo.json")
    with open(locatorPath, 'r', encoding='utf-8') as f:
        locatorInfo = json.load(f)
    return locatorInfo

class GlobalManager(object):

    globaldict = {}
    _instance = False

    def __init__(self):
        self.globaldict['rootPath'] = os.path.dirname(os.path.dirname(__file__))
        self.globaldict['picInfo'] = get_pic_info()
        self.globaldict['locatorInfo'] = get_locator_info()

    def get_value(self, name):
        try:
            return self.globaldict[name]
        except KeyError as e:
            print("获取的变量名称不存在！！！！！！！！！！！！！！！")
            return None

    def set_value(self, name, value):
        self.globaldict[name] = value

    def __new__(cls, *args, **kwargs):
        if cls._instance == False:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

