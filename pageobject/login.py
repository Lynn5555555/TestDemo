from common.webbase import WebBase
from common.globalmanager import get_locator_info
import time

webInfo = get_locator_info()


class Login():

    def login(self, driver, username, psw):
        """163邮箱登录"""
        web = WebBase(driver)
        driver.get("https://mail.163.com")
        driver.maximize_window()
        web.switch_iframe(webInfo['frame'])
        web.sendKeys(webInfo['username'], username)
        web.sendKeys(webInfo['psw'], psw)
        web.click(webInfo['login'])
        time.sleep(3)

    def login_is_ok(self, driver, username):
        web = WebBase(driver)
        assert web.get_text(webInfo['is_login']) == username
