import sys
import time
import pyautogui
import os
import pyperclip
from common.logger import Logger
from common.config import Config
from common.globalmanager import GlobalManager

config = Config.getConfig()
rootPath = GlobalManager().get_value('rootPath')
logger = Logger('guibase').getLogger()


class GuiBase(object):
    SCREENSIZE = (1920, 1080)

    def __init__(self):
        self.duration = 0.2  # 设置鼠标移动速度；0为立即执行
        self.interval = 0.2  # 每次点击间隔时间；0为立即执行
        self.minSearchTime = 5  # 隐试等待时间
        # self.confidence = 0.98   #设置图片识别信任度

    def click_picture(self, el, clicks=1, button='left'):
        '''点击图片方法'''
        try:
            contrastPath = os.path.join(rootPath, config['pic']['contrastPath'], el)
            pos_x_y = pyautogui.locateOnScreen(contrastPath, minSearchTime=self.minSearchTime)
            assert pos_x_y
            pyautogui.click(pyautogui.center(pos_x_y), clicks=clicks, button=button, duration=self.duration,
                            interval=self.interval)
            logger.info('查找图片 {} 位置,点击成功'.format(el))
        except Exception as e:
            screenshotPath = os.path.join(rootPath, config['pic']['screenshotPath'], el)
            self.screenshot(screenshotPath)
            logger.error('查找图片 {} 位置, 当前屏幕无此内容，已截图'.format(el))
            raise e

    def rel_picture_click(self, el, rel_x=0, rel_y=0, clicks=1, button='left'):
        '''图像的相对位置点击'''
        try:
            contrastPath = os.path.join(rootPath, config['pic']['contrastPath'], el)
            pos_x_y = pyautogui.locateOnScreen(contrastPath, minSearchTime=self.minSearchTime)
            assert pos_x_y
            pyautogui.moveTo(pos_x_y, duration=self.duration)  # 移动到 (100,100)
            pyautogui.moveRel(rel_x, rel_y, duration=self.duration)  # 从当前位置右移100像素
            pyautogui.click(clicks=clicks, button=button, duration=self.duration)
            logger.info('查找图片 {} 位置,点击成功'.format(el))
        except Exception as e:
            screenshotPath = os.path.join(rootPath, config['pic']['screenshotPath'], el)
            self.screenshot(screenshotPath)
            logger.error('查找图片 {} 位置, 当前屏幕无此内容，已截图'.format(el))
            raise e

    def mouse_click(self, posx=0, posy=0, clicks=1, button='left', flag=1):
        '''鼠标点击方法'''
        if flag == 1:
            pyautogui.click(posx, posy, clicks=clicks, button=button, duration=self.duration, interval=self.interval)
            logger.info('鼠标在坐标{},{} 点击{}键 {}次'.format(posx, posy, button, clicks))
        elif flag == 2:
            pyautogui.moveRel(posx, posy, duration=self.duration)  # 从当前位置右移100像素
            pyautogui.click(button=button, clicks=clicks)  # 鼠标当前位置点击一下

    def check_result(self, el):
        '''检查图片是否存在'''
        picPath = os.path.join(rootPath, config['pic']['contrastPath'], el)
        try:
            assert pyautogui.locateOnScreen(picPath, minSearchTime=self.minSearchTime)
        except AssertionError as e:
            logger.error('点击“ {} ”未返回正确结果'.format(el.split('.')[0]))
            raise e
        logger.info('点击“ {} ” 返回结果正确'.format(el.split('.')[0]))

    def ispicture(self, el):
        '''判断图片是否存在'''
        picPath = os.path.join(rootPath, config['pic']['contrastPath'], el)
        x, y = pyautogui.locateCenterOnScreen(picPath, minSearchTime=self.minSearchTime)
        isnot = pyautogui.onScreen(x, y)
        if isnot == True:
            return True
        else:
            return False

    def moveto(self, posx=0, posy=0, flag=1):
        '''鼠标移动方法'''
        if flag == 1:
            pyautogui.moveTo(posx, posy, duration=self.duration)
            logger.info('鼠标偏移{},{}'.format(posx, posy))
        else:
            pyautogui.moveRel(posx, posy, duration=self.duration)
            logger.info('鼠标移动到{},{}'.format(posx, posy))

    def drag_to(self, posx, posy, button='left', flag=1):
        '''鼠标拖拽'''
        if flag == 1:
            pyautogui.dragTo(posx, posy, duration=self.duration, button=button)
            logger.info('鼠标拖拽{},{}'.format(posx, posy))
        elif flag == 2:
            pyautogui.dragRel(posx, posy, duration=self.duration)
            logger.info('鼠标相对拖拽{},{}'.format(posx, posy))

    def type(self, str):
        '''键盘输入'''
        pyautogui.write(str, interval=self.interval)
        logger.info('文本框输入{}'.format(str))

    def scroll(self, amount_to_scroll, moveToX=None, moveToY=None):
        '''鼠标滚动'''
        pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
        logger.info('鼠标在{}位置滚动{}值'.format(moveToX, moveToY), amount_to_scroll)

    def input_cn(self, text):
        '''输入中文'''
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        logger.info('{}输入完成'.format(text))

    @classmethod
    def screen_size_check(cls):
        if cls.SCREENSIZE != pyautogui.size():
            logger.error("SystemError:plz use 1080p resolution")
            sys.exit(1)
        else:
            print("screen resolution {}\nrun test...............".format(pyautogui.size()))

    def screenshot(self, name):
        pyautogui.screenshot(name)

    @staticmethod
    def always_get_position():
        while True:
            time.sleep(1)
            x, y = pyautogui.position()
            print(x, y)
