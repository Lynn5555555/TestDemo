import logging
import time
from common.config import Config
from common.globalmanager import GlobalManager
import os

config = Config.getConfig()
rq = time.strftime('%Y%m%d_%H%M', time.localtime()) + '.log'
rootPath = GlobalManager().get_value('rootPath')


class Logger(object):

    def __init__(self, name):
        self.name = name
        self.logPath = config['log']['path']
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)
        # self.streamHandler = logging.StreamHandler()
        self.fileHandler = logging.FileHandler(os.path.join(rootPath, self.logPath, rq), 'a', encoding='utf-8')
        self.formatter = logging.Formatter(config['log']['fmt'])
        # self.streamHandler.setLevel(logging.INFO)
        self.fileHandler.setLevel(logging.DEBUG)
        self.fileHandler.setFormatter(self.formatter)
        # self.streamHandler.setFormatter(self.formatter)
        # self.logger.addHandler(self.streamHandler)
        self.logger.addHandler(self.fileHandler)

    def getLogger(self):
        return self.logger
