from common.webbase import WebBase
from common.globalmanager import get_locator_info
import time
from common.logger import Logger

logger = Logger('Setting').getLogger()
webInfo = get_locator_info()


class Setting():

    def seting(self, driver, title, content):
        web = WebBase(driver)
        web.click(webInfo["setting"])
        web.click(webInfo["normal_set"])
        web.click(webInfo["sign"])
        time.sleep(3)
        web.click(webInfo["add_sign"])
        time.sleep(1)
        web.sendKeys(webInfo["in_title"], title)
        web.switch_iframe(webInfo['frame2'])
        web.sendKeys(webInfo["in_content"], content)
        web.switch_iframe_out()
        web.click(webInfo["save"])
        time.sleep(3)

    def setting_is_ok(self, driver, content):
        web = WebBase(driver)
        assert web.get_text(webInfo["is_success"]) == content

    def dele_sign(self, driver):
        '''删除签名'''
        web = WebBase(driver)
        time.sleep(2)
        web.click(webInfo['dele'])
        time.sleep(1)
        web.click(webInfo['dele_ok'])
        time.sleep(10)

    def dele_sign_ok(self, driver):
        web = WebBase(driver)
        alert = web.switch_alert()

        assert web.get_text(webInfo['dele_success']) == '还没有创建任何签名哦!'
