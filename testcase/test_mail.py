import pytest
from common.globalmanager import get_locator_info
from pageobject.login import Login
from pageobject.setting import Setting

webInfo = get_locator_info()
login = Login()
setting = Setting()


class TestMail():

    def test_mail_001(self, driver):
        login.login(driver, 'lilinlinmail@163.com', 'linlin55')
        login.login_is_ok(driver, 'lilinlinmail')

    @pytest.mark.usefixtures('init_fun')
    def test_mail_02(self, driver):
        """163邮箱登录"""
        setting.seting(driver, '这是标题', '1234')
        setting.setting_is_ok(driver, '1234')

    def test_mail_03(self, driver):
        """163邮箱登录1"""
        login.login(driver, 'lilinlinmail@163.com', 'linlin55')
        setting.seting(driver, '这是标题', '1234')
        setting.setting_is_ok(driver, '1234')
        setting.dele_sign(driver)
        setting.dele_sign_ok(driver)