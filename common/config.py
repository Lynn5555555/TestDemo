import os
from configparser import RawConfigParser


class Config(object):

    rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    configPath = os.path.join(rootDir, 'config\\', 'config.ini')

    @classmethod
    def getConfig(cls):
        config = RawConfigParser()
        config.read(cls.configPath,encoding='utf-8')
        return config

