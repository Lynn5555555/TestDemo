import pytest
import time
from common.guibase import GuiBase
from common.globalmanager import get_pic_info

gui = GuiBase()
picInfo = get_pic_info()


class TestBase():
    def test_QQ_001(self):
        '''用例一：qq登录'''
        import pyautogui
        pyautogui.hotkey('win', 'd')
        time.sleep(3)
        gui.click_picture(picInfo['qq_icon'], clicks=2, button='left')
        gui.rel_picture_click(picInfo['qq_user'], rel_x=-100, clicks=1, button='left')
        gui.type('15900715134')
        gui.rel_picture_click(picInfo['qq_login'], rel_x=-100, clicks=1, button='left')
        gui.type('LiLinlin55')
        gui.click_picture(picInfo['qq_login'], clicks=1, button='left')
        time.sleep(6)
        assert gui.ispicture(picInfo['login_in_ok'])
